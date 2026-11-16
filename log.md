## Aufgabe 1.2 – Speicherbedarf schätzen

Faustformel: **Gewichte in GB ≈ Parameter in Mrd. × Bit pro Gewicht / 8**

| Modell | 16 Bit | 8 Bit | 4 Bit |
| --- | --- | --- | --- |
| Qwen3.8-27B (27 Mrd.) | ~54 GB | ~27 GB | ~13,5 GB |
| Qwen3.8-Flash-Next (125 + 51 Mrd.) | ~352 GB | ~176 GB | ~88 GB |
| Gemma 4 26B A4B (26 Mrd.) | ~52 GB | ~26 GB | ~13 GB |

### Fragen

**Welche Varianten passen in 128 GB (macOS gibt ~75 % für die GPU frei)?**
- Verfügbarer VRAM: 128 GB × 0,75 = **96 GB**
- Qwen3.8-27B: alle Varianten (16/8/4 Bit)
- Gemma 4 26B: alle Varianten (16/8/4 Bit)
- Qwen3.8-Flash-Next: nur **4 Bit (~88 GB)** – und dann mit knappem Rest

**Welche passen nicht gleichzeitig mit einem Videomodell?**
- Qwen3.8-Flash-Next 4 Bit: Es bleiben nur ~8 GB – reicht für kein nennenswertes Videomodell
- Auch die 16-Bit-Varianten von 27B/26B zusammen mit einem größeren Videomodell werden eng

**Was kommt zu den Gewichten noch hinzu?**
- **KV-Cache:** wächst mit Kontextlänge und Batch-Größe (mehrere GB bei langen Kontexten)
- **Vision-Encoder:** separater Encoder (z. B. CLIP/SigLIP) für Bild-Eingaben
- **Overhead:** Treiber, Runtime, Zwischenergebnisse (Aktivierungen) im Forward-Pass
- **N-Gramm-Bestandteil** bei Flash-Next: zusätzliche Lookup-Tabellen



## Aufgabe 1.3 – Stationen: Werkzeuge vergleichen (35 Minuten)

| Station | Gruppen | Werkzeug |
| --- | --- | --- |
| A | 1–10 | Ollama (`ollama run qwen3.8:27b --verbose --think=false`) |
| B | 11–20 | oMLX (Web-UI) |

**Einstellungen für alle:** Qwen3.8-27B, 4 Bit, Reasoning aus, Kontextlänge 4096.

**Drei feste Prompts:**

1. kurz: „Nenne drei Märchen der Brüder Grimm.“
2. mittel: „Fasse Rotkäppchen in fünf Sätzen zusammen.“
3. lang: „Schreibe eine Szene von etwa 300 Wörtern, in der ein kleiner Roboter nachts einen Wald betritt.“

### Messung – Station B (oMLX Web-UI, Modell: Qwen3.8-27B-oQ4e-fp16-mtp)

| Prompt | Prompt-Verarb. (Tok/s) | Generierung (Tok/s) | Zeit bis 1. Token | Speicher |
| --- | --- | --- | --- | --- |
| kurz | – * | 42,1 | – * | – * |
| mittel | – * | 42,8 | – * | – * |
| lang | – * | 49,3 | 1,66 s | – * |

\* Nicht im Server-Log vorhanden → im oMLX-Dashboard ablesen.

**Rohdaten aus dem Server-Log:**

| Prompt | Prompt-Tokens | Antwort-Tokens | Dauer |
| --- | --- | --- | --- |
| kurz | 503 | 534 | 12,68 s |
| mittel | 643 | 659 | 15,41 s |
| lang | 7023 | 4135 | 85,53 s |

### Auswertung: Schätzung (1.2) vs. Messung

- **Gewichte:** Schätzung 13,5 GB (4 Bit) vs. gemessen ~16–19 GB. Die Faustformel ignoriert: gguf-Q4-Quantisierung nutzt effektiv ~4,8–5 Bit pro Gewicht, plus Vision-Encoder, KV-Cache und Runtime-Overhead.
- **Prompt-Spalte nicht direkt vergleichbar mit Station A:** Die oMLX-Web-UI schickt zu jedem Prompt einen System-Prompt (~485 Token) plus Session-Kontext mit (deshalb 503 → 643 → 7023 Prompt-Tokens), Ollama schickt nur den reinen Prompt. Zusätzlich reduziert der Prefix-Cache die Prefill-Zeit (z. B. beim lang-Prompt waren ~6.856 Token bereits gecacht).
- **MTP-Beschleunigung:** oMLX lief mit Multi-Token-Prediction (Akzeptanzrate 62–83 %) → 40–49 tok/s. Ollama ohne MTP liegt typischerweise niedriger – der Geschwindigkeitsunterschied zwischen den Stationen kommt aus der Inference-Pipeline, nicht aus dem Modell.
- **Geteilter Server:** TTFT kann Scheduler-Wartezeiten enthalten (ein Lauf zeigte 12,67 s, weil parallel andere Requests liefen) – für saubere Werte am wenigsten ausgelasteten Zeitpunkt messen.

## LE 3 – Exposé „Echo im Rost" (02.11.2026)

**Modell & Parameter:** Qwen3.8-27B (Ollama, Q4_K_M), `think=false`, Kontext 262k
- Entwurf: Temperature 0,8 · 2.390 Token · ~93 s
- Kritik (separate Anfrage): Temperature 0,7 · 1.962 Token · ~66 s
- Überarbeitung: Temperature 0,7 · 2.689 Token · ~58 s

**Prompts:** `prompts/expose_robostadt.txt` (Bausteine: Rolle, Kontext, Aufgabe, Format, Einschränkungen, Idee), `prompts/expose_kritik.txt`, `prompts/expose_ueberarbeitung.txt`. Kritiker-Output: `prompts/kritik_ergebnis.md`. Template (unbelegt, aus LE 3): `prompts/expose.txt`.

**Kritik-Runde – drei Schwächen (alle in v2 eingearbeitet):**
1. **Hologramm-Interaktion im selben Frame** (Szene 7): echtes Licht/physikalische Logik nicht zuverlässig renderbar, hohes Artefakt-Risiko am emotionalen Höhepunkt → **Interaktion durch Schnitt**: Shot A (Prima + Lichtkern, Hand ohne Berührung), Shot B (Großaufnahme Auge mit Echo-Reflexion, Post-Produktion), Shot C (nur Echo-Hologramm), im Editor montiert.
2. **„Schnelle, dynamische Schnitte" + Handkamera im Tunnel** (Szene 4): Wackelkamera ist einer der schwierigsten Effekte für Wan 2.2 (Morphing, Verformung), frisst das Clip-Budget → **3–4 statische/lineare Shots** (frontal, seitlich, Rückansicht), Dynamik ausschließlich im Schnitt.
3. **Figurenkonsistenz**: „Figur nicht im Video-Prompt beschreiben" reicht nicht, Wan 2.2 hat keinen Gedächtniskontext → **I2V für jeden Clip aus 5 Master-Posen** (FLUX.1 dev, Identität via IP-Adapter/LoRA), im Wan-Prompt nur die Bewegung.

**Verworfen (und warum):** Wackelkamera/Follow-Shots (technisch nicht zuverlässig), gemeinsamer Frame Prima + Echo (nicht renderbar), „Refrain = schnelle Schnitte im Modell" (Clip-Budget + Artefakt-Risiko).

**Entscheidungen (diese Sitzung):**
- Roboter-Name: **Prima**; Echo ausschließlich als Hologramm (zählt zur 2-Figuren-Grenze, aber kein physischer Konsistenz-Druck)
- Prima: ca. 30 cm, cremefarbene Schale + rostfarbene Kratzer, bernsteinfarbenes Auge, rote Antenne, grauer Rucksack (5 feste Merkmale, in jedem Prompt identisch)
- 4 Orte: Straße/Rooftops, U-Bahn-Tunnel, Parklichtung, Glas-Kuppel
- Twist (Echo = gespeicherte Erinnerung) in Szene 7, direkt nach der leisen Bridge (Park, Regen, Antenne erlischt) → Finale = Signal + Stadt erwacht
- Musik: Cinematic Post-Rock, ~70 BPM, **weibliche, ethereale Vocals im Refrain** (ACE-Step 1.5) – von der Gruppe zu bestätigen
- Resultat: `expose/echo-im-rost.md` (endgültig, inkl. manueller Korrektur von Logline und Tippfehlern)
- Hinweis: Parallel existiert der Exposé-Kandidat `expose/gravity-of-wild.md` (Fabian, 02.11.). Gruppenentscheidung, welche Exposé am 08.11. abgegeben wird, ist noch offen.

## LE 3 – Drehbuch, Storyboard, Shotlist (02.11.2026)

**Erstellt:** Drehbuch (8 Szenen) + Storyboard (43 Shots) + Shotlist als JSON.

**Drehbuch** (`expose/drehbuch_echo_im_rost.txt`): 8 Szenen mit Szenenkopf (INT./EXT. ORT – TAGESZEIT) und Songabschnitt pro Szene; nur Sichtbares und Hörbares, keine Gedanken; ohne Dialog.

**Storyboard** (`expose/storyboard_echo_im_rost.txt`): pro Szene 3–6 Einstellungen, einheitliches Vokabular (Totale/Halbtotale/Nah/Groß/Detail; statisch/Schwenk/Fahrt/Zoom/Handkamera). Laut Exposé nur statische oder lineare Kamera (Fahrt) – Dynamik ausschließlich im Schnitt.

**Shotlist** (`shotlist/shotlist_v001.json`), erzeugt per Skript `scripts/generate_shotlist.py`, validiert gegen `shotlist/schema.json` (jsonschema):
- 43 Shots, Summe `dauer_s` = **240 s** (Pfad: 180–300 s)
- Figurenmerkmale (Prima, Echo) **identisch formuliert in jedem `prompt_bild`** (Skript-Check)
- Shots pro Szene: {1: 6, 2: 6, 3: 5, 4: 5, 5: 6, 6: 4, 7: 5, 8: 6} (alle 3–6)
- Alle `einstellung`/`kamera`-Werte aus dem Schema-Enum

**Entscheidungen:**
- Song-Struktur über 8 Szenen: Intro / Strophe 1 / Strophe 2 / Refrain 1 / Bridge / Bridge-Ende / Refrain 2 (Auflösung) / Finaler Refrain + Outro.
- Shot-IDs `s01`–`s43`; Storyboard-Tabelle verweist 1:1 auf die Shotlist-IDs.
- Shotlist ist **vorläufig** – in LE 7 wird sie an die reale Songstruktur von ACE-Step angepasst.
## LE 6 – Bild-Workflows & Plakat (16.11.2026)

**Plakat-Pipeline (Übung 6.1, alles lokal):** `prompts/plakat_idee.txt` → `scripts/le06_plakat.py` → oMLX (`/v1/chat/completions`, Modell `Qwen3.8-27B-oQ8e-mtp`, temperature 0.4, `response_format: json_schema`) → validiert gegen `prompts/ideogram4_schema.json` (bbox 0–1000, Titel/Credits/Hinweis buchstabentreu) → `prompts/plakat_v002.json`. API-Key aus `$OMLX_API_KEY` oder `~/.config/opencode/opencode.json`.

**Plakat-Iterationen (je Version nur ein Element gezielt geändert):**
- `v002` (oMLX-Entwurf): Titel doppelt + „Prime 17“ statt „Gruppe 17“ – Ursache: „Prima，“ am Anfang der figure-Beschreibung wurde als Bildtext gerendert
- `v003`: photorealistischer Look + „official theatrical one-sheet“ statt Illustration
- `v004`: Roboter ohne Beine, nur rollende Kugel (Designentscheid, von Gruppe bestätigt)
- `v005`: zweites Kugel-Element ergänzt – Kopfkuppel auf festem Ring, Rucksack auf Joch darüber (bleibt beim Rollen an derselben Stelle)
- `v006`: Modell kopierte BB-8 → „no panels/decals/orange, exactly ONE eye, not based on any existing movie robot“; Tagline gekürzt, alle Texte „horizontal, sharp, readable“
- `v007` (**aktueller Entwurf**): Credits als echter Billing-Block: GRUPPE 17 PRÄSENTIERT · HOCHSCHULE FULDA · MODUL KI IN DER MEDIENPRODUKTION · PROF. DR. JAN-TORSTEN MILDE · AB 07.03.2027
- Zusatz: `prompts/plakat_krea2_turbo.json` (paralleler Entwurf, separate Renderstraße)

**Figuren-Redesign Prima (Gruppenentscheid):** Beine entfernt – Unterkörper = rollende Kugel (~40 cm), darauf Kopfkuppel mit Ringspalt, ein bernsteinfarbenes Auge, rote Antenne; Rucksack hinter der Kuppel montiert. Character Sheet (`expose/echo-im-rost.md`) und `PRIMA`-Merkmale in `scripts/generate_shotlist.py` angepasst; Shotlist neu generiert und validiert (43 Shots, 240 s, Merkmale identisch).

**ComfyUI-Workflow (lokal, kein Cloud-Magic-Prompt laut Skript S. 10):** Ideogram-4-T2I-Kette: `ideogram4_fp8_scaled` + `ideogram4_unconditional_fp8_scaled` (uncond-Branch), `CLIPLoader qwen3vl_8b_fp8_scaled` (type ideogram4), VAE `flux2-vae`, Sampler euler, Format 2:3 Hochformat ≈1 MP (848×1264). Das Plakat-JSON geht **direkt** in den positiven CLIP-Text-Encode; der „Ideogram4 Caption Prompt Template“-Node ist wirkungslos (führt nur nach „Preview as Text“) und bleibt als Doku für 6.4 erhalten. Export: `workflows/ideogram4_t2i_api.json` (API-Format, aus der lokalen ComfyUI-History); UI-Format muss in ComfyUI noch per Datei → Speichern unter `workflows/ideogram4_t2i.json` gesichert werden.

**Bisherige Renders in `renders/`:** Poster-Durchläufe (Ideogram 4.0, mehrere Versionen, zuerst mit Titel-/Credit-Fehlern), erste Keyframes aus Qwen Image 2.1; Originale in der hessenbox. Struktur: `renders/plakat/` (Ideogram-Plakat-Durchläufe) und `renders/keyframes/` (Qwen-Image-Keyframes); `workflows/ideogram4_t2i_api.json` jetzt als offizieller API-Export aus ComfyUI ("Export (API)"). UI-Format weiterhin offen.

**To-dos bis Meilenstein:** Plakat v007 rendern und bewerten; Keyframe für jede der 8 Szenen (Übung 6.4) gegen Character Sheet prüfen; Inpainting-Fixes (6.2); Upscaling-Vergleich (6.3); UI-Workflow-Export; alles in Moodle hochladen.
