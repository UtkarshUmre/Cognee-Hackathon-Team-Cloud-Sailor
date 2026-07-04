"""
Face-recognition security gate (Page 3) — powered by DeepFace.

Only enrolled "operatives" (the Wolfpack) can unlock the memory database. We keep
a small gallery of authorized faces on disk; a webcam scan is matched against it.

Design notes:
- DeepFace + OpenCV are imported lazily so the API still boots while the (heavy)
  install finishes, or on machines without them.
- Webcam frames arrive as data URLs; we decode to a BGR numpy array (the most
  reliable DeepFace input) rather than juggling base64 prefixes.
- SFace + opencv detector keeps it fast enough for a live demo.
"""

from __future__ import annotations

import base64
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

_ROOT = Path(__file__).resolve().parent.parent
GALLERY = _ROOT / "media" / "faces"          # authorized faces live here
MODEL_NAME = "SFace"                          # light + fast
DETECTOR = "opencv"                           # no extra system deps


class FaceGateError(RuntimeError):
    """Recoverable face-gate failure (no face, bad image, deps missing)."""


@dataclass(frozen=True)
class VerifyResult:
    granted: bool
    identity: Optional[str]
    distance: Optional[float]
    threshold: Optional[float]
    reason: str


def is_available() -> bool:
    try:
        import cv2  # noqa: F401
        import deepface  # noqa: F401
        return True
    except Exception:  # noqa: BLE001
        return False


def enrolled_names() -> list[str]:
    if not GALLERY.is_dir():
        return []
    return sorted(p.stem for p in GALLERY.glob("*.jpg"))


def _decode_dataurl(data_url: str):
    """data URL / base64 -> BGR numpy image (raises FaceGateError on bad input)."""
    import cv2
    import numpy as np

    if not data_url:
        raise FaceGateError("No image provided.")
    b64 = data_url.split(",", 1)[1] if data_url.startswith("data:") else data_url
    try:
        raw = base64.b64decode(b64)
        arr = np.frombuffer(raw, dtype=np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    except Exception as e:  # noqa: BLE001
        raise FaceGateError(f"Could not decode image: {e}") from e
    if img is None:
        raise FaceGateError("Decoded image was empty.")
    return img


def _clear_cache() -> None:
    """DeepFace.find caches representations in the gallery; drop it after enroll."""
    if GALLERY.is_dir():
        for pkl in GALLERY.glob("*.pkl"):
            pkl.unlink(missing_ok=True)


def enroll(name: str, data_url: str) -> str:
    """Save a webcam frame as an authorized face. Returns the stored file name."""
    import cv2

    if not is_available():
        raise FaceGateError("DeepFace/OpenCV not installed yet.")
    safe = "".join(c for c in name.strip() if c.isalnum() or c in ("-", "_")) or "operative"
    img = _decode_dataurl(data_url)
    GALLERY.mkdir(parents=True, exist_ok=True)
    out = GALLERY / f"{safe}.jpg"
    if not cv2.imwrite(str(out), img):
        raise FaceGateError("Failed to write face image.")
    _clear_cache()
    return out.name


def _embed(img):
    """SFace embedding for an image (whole frame if no face is boxed).

    enforce_detection=False means it never throws on a missing face box — it just
    embeds the frame — which keeps the demo scanner from dead-ending.
    """
    from deepface import DeepFace

    reps = DeepFace.represent(
        img_path=img,
        model_name=MODEL_NAME,
        detector_backend=DETECTOR,
        enforce_detection=False,
        align=True,
    )
    if not reps:
        return None
    return reps[0].get("embedding")


def _cosine_distance(a, b) -> float:
    import numpy as np

    va, vb = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    denom = (np.linalg.norm(va) * np.linalg.norm(vb)) + 1e-9
    return float(1.0 - (va @ vb) / denom)


def verify(data_url: str) -> VerifyResult:
    """Match a webcam frame against the enrolled gallery.

    We compute the SFace embedding ourselves and compare with a loose cutoff so
    the enrolled person is recognized reliably in a live demo (this gate is
    theater for the judges, not real security). Tunable via FACE_MATCH_CUTOFF.
    """
    import os

    import cv2

    if not is_available():
        raise FaceGateError("DeepFace/OpenCV not installed yet.")
    if not enrolled_names():
        return VerifyResult(False, None, None, None, "No operatives enrolled yet.")

    img = _decode_dataurl(data_url)
    try:
        probe = _embed(img)
    except Exception:  # noqa: BLE001
        probe = None
    if probe is None:
        return VerifyResult(False, None, None, None, "Couldn't read the frame — try again.")

    best_name, best_dist = None, 2.0
    for face_file in GALLERY.glob("*.jpg"):
        try:
            ref_img = cv2.imread(str(face_file))
            ref = _embed(ref_img) if ref_img is not None else None
        except Exception:  # noqa: BLE001
            ref = None
        if ref is None:
            continue
        d = _cosine_distance(probe, ref)
        if d < best_dist:
            best_name, best_dist = face_file.stem, d

    if best_name is None:
        return VerifyResult(False, None, None, None, "No usable enrolled face — re-enroll.")

    cutoff = float(os.getenv("FACE_MATCH_CUTOFF", "0.80"))  # loose, demo-friendly
    granted = best_dist <= cutoff
    return VerifyResult(
        granted=granted,
        identity=best_name if granted else None,
        distance=round(best_dist, 4),
        threshold=round(cutoff, 4),
        reason="Access granted." if granted else "Face not recognized.",
    )
