# Gruppe 17 – KI in der Medienproduktion

**Projekt:** Musikvideo, 3–5 Minuten, vollständig KI-generiert (lokal: FLUX.1 dev, Wan 2.2, ACE-Step 1.5)

**Exposé-Kandidaten (Gruppenentscheidung ausstehend, Abgabe 08.11.):**
- `expose/echo-im-rost.md` – Roboter „Prima“ in einer von der Natur zurückeroberten Stadt (diese Sitzung, LE-3-Workflow mit Kritik-Runde)
- `expose/gravity-of-wild.md` – zwei Gorillas tanzen sich in die Freiheit (Fabian, 02.11.)

## Dokumente

| Datei | Inhalt |
| --- | --- |
| `expose/` | Exposé-Kandidaten (Entscheidung offen) |
| `prompts/` | Verwendete Prompt-Vorlagen (Template + filled-in + Kritik/Überarbeitung) |
| `shotlist/` | Shotlist als JSON (gemeinsames Schema) |
| `log.md` | Alle Generierungen: Modell, Version, Seed, Parameter, Laufzeit, Entscheidungen |
| `assets.md` | Quellen, Lizenzen, Rechte-Status |
| `audio/`, `renders/`, `workflows/`, `scripts/` | Produktion |

## Pipeline (geplant)

Exposé → Drehbuch → Storyboard → Shotlist (JSON) → Song (ACE-Step) → Master-Posen (FLUX.1 dev + IP-Adapter/LoRA) → I2V-Clips (Wan 2.2) → Schnitt & Mix → Film + Poster
