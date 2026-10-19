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