# Workflows

## ideogram4_t2i – Plakat & Keyframes (ComfyUI 0.45, lokal)

Modelle/Parameter:
- Diffusion: `ideogram4_fp8_scaled.safetensors` + `ideogram4_unconditional_fp8_scaled.safetensors` (CFG-Verzweigung)
- CLIP: `qwen3vl_8b_fp8_scaled.safetensors`, type `ideogram4`
- VAE: `flux2-vae.safetensors`, Sampler: euler, 2:3 Hochformat ≈ 1 MP (848×1264)

Nutzung:
- Plakat: komplettes JSON aus `prompts/plakat_v00N.json` 1:1 in den positiven
  CLIP-Text-Encode einfügen (bbox-Werte 0–1000 relativ zum Bild).
- Der Node „Ideogram4 Caption Prompt Template“ ist nur Doku/Vorschau (führt
  ausschließlich nach „Preview as Text“). Cloud-Magic-Prompt ist laut Skript
  S. 10 nicht erlaubt; Prompt-Erzeugung läuft lokal über
  `scripts/le06_plakat.py` (oMLX).

Dateien:
- `ideogram4_t2i_api.json` – API-Format (exportiert aus der lokalen
  ComfyUI-History, über „Load“/API nutzbar)
- `ideogram4_t2i.json` – UI-Format: in ComfyUI über Datei → Speichern
  (arbeitsfähig, mit Gruppen/Notizen) hier ablegen
