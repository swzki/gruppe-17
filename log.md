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