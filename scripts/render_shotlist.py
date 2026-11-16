"""Rendert alle Bilder aus der Shotlist über die ComfyUI-API.

Aufruf:  python3 scripts/render_shotlist.py [--shots s01,s03] [--force]
Output:  renders/<shot_id>.png

Vorbereitung (einmalig):
1. In ComfyUI einen normalen Workflow aufbauen:
   CheckpointLoader -> positiver + negativer CLIP Text Encode -> KSampler
   -> VAEDecode -> SaveImage.
2. In den POSITIVEN Prompt exakt den Platzhalter __PROMPT__ schreiben
   (ersetzt pro Shot durch prompt_bild aus der Shotlist).
3. ComfyUI starten (Standard: http://127.0.0.1:8188).
4. Im Menü "Save (API Format)" -> Datei als workflows/echo_api.json speichern.

Das Skript setzt pro Shot außerdem den Seed aller KSampler identisch
(--seed + Shot-Index), damit die Bilder reproduzierbar werden.
Bestehende renders/<id>.png werden übersprungen (außer --force).
"""

import argparse
import copy
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

BASE = Path(__file__).resolve().parent.parent
SHOTLIST_PATH = BASE / "shotlist" / "shotlist_v001.json"
WORKFLOW_PATH = BASE / "workflows" / "echo_api.json"
OUT_DIR = BASE / "renders"

PLACEHOLDER = "__PROMPT__"


def http_json(url: str, payload: dict | None = None) -> Any:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise SystemExit(f"HTTP {e.code} von {url}:\n{body}")


def download(url: str, dest: Path) -> None:
    with urllib.request.urlopen(url) as resp, open(dest, "wb") as f:
        f.write(resp.read())


def inject_prompt(obj: Any, prompt: str) -> Any:
    """Ersetzt den Platzhalter rekursiv in allen String-Werten."""
    if isinstance(obj, dict):
        return {k: inject_prompt(v, prompt) for k, v in obj.items()}
    if isinstance(obj, list):
        return [inject_prompt(v, prompt) for v in obj]
    if isinstance(obj, str) and PLACEHOLDER in obj:
        return obj.replace(PLACEHOLDER, prompt)
    return obj


def set_seeds(workflow: dict, seed: int) -> None:
    for node in workflow.values():
        inputs = node.get("inputs", {})
        for key in ("seed", "noise_seed"):
            if key in inputs:
                inputs[key] = seed


def render_shot(comfy: str, workflow: dict, prompt: str, seed: int) -> list[dict]:
    wf = inject_prompt(copy.deepcopy(workflow), prompt)
    set_seeds(wf, seed)
    result = http_json(f"{comfy}/prompt", {"prompt": wf})
    prompt_id = result["prompt_id"]

    while True:
        history = http_json(f"{comfy}/history/{prompt_id}")
        if prompt_id in history:
            break
        time.sleep(1)

    images = []
    for output in history[prompt_id].get("outputs", {}).values():
        images.extend(output.get("images", []))
    return images


def main() -> None:
    ap = argparse.ArgumentParser(description="Shotlist -> ComfyUI -> renders/<id>.png")
    ap.add_argument("--shots", help="Komma-getrennte Shot-IDs (Default: alle)")
    ap.add_argument("--comfy", default="http://127.0.0.1:8188", help="Basis-URL von ComfyUI")
    ap.add_argument("--seed", type=int, default=42, help="Basis-Seed (pro Shot: seed + Index)")
    ap.add_argument("--force", action="store_true", help="Existierende Bilder neu rendern")
    args = ap.parse_args()

    shotlist = json.loads(SHOTLIST_PATH.read_text(encoding="utf-8"))
    if not WORKFLOW_PATH.exists():
        raise SystemExit(f"{WORKFLOW_PATH} fehlt – Workflow in ComfyUI aufbauen und per "
                         f"\"Save (API Format)\" dort speichern (siehe Docstring im Skript).")
    workflow = json.loads(WORKFLOW_PATH.read_text(encoding="utf-8"))
    if PLACEHOLDER not in json.dumps(workflow):
        raise SystemExit(f"Platzhalter {PLACEHOLDER} nicht im Workflow gefunden "
                         f"({WORKFLOW_PATH}) – bitte in den positiven Prompt schreiben.")

    shots = shotlist["shots"]
    if args.shots:
        wanted = {s.strip() for s in args.shots.split(",")}
        shots = [s for s in shots if s["id"] in wanted]

    OUT_DIR.mkdir(exist_ok=True)
    comfy = args.comfy.rstrip("/")

    for idx, shot in enumerate(shots):
        out = OUT_DIR / f"{shot['id']}.png"
        if out.exists() and not args.force:
            print(f"{shot['id']}: vorhanden, übersprungen")
            continue
        print(f"{shot['id']} ({shot['einstellung']}, {shot['songabschnitt']}): render …")
        images = render_shot(comfy, workflow, shot["prompt_bild"], args.seed + idx)
        if not images:
            print(f"{shot['id']}: FEHLER – kein Bild zurückbekommen")
            continue
        img = images[-1]
        qs = urllib.parse.urlencode({
            "filename": img["filename"],
            "subfolder": img.get("subfolder", ""),
            "type": img.get("type", "output"),
        })
        download(f"{comfy}/view?{qs}", out)
        print(f"{shot['id']}: -> {out}")

    print("Fertig.")


if __name__ == "__main__":
    main()
