"""Erzeugt das Plakat-JSON (Ideogram 4) über die lokale oMLX-API (Übung 6.1).

Aufruf:  python3 scripts/le06_plakat.py [--model NAME] [--force]
Input:   prompts/plakat_idee.txt, prompts/ideogram4_schema.json,
         prompts/plakat_v001.json (Beispiel aus Übung 5.3)
Output:  prompts/plakat_v002.json  -> in ComfyUI in den Ideogram-4-Workflow
         einfügen, Hochformat (z.B. 1024x1536), rendern.

Das Skript prüft danach:
- Schema-Validierung (inkl. bbox-Werte 0-1000)
- Titel, Credits und "KI-generiert" buchstabentreu als content der
  Text-Elemente
- Schlüssel in der Reihenfolge des Schemas

Der API-Key kommt aus $OMLX_API_KEY oder aus ~/.config/opencode/opencode.json
(provider.omlx.options.apiKey). Er wird niemals ausgegeben.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

import jsonschema
import requests

BASE = Path(__file__).resolve().parent.parent
SCHEMA_PATH = BASE / "prompts" / "ideogram4_schema.json"
BEISPIEL_PATH = BASE / "prompts" / "plakat_v001.json"
IDEE_PATH = BASE / "prompts" / "plakat_idee.txt"
OUT_PATH = BASE / "prompts" / "plakat_v002.json"

# Diese Zeichenketten müssen exakt (buchstabentreu) als text.content auftauchen.
EXAKT_TEXT = ["Echo im Rost", "Gruppe 17", "KI-generiert"]


def load_api_key() -> str:
    key = os.environ.get("OMLX_API_KEY")
    if key:
        return key
    cfg = Path.home() / ".config" / "opencode" / "opencode.json"
    data = json.loads(cfg.read_text(encoding="utf-8"))
    key = data["provider"]["omlx"]["options"].get("apiKey")
    if not key:
        sys.exit("Kein API-Key: OMLX_API_KEY setzen oder in opencode.json eintragen.")
    return key


def pick_model(base_url: str, key: str) -> str:
    resp = requests.get(f"{base_url}/models", headers={"Authorization": f"Bearer {key}"}, timeout=30)
    resp.raise_for_status()
    ids = [m["id"] for m in resp.json().get("data", [])]
    if not ids:
        sys.exit("oMLX meldet keine geladenen Modelle – bitte im Dashboard prüfen.")
    for mid in ids:
        if "qwen3.8" in mid.lower():
            return mid
    return ids[0]


def chat(base_url: str, key: str, model: str, schema: dict, beispiel: str, idee: str) -> str:
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    body = {
        "model": model,
        "temperature": 0.4,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Schreibe einen Ideogram-4-JSON-Prompt nach diesem Beispiel. "
                    "Antworte nur mit JSON.\n" + beispiel
                ),
            },
            {"role": "user", "content": idee},
        ],
    }
    resp = requests.post(
        f"{base_url}/chat/completions",
        headers=headers,
        json={
            **body,
            "response_format": {
                "type": "json_schema",
                "json_schema": {"name": "ideogram4", "schema": schema, "strict": False},
            },
        },
        timeout=600,
    )
    if resp.status_code >= 400:
        print(f"json_schema abgelehnt ({resp.status_code}), fallback auf json_object")
        resp = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json={**body, "response_format": {"type": "json_object"}},
            timeout=600,
        )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def parse_json(text: str) -> dict:
    text = text.strip()
    match = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, re.DOTALL)
    if match:
        text = match.group(1)
    return json.loads(text)


def order_keys(obj: Any, schema: dict) -> Any:
    """Bringt Schlüssel rekursiv in die Reihenfolge des Schemas."""
    if isinstance(obj, dict) and "properties" in schema:
        props = schema["properties"]
        out = {k: order_keys(obj[k], props[k]) for k in props if k in obj}
        out.update({k: v for k, v in obj.items() if k not in out})
        return out
    if isinstance(obj, list):
        items = schema.get("items", {})
        return [order_keys(v, items) for v in obj]
    return obj


def check(plakat: dict, schema: dict) -> None:
    jsonschema.validate(plakat, schema)
    print("OK: Schema validiert (bbox-Werte liegen per Schema zwischen 0 und 1000)")

    contents = [e.get("content", "") for e in plakat["elements"] if e.get("kind") == "text"]
    for wanted in EXAKT_TEXT:
        if wanted not in contents:
            sys.exit(f"FEHLER: Text-Element {wanted!r} fehlt oder ist nicht buchstabentreu: {contents}")
        print(f"OK: {wanted!r} exakt vorhanden")

    figuren = [e for e in plakat["elements"] if e.get("kind") == "figure"]
    if not figuren:
        sys.exit("FEHLER: kein figure-Element – Hauptfigur fehlt im Plakat.")
    print(f"OK: {len(figuren)} figure-Element(e), {len(contents)} text-Element(e)")


def main() -> None:
    ap = argparse.ArgumentParser(description="Plakat-JSON mit oMLX erzeugen (Übung 6.1)")
    ap.add_argument("--url", default="http://localhost:8000/v1", help="OpenAI-API-Basis von oMLX")
    ap.add_argument("--model", help="Modell-ID (Default: Qwen3.8-Modell vom oMLX-Server)")
    ap.add_argument("--out", default=str(OUT_PATH), help="Zieldatei (Default: prompts/plakat_v002.json)")
    ap.add_argument("--force", action="store_true", help="Existierende Ausgabedatei überschreiben")
    args = ap.parse_args()

    out = Path(args.out)
    if out.exists() and not args.force:
        sys.exit(f"{out} existiert bereits – mit --force überschreiben.")

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    beispiel = BEISPIEL_PATH.read_text(encoding="utf-8")
    idee = IDEE_PATH.read_text(encoding="utf-8")

    key = load_api_key()
    model = args.model or pick_model(args.url, key)
    print(f"Modell: {model}")

    raw = chat(args.url, key, model, schema, beispiel, idee)
    plakat = order_keys(parse_json(raw), schema)
    check(plakat, schema)

    out.write_text(json.dumps(plakat, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Geschrieben: {out.relative_to(BASE)} – bereit für den Ideogram-4-Workflow in ComfyUI.")


if __name__ == "__main__":
    main()
