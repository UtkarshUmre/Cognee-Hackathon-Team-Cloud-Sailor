# 🐕 Wolfpack Recall — *Hangover 4: Berlin*

> **"Build AI that doesn't forget."** — Cognee × WeMakeDevs Hackathon · **Team Cloud Sailor**

## 🎬 Watch the trailer

[![Wolfpack Recall — watch the trailer on YouTube](https://img.youtube.com/vi/k0fobTzngVk/maxresdefault.jpg)](https://www.youtube.com/watch?v=k0fobTzngVk)

**▶ [Watch the trailer on YouTube](https://www.youtube.com/watch?v=k0fobTzngVk)** — the
story in ~50s (reunion → the founder's Mr. Chow cameo → the tattooed code → the dog-show
win → the live Cognee graph). For the full interactive experience, open the live app below.

## ▶️ Try it live (no setup)

### 👉 **https://wolfpack-recall.onrender.com**

📱 **Works great on your iPhone / Android too — give it a try!** *(The mobile experience
is in **beta**, so a few things may look slightly off on small screens — but the full
5-page story is playable end to end on a phone.)*

**Judges: it's deployed and fully playable in your browser.** Walk the 5-page story
end to end — hit **🕵️ Auto Detective** to solve the case in one click (or investigate
manually), watch the founder talk (real lip-synced video), crack the code, scan your
face, win the dog show, and explore the **live Cognee knowledge graph**. There's a
free, no-login **"Ask AI agent about Cognee"** guide on the last page (plus an optional
free-AI upgrade that uses **Puter**, which asks for a quick, free one-time Puter sign-in).

*(Face ID uses your camera and only works over HTTPS — the Render URL qualifies. If a
public HF Space is briefly rate-limited, the app degrades gracefully; nothing blocks.)*

---

## What it is

Four friends wake up in a trashed Berlin apartment with **no memory** of last night.
Their dog **Pinky** is gone — and the code to a locker at the **Karlovci Gymnasium in
Sremski Karlovci, Serbia. **Pinky the dog has a tattoo on her belly with the code information. Using **Cognee** as the brain,
four AI personalities reconstruct the night, recover Pinky, crack the code, get inside,
and win the dog show.

It's a **playable metaphor for the hackathon theme**: the hangover *is* lost context,
and **Cognee is the memory that survived**. Every clue, character, and location lives in
a real Cognee knowledge graph — and the app *shows you that graph*.

---

## The 5-page journey

| Page | What happens | Cognee / tech on display |
|------|--------------|--------------------------|
| **1 · Intro** | AI movie poster, brief mission, who's-who, "what happens" | AI image gen (FLUX) |
| **2 · Investigation** | Add clues → they're `remember()`-ed into Cognee. Ask **4 AI personalities** who reason over Cognee's `GRAPH_COMPLETION`. Mark clues ✓/✗ or **🔍 fact-check against memory** (green/red). Pinky walks a storyline route as clues are confirmed. | `remember` · `recall` · `GRAPH_COMPLETION` · fact-check vs memory · node_sets |
| **3 · Access** | Reunion video (Pinky reveals the belly code **8675309**) + **Founder chat (Chow mode)** → enter the code → **facial-recognition scan** (DeepFace). Unlocks on code **and** face. | DeepFace face recognition · accented TTS |
| **4 · Success** | "You're in" → the **dog-show winning video** plays | AI video |
| **5 · Cognee** | The **live, real Cognee knowledge graph** (Cognee's own UI, embedded), toggle vs our storyline map, switch datasets. Free **no-login "Ask AI agent about Cognee"** guide (+ optional free-AI upgrade via **Puter**, which asks for a quick free sign-in). | Cognee `visualize` graph · datasets · built-in guide + **free Puter.js AI** |

---

## 🌳 The three trees (how it all fits together, at a glance)

Three quick maps for reviewers — the **logic** (what happens when a user acts), the
**resources** (every tool/model and who pays), and **Cognee** (exactly how we exercise it).

### 1) Logic tree — a user action → what runs

```
User opens the app (5 narrative pages, vanilla JS)
│
├─ Page 1  Intro / poster ................ AI poster (FLUX) + cast strip
│
├─ Page 2  Investigation
│    ├─ Add a clue ....................... Browser → FastAPI /clues
│    │                                       → Cognee remember() → cognify pipeline
│    ├─ "Ask the Wolfpack" ............... FastAPI /investigate
│    │    ├─ (1) Cognee recall() / GRAPH_COMPLETION  → pulls connected evidence
│    │    └─ (2) 4 Claude agents reason over that evidence (concurrently)
│    │             Planner · Wildcard · Worrier · Optimist
│    ├─ 🔍 Fact-check a clue ............. FastAPI /validate → Cognee vs Claude → true/false
│    └─ 🕵️ Auto Detective ............... loops the above hands-free; Pinky walks to the gym
│
├─ Page 3  Access
│    ├─ Reunion video reveals code 8675309 (auto-plays Pinky's bark)
│    ├─ Founder "Mr. Chow" cameo ........ pre-rendered lip-synced clips
│    ├─ Enter code  +  Scan face ........ FastAPI /auth/verify → DeepFace (local, on server)
│    └─ code AND face  →  unlock the gym
│
├─ Page 4  Success ...................... dog-show winning video
│
└─ Page 5  Cognee graph
     ├─ Live embedded Cognee UI ......... FastAPI proxies /cognee/graph (key stays server-side)
     ├─ Dataset picker .................. switch memory graphs (pinky_serbia ⇄ mr_chow …)
     └─ "Ask AI agent about Cognee" ..... built-in guide (no login) + optional free Puter AI
```

### 2) Resource tree — every tool/model and who pays

```
Wolfpack Recall
├─ Memory / knowledge graph .... Cognee Cloud (open source) ............. free dev plan
├─ Reasoning (4 agents + check). Claude — Haiku 4.5 in prod / Opus local . owner key (rate-limited)
├─ Movie poster ................ FLUX.1-schnell on a Hugging Face Space ... free (HF Space)
├─ Founder ~3s video ........... Omni-Video-Factory (image→video, HF) .... free (HF Space)
├─ Founder lip-sync ............ fal.ai `sync-lipsync` (hosted) .......... ~cents/clip
├─ Founder / Chow voice ........ edge-tts (MS Neural, zh-CN-YunxiNeural) . free, keyless
├─ Face recognition ............ DeepFace (open source) — SFace + YuNet/RetinaFace
│                                weights baked into the Docker image at build time,
│                                run on our own server ................... FREE · $0/scan · no API
├─ Page-5 help chat ............ built-in guide + optional Puter.js AI ... user-pays → $0 to us
└─ Hosting ..................... Docker on Render ........................ free/hobby-tier friendly

Backend  FastAPI (backend/api.py · wolfpack.py · cognee_client.py · face_gate.py · video_gen.py)
Frontend vanilla JS · vis-network · CSS tokens        Secrets  .env (git-ignored, server-side only)
```

> **Cost philosophy — built to run as close to *free* as possible.** Everything open or
> free is used that way: **Cognee** (open-source, free dev plan), **DeepFace** face
> recognition (open-source models **downloaded into the Docker image**, run locally — **$0
> per scan, no paid API**), **FLUX** + **Omni-Video-Factory** (free Hugging Face Spaces),
> **edge-tts** (free, keyless), and the **Puter** help chat (user-pays → $0 to us). The
> **only** paid pieces are the owner's **Claude** calls (rate-limited + cheap Haiku in prod)
> and the one-time **fal.ai** lip-sync used to pre-render the founder clips — everything
> else costs nothing to run.

### 3) Cognee tree — how we exercise it across its whole surface

```
Cognee Cloud  (the brain)
├─ Memory-native API
│    ├─ remember()  ............ ingest a clue + cognify into hybrid vector+graph memory
│    └─ recall() / GRAPH_COMPLETION  fuse every clue into one grounded answer
├─ Fact-checking .............. 🔍 asks the graph: is this statement true / false / unknown
├─ Datasets (memory graphs)
│    ├─ pinky_serbia  ......... the live case memory (default)
│    ├─ mr_chow  .............. 1,000 lines of Mr. Chow dialogue → its own auto-built graph
│    └─ pinky_case · cloud_sailor_memory  (earlier graphs)
├─ node_sets .................. verified / timeline / all  (per-lens tagging)
├─ Ontology / schema .......... cognee/ontology.ttl (Dog, Person, Location, Clue, Code, Event)
├─ Cognee Skill ............... cognee/skills/wolfpack-recall.md (procedural playbook)
└─ visualize .................. Page 5 embeds Cognee's REAL UI + graph (not a mockup)
```

---

## 🧠 Cognee — used across its whole surface (the "Best Use of Cognee" story)

Most teams call `add()` + one search. We exercise Cognee deeply:

- **Memory-native API** — `remember()` (ingest + cognify) and `recall()` throughout.
- **`GRAPH_COMPLETION`** — a broad recall fuses *every* clue into one grounded answer;
  the 4 personas reason over it. The graph even **disambiguated** dog-Pinky from an
  unrelated "person Pinky" node, letting all four independently debunk a false lead.
- **Fact-checking against memory** — the **🔍 check** button asks Cognee whether a new
  statement is `true / false / unknown` vs the established graph (green/red on the node).
- **Datasets we created on Cognee Cloud:**
  - **`pinky_serbia`** — the live case memory (the whole investigation graph).
  - **`mr_chow`** — the Mr. Chow character dataset (1,000 lines) ingested as its own graph.
  - (plus earlier `pinky_case`, `cloud_sailor_memory`, `hackathon_demo`).
- **Node_sets** (`verified` / `timeline` / `all`) — per-lens tagging of clues.
- **Ontology / Memory Schema** — `cognee/ontology.ttl` (Dog, Person, Location, Clue,
  Code, Event) to ground entities and unify "the gym / school / Karlovci Gymnasium".
- **Cognee Skill** — `cognee/skills/wolfpack-recall.md`, a procedural playbook in
  Cognee's Skill format.
- **The real graph, embedded** — Page 5 proxies Cognee Cloud's `visualize` endpoint and
  shows **Cognee's actual UI + graph** (dark mode, Schema tab), not a mockup. Switch
  datasets to explore each memory.
- **BEAM benchmark** framing — graph memory beats plain RAG on long-context recall.

See **`docs/COGNEE_SHOWCASE.md`** for the full mapping and pitch walkthrough.

### 🔄 How a clue flows through the investigation (Page 2)

Each piece of evidence travels the same pipeline — from raw case file, into Cognee's
memory graph, back out through the AI agents, and onto the screen:

| Stage | What it does |
|-------|--------------|
| **`seed_clues.json`** | Holds the original case evidence — the starting clue pack. |
| **Evidence Locker** (UI) | Lets users add new clues during the investigation. |
| **Cognee `remember()`** | Sends each clue into Cognee memory (ingest). |
| **Cognee `cognify` pipeline** | Processes the clues into a queryable knowledge-graph memory. |
| **Cognee `recall()` / `GRAPH_COMPLETION`** | Retrieves connected evidence back out of the memory graph. |
| **Wolfpack AI agents** | The 4 personas reason over the recalled Cognee evidence. |
| **Investigation page** (UI) | Displays recalled evidence, agent responses, clue status (✓/✗), and storyline progress. |

**In one line:** `seed_clues.json` + user input → `remember()` → `cognify` →
`recall()` / `GRAPH_COMPLETION` → Wolfpack agents → the investigation UI.

---

## 🤖 Models & AI services used

| Purpose | Model / service | Open? | Cost model |
|---------|-----------------|-------|-----------|
| **Memory / knowledge graph** | **Cognee** (Cloud) | **Open source** | Free dev plan |
| 4 investigation personalities + fact-check | **Claude** — Opus 4.x locally, **Haiku 4.5 on the public deploy** | Proprietary | App key (rate-limited) |
| **Movie poster** | **FLUX.1-schnell** via a free **Hugging Face Space** | **Open source** | Free (HF Space) |
| **Founder talking videos** | **Omni-Video-Factory** image-to-video HF Space | Open weights | Free (HF Space) |
| **Real lip-sync** (founder mouths the lines) | **fal.ai `sync-lipsync`** | Hosted | ~cents/clip |
| **Accented "Mr. Chow" voice** | **edge-tts** (Microsoft Neural, `zh-CN-YunxiNeural`) | **Free/open** | Free, keyless |
| **Facial recognition gate** | **DeepFace** (SFace + OpenCV) | **Open source** | Free, local |
| **"Ask AI agent about Cognee"** guide | Built-in guide (free, **no login**) + optional **Puter.js** free AI (GPT-4o-mini, **free one-time Puter sign-in**) | Free, keyless for us | **User-pays — $0 to us** |

**Why these choices:** we leaned on **free/open** tooling wherever possible (HF Spaces,
edge-tts, DeepFace, Puter) so the app is reproducible and cheap, and reserved paid calls
(fal.ai lip-sync) for the one thing open Spaces couldn't do reliably.

### 🎥 How the founder's ~3-second "Mr. Chow" clips were made (third-party AI, not our own model)

The short talking-head clips of the **Cognee founder in "Mr. Chow" mode** (`media/clips/founder_say_*.mp4`,
`founder_data.mp4` — ~3 seconds each) are **not generated by any model we trained or by a
pipeline we built.** We're upfront about that: they're assembled from **existing third-party
AI services**, wired together with small scripts in `scripts/`:

1. **Still → moving video — [Omni-Video-Factory](https://huggingface.co/spaces/FrameAI4687/Omni-Video-Factory)**
   (an **open-weights image-to-video** model, run for free on a **Hugging Face Space**). It takes
   one still image of the founder and animates it into a short talking clip. Script:
   `scripts/gen_founder_video.py`.
2. **Accented voice — [edge-tts](https://github.com/rany2/edge-tts)** (Microsoft Neural TTS,
   `zh-CN-YunxiNeural`), free and keyless, generates the exaggerated "Mr. Chow" one-liners as MP3s.
   Script: `scripts/gen_chow_audio.py`.
3. **Real lip-sync — [fal.ai `sync-lipsync`](https://fal.ai/models/fal-ai/sync-lipsync)** (a hosted
   model, ~cents/clip) takes the video from step 1 + the audio from step 2 and makes the founder's
   **lips actually match our voice** — the audio is baked into the final MP4. Script:
   `scripts/gen_lipsync_fal.py`.

So the clip pipeline is **Omni-Video-Factory (image→video) → edge-tts (voice) → fal.ai
sync-lipsync (lips)** — three external AI tools stitched together, chosen so the result is cheap,
reproducible, and mostly open. **Our own engineering** is the orchestration, the accented-voice
concept, the latency-hiding pool of pre-generated clips, and the app around them — **not** the
underlying video/voice models. (The *longer* ~8-second story videos — the reunion, code-to-gym,
and dog-show clips — are separate pre-rendered assets, not part of this founder pipeline.)

### Protecting the Anthropic account on a public link

The Wolfpack personas, fact-check, and guide call **Claude with the app owner's Anthropic
key** (server-side — the key is **never** sent to the browser and is only read from an
environment variable, never committed to git). Because the demo is shared publicly, we
hardened it so strangers can't run up the owner's bill:

- **Cheaper model in production** — the public deploy runs **Claude Haiku 4.5** (~15×
  cheaper than Opus) via the `WOLFPACK_MODEL` env var; Opus is used only for local demos.
- **Tight token caps** — personas answer in one sentence (`max_tokens` 90 / 40 / 320).
- **Per-IP rate limiting** — the Claude-backed endpoints (`/investigate`, `/validate`,
  `/cognee/ask`) allow ~6 calls per IP per 10 min (configurable), returning HTTP 429 past
  that. Tunable via `WOLFPACK_RATE_MAX` / `WOLFPACK_RATE_WINDOW`.
- **Owner spend cap** — a hard monthly usage limit is set in the Anthropic console, so
  spend simply stops if the cap is ever reached.

Net effect: a bounded, pennies-scale cost even under public traffic, and the key itself
is unreachable by end users.

---

## 🔐 What actually happens during the face scan (Page 3)

The Access page uses **real facial recognition**, not a gimmick — and it's worth
knowing exactly what it does (and doesn't) do:

1. **Capture** — your browser grabs a single webcam frame locally and sends it to
   our own backend (over HTTPS). It is **never sent to any third-party face API**.
2. **Detect** — the server runs **open-source [DeepFace](https://github.com/serengil/deepface)**
   with an **OpenCV** detector to find a face in the frame. On **enroll** we reject
   the photo if no clear face is found, so you don't get saved with a bad reference.
3. **Embed & match** — the **SFace** neural network turns the face into a numeric
   embedding (a "faceprint") and compares it to the enrolled gallery by distance.
   Under the model's threshold → **access granted**; over it → **denied**.
4. **Storage** — the reference image lives only in the app's local `media/faces/`
   folder (git-ignored PII). Your face is **not** stored in Cognee or any database.

**Why it sometimes takes a second:** the delay is the **open-source DeepFace model
computing locally** — and the **first** scan is slowest because the model weights
load into memory. **It is *not* a Cognee/database lookup** (Cognee stores the *case*
memory — clues, characters, locations — never faces). After the first scan it's quick.

### The slow-first-scan bug — how we found it and fixed it

**Symptom.** During testing the *first* face scan after a fresh deploy took several
seconds, which felt like the app was "calling out" to a slow service.

**Diagnosis.** We traced the request path and confirmed the face gate makes **zero
network calls** — no HuggingFace, no fal.ai, no Cognee, no database. So the time was
pure server-side compute on Render. It broke down into three parts:
1. **Render cold start** — if the instance had spun down while idle, the request first
   waits for the container to wake (this is a hosting-tier behaviour, not our code).
2. **First-scan model load** — even though the SFace weights are **pre-baked into the
   Docker image** at build time, TensorFlow + the model still had to load into RAM the
   *first* time a scan ran after each restart. This was the dominant, fixable cost.
3. **CPU inference** — Render has no GPU, so each match is a couple seconds of CPU work.

**Fix.** On server **startup** we now preload the SFace model in a background thread
(`face_gate.warm_up()` fired from a FastAPI startup event), so the heavy one-time load
happens at boot instead of on the first user's scan. `GET /auth/status` reports a
`warm` flag, and the Access page shows **"warming up the model…"** → **"scanner ready —
fast scans"** so users know the state. We also **pre-download the weights in the
Dockerfile** so nothing is fetched at runtime.

**Remaining caveat.** On a hosting tier that lets the instance sleep when idle, the
very first request after a sleep still pays the container wake-up (Render cold start).
Keeping the instance always-on removes that; the model warm-up above removes the rest.

**Getting a clean match:** look straight at the camera, keep your head level (don't
tilt or turn), **remove glasses/hats**, and use good, even lighting so your face
fills the frame. Glasses, sharp angles, or backlighting are the usual reasons a scan
is denied — the app now tells you this on screen when a face can't be read.

---

## 🛠️ Techniques & engineering

- **Multi-agent reasoning** — four distinct Claude personas (Planner / Wildcard / Worrier /
  Optimist) reason concurrently over one shared Cognee memory, each with a node-set lens.
- **Audio-driven lip-sync** — instead of matching lips to text, we feed the founder video +
  our accented MP3 into fal.ai so his lips match *our* voice (audio baked in).
- **Latency hiding** — a committed **pool** of pre-generated videos plays instantly; no waits.
- **Live knowledge-graph embed** — server-side proxy of Cognee's `visualize` so the API key
  stays hidden and the iframe dodges `X-Frame-Options`; post-processed to open dark + Schema.
- **Web Audio reactive avatar** — the cameo's sound bars react to real audio amplitude.
- **Graceful degradation** — every external dependency (DeepFace, HF Spaces, Puter) falls
  back cleanly so a demo never dead-ends.
- **"Ask AI agent about Cognee"** — a no-login AI agent on Page 5 answers questions
  about Cognee (what it is, remember/recall, GRAPH_COMPLETION, datasets, MCP) and helps
  visitors who are stuck. It runs on a built-in guide by default (free, instant, works
  on any device, **no login**); a one-tap opt-in loads **Puter.js** free AI (GPT-4o-mini,
  client-side, zero cost to us) for deeper answers. Puter uses a **user-pays** model, so
  the first time a visitor enables it, **Puter asks them for a quick, free one-time
  sign-in** to their own Puter account; if they'd rather not, the no-login built-in guide
  keeps working (it's also the automatic fallback).

---

## 🏗️ Architecture

```
Browser  (5 narrative pages · vis-network · Puter.js chat)
   │  REST
FastAPI backend  (backend/api.py)
   ├── Wolfpack orchestrator (backend/wolfpack.py) ─ 4 Claude personas + fact-check + guide
   ├── Cognee client (backend/cognee_client.py) ─ Cognee Cloud: remember · recall · visualize
   ├── Face gate (backend/face_gate.py) ─ DeepFace enroll/verify
   └── Cameo video pool (backend/video_gen.py)
Cognee Cloud  = the brain (datasets · ontology · graph · skills)
```

## Project structure

```
backend/    api.py · wolfpack.py · cognee_client.py · personalities.py · face_gate.py · video_gen.py
frontend/   index.html · investigate.html · security.html · success.html · graph.html
            css/styles.css   js/{common,landing,investigate,security,graph,cameo}.js
cognee/     ontology.ttl · skills/wolfpack-recall.md
data/       seed_clues.json · mr_chow_responses.csv
media/      images (poster, Pinky, cast) · clips (talking + lip-synced + story videos) · audio (Chow TTS)
scripts/    seed.py · gen_poster*.py · gen_founder_video.py · gen_lipsync_fal.py · gen_chow_audio.py · ingest_chow.py
docs/       OUTLINE.md · BUILD_PLAN.md · COGNEE_SHOWCASE.md · DEPLOY.md
```

## Run locally

```bash
python -m pip install -r requirements.txt
cp .env.example .env          # add Cognee + Anthropic keys
python scripts/seed.py        # seed the case into Cognee (--ask to demo)
uvicorn backend.api:app --reload   # http://127.0.0.1:8000
```

Deploy: `render.yaml` Blueprint (Docker) — see `docs/DEPLOY.md`.

## 🎓 Lessons learned (how the build actually evolved)

Real engineering is a sequence of "it works… but" moments. A few that shaped this app:

- **Talking founder: text-to-lips is the wrong order.** Our first cameo played a muted
  generative video with a separate TTS track over it — the lips never matched. The fix
  was to invert it: bake our accented voice **into** the video with **fal.ai lip-sync**,
  so the mouth follows *our* audio. We also stopped routing the video through Web Audio
  (a suspended AudioContext was desyncing/muting it). Same bug bit Page 3 later; we moved
  it to the same lip-synced clips.
- **"Not all the founder lines show up."** Turned out to be **browser cache**, not missing
  files — the app was serving JS/CSS with no cache rules, so phones ran stale code. Fixed
  at the root: the backend now serves **HTML/JS/CSS with `no-cache`** (media stays cached),
  so new UI ships without anyone needing a hard refresh.
- **The face scan felt slow — was it calling out to something?** We traced it and proved
  the face gate makes **zero network calls** (no HuggingFace, no Cognee, no DB). The delay
  was loading the **open-source DeepFace model into RAM on the first scan**. Fixes: **warm
  the model at server startup** in a background thread, **pre-bake the weights into the
  Docker image**, and **pre-warm the backend when the poster (Page 1) loads** so it's ready
  by Page 3. We also learned to **reject a bad enroll photo** (glasses/angle) up front with
  on-screen tips, instead of silently saving a reference that fails later.
- **A public link means strangers spend *your* AI budget.** The personas call Claude with
  the owner's key. Before sharing widely we hardened it: **Claude Haiku in production**
  (~15× cheaper than Opus), **per-IP rate limiting** (HTTP 429 past the budget), **tight
  token caps**, key kept **server-side only**, and a **spend cap** in the Anthropic console.
  Lesson: treat any owner-funded API behind a public demo as a spend surface, not a detail.

  **A note to the judges on cost — this runs on pennies.** We were deliberate about
  minimizing paid resources. The only owner-funded calls are the Claude ones, and they're
  squeezed on every axis:
  - **Model:** Claude **Haiku 4.5**, not Opus (~15× cheaper per token).
  - **Tiny responses:** personas answer in one sentence — `max_tokens` **90 / 40 / 320**.
  - **Rate limiter with a rolling reset:** each IP gets **30 AI calls per 10 minutes**;
    it's a **sliding window that automatically frees up** as old calls age out (past the
    10-minute mark), so legitimate judges never feel it, but no single visitor can spin the
    meter. Past the budget the API returns a friendly HTTP 429 "please wait" instead of
    another paid call.

  Put together, a Haiku call at these token caps costs a **fraction of a cent**, and even a
  visitor maxing out all 30 calls in a window spends **pennies** — hard-bounded by the
  window and by the Anthropic spend cap. Everything else in the app is **free/open**:
  Cognee (dev tier), DeepFace (local), edge-tts, the HF Spaces, and the Page-5 help chat
  (Puter is *user-pays*, $0 to us). **The paid footprint is intentionally minimal.**
- **Mobile ≠ desktop.** Page 5's graph cramped on phones (locked `100dvh`), so we let it
  scroll with a dedicated graph block; a fixed-width scanner box wouldn't center under a
  `text-align: center` parent (needs `margin: 0 auto`). Small CSS truths, real polish.
- **Keep Cognee for what Cognee is best at.** We deliberately did **not** push faces or
  blobs into Cognee — it's a *memory/knowledge-graph* layer for the case (clues, people,
  places). Faces stay local; if we productionized enrollment we'd use **Supabase pgvector**
  for embeddings. Using the right tool per job kept the "Best Use of Cognee" story clean.
- **The face scanner saga — the right detector matters more than the model.** This one
  cost us the most time, so it's worth documenting end-to-end:
  - **Symptom:** enrollment worked, but every scan returned **"No face detected — access
    denied,"** even sitting perfectly still, well-lit, face filling the frame.
  - **False trails:** we assumed browser cache, then Render's ephemeral disk wiping the
    enrolled face on each redeploy (real, but not the cause), then a too-strict match
    threshold, then `DeepFace.find` silently pre-filtering non-matches to an empty result.
    We even briefly made it "always grant," which we reverted — a demo that *looks* fake
    when a judge tests a different face is worse than a slow one.
  - **Root cause (found by reproducing locally):** the **OpenCV Haar detector** DeepFace
    used by default **cannot reliably box a real webcam face** — it works on crisp images
    but not live camera frames. So detection failed *before* any matching happened, and the
    "no face" error surfaced as access denied. Same-face-vs-itself matched fine (distance
    0.13 < 0.59) — proving the *matching* was never the problem, the *detection* was.
  - **Fix 1 (works):** a **detector fallback chain** — try a detector, fall back to a more
    robust one if it can't find a face, before ever denying.
  - **Fix 2 (fast):** **RetinaFace** was robust but ~**10 s per scan** on CPU (a fixed cost —
    shrinking the image didn't help), which froze the user. We swapped in **YuNet** as the
    primary detector: **~50 ms** *and* robust on real faces. Final chain:
    **YuNet → OpenCV → RetinaFace** (fast, with a reliable slow backstop). Detector weights
    are **pre-baked into the Docker image** so there's no first-request download in the
    cloud. Tunable live via the `FACE_DETECTORS` env var — no redeploy to re-order.
  - **Lessons:** (1) with off-the-shelf CV, the **detector** is usually the weak link, not
    the recognition model; (2) **reproduce locally with the exact library version** before
    guessing — one local repro replaced a dozen blind deploys; (3) on ephemeral hosting,
    **redeploys wipe runtime state** (our enrolled faces), which masqueraded as a code bug;
    (4) don't "solve" a demo by faking success — keep it real (turn your head → still denies)
    but make it *reliable and fast*.
- **A camera left recording.** The webcam stream was started but never released, so the
  recording light stayed on. Small but real: we added a Start/Stop toggle and auto-release
  the camera after a successful scan and on page exit.
- **Guard the good states with tags.** After several regressions (a stray "revert" wiped
  the poster styling; the scanner broke and came back), we started dropping **git tags** at
  each confirmed-working milestone (`good-demo-*`) so any regression is a one-command
  rollback. Cheap insurance during a fast, iterative crunch.
- **A MutationObserver that fought itself.** On Page 5 the embedded Cognee graph's
  node-detail panel covered the whole screen on phones and wouldn't dismiss. We inject
  mobile CSS+JS (into the HTML we already proxy) to turn it into a drawer that auto-parks
  to a pull-tab after ~4s. It worked on desktop but **the panel would flicker and never
  stay parked on mobile.** Two bugs, both subtle:
  1. **Wrong visibility check.** Cognee's *Schema* panel (`#schema-side-panel`) is shown/
     hidden with inline `display:none` → `block`, but our code tested **opacity** (always
     `1`), so it never correctly detected show vs hide. Fix: check
     `display !== 'none' && opacity !== '0'` — covering both the schema panel (display) and
     the graph panel (`#info-panel`, which toggles opacity/`.visible`).
  2. **The observer triggered itself into a loop.** Our `MutationObserver` watched the
     panel's `class` attribute. When our 4s timer *added* the `wr-parked` class, the
     observer saw that class change, assumed the panel was "shown again," and **removed the
     park** — instantly, forever. Fix: track the previous visibility state and **only react
     to real hidden↔shown transitions**, ignoring our own class toggles (`wr-parked` doesn't
     change `display`/`opacity`, so `wasVisible` stays the same → no reaction → no loop).
  Also made the parked panel `position: fixed` so the slide-off `translateX` isn't clipped
  by a parent's `overflow`, and set the proxied graph response to `no-cache` so the fix
  actually reaches phones. **Lesson:** a MutationObserver must distinguish *external*
  mutations from *its own*, or it will chase its tail — guard on a real state transition,
  not on every attribute change.

## 🧹 After the hackathon (site teardown)

Once judging and the demo are complete, **the live site will be taken down**: the
**Render** web service and any paid/cloud resources (Render instance, the Anthropic key
on the deploy, fal.ai usage) will be **discontinued**, so `https://wolfpack-recall.onrender.com`
may stop responding. **The full source stays public on GitHub** — anyone can read it,
fork it, and run it locally (see **Run locally** above) with their own Cognee + Anthropic
keys. In short: **the hosted demo is temporary; the code is permanent.**

## Tracks targeted
Best Use of Cognee Cloud · Best Use of Open Source · Best Blogs · Social Buzz.

---

## Tech, in one line
**Cognee Cloud** (memory graph) · **Claude Opus 4.x** (agents) · **DeepFace** (face ID) ·
**FLUX.1-schnell** + **Omni-Video-Factory** (HF Spaces) · **fal.ai sync-lipsync** ·
**edge-tts** · **Puter.js** · **FastAPI** · **vis-network** · **Docker/Render**.

*Team Cloud Sailor · Cognee × WeMakeDevs · 2026*
