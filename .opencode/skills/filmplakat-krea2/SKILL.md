---
name: filmplakat-krea2
description: Baut aus einem Einzeiler ein kinoreifes Filmplakat (One-Sheet) für den Kurzfilm „Echo im Rost“ auf lokalem Krea-2-Turbo: Poster-Kompositions- und Typografie-Layer, fester Credit-Block (Gruppe 17, Daniel Sawazki, Fabian Weismüller) und immer gut lesbarer „KI-generiert“-Hinweis, danach dichte English-Caption nach comfyui-kreatool-Regeln und Render auf dem lokalen Mac-Workflow. Use when the user asks for a Plakat, Poster, One-Sheet, Key Art, Teaser-Poster or Plakat-Prompt for the short film.
---

# Filmplakat Krea 2 — One-Sheet-Pipeline „Echo im Rost“

Poster-Spezialschicht **auf** der bestehenden Krea-2-Pipeline. Diese Skill ersetzt comfyui-kreatool nicht, sie ergänzt den Pflichtlayer „Kino-Plakat“ (Komposition × Typografie × Credits) und liefert die hier dokumentierte lokale Renderstraße.

## 0. Pipeline (Reihenfolge zwingend)

1. `comfyui-kreatool/SKILL.md` laden (unter `~/.config/opencode/skills/comfyui-good-krea/`) — deren harte Regeln gelten unverändert: dichte Natural-Language-Caption, Pflicht-Kompositionsschicht (§3), Fotolayer (§3.5), ~150–230 Wörter, kein Tag-Listing, keine Quality-Tokens, keine Gewichtssyntax, Konfliktcheck (§10), Stil-Anker (E018), keine `muted/desaturated/subdued`-Wörter (E019), Palette- Enumeration (§12).
2. **Diesen Skill anwenden**: §2 Feste Projektdaten unverändert einsetzen, §3 Typografie-Layer, §4 Komposition, §5 Montage-Template bauen.
3. Render: auf diesem Rechner §8 (lokaler Mac-Workflow). Auf RTX-Maschinen stattdessen `comfyui-manager/SKILL.md` mit Workflow `local/krea2-turbo-txt2img`.
4. Text-QA nach §7; Plan B (§7.3) erst nach 3 fehlenden Rolls vorschlagen.

AUP der Krea-2-Lizenz weiterhin bindend.

## 1. Was „echtes Filmplakat“ hier heißt

Ein One-Sheet, kein illustriertes Bild mit Text darauf. Messlatten, die die Caption sichtbar erfüllen muss:

- **Ein Bildgedanke, eine Achse.** Kino-Plakate tragen eine Idee (Figur im Nebel, Kopf unten, Antenne als Nadel). Zwei Bildideen → zwei Poster.
- **Hierarchie in vier Stufen:** Titel › Subtitle/Tagline › Credits › Legal-Hinweis. Größen- und Gewichtsabstände sind Teil des Designs und gehören in die Caption beschrieben.
- **Typografie sitzt nur in Ruhezonen** (Nebel, Himmel, dunkle Asphaltbandene), nie über Detailstruktur oder Gesicht.
- **Safe Area:** alle Texte ≥ ~8 % Randabstand; Credits-Zeile never touching frame edge.
- **Ein Farbakzent maximum** als Leitpunkt (hier: Signalrot), Titelschrift bleibt ein einziges Schriften-System.

## 2. Feste Projektdaten (verbatim, nicht umformulieren)

**Titelblock**

- Titel: `ECHO IM ROST` — groß, weitlaufende schmale Großbuchstaben, cream-weiß, leichte Abnutzung, horizontal, exakt einmal.
- Subtitle: `EIN KURZFILM` — klein, weiter Laufabstand, direkt unter dem Titel.
- Tagline (optional, nur wenn sonst ≤ 5 Textzeilen): `EIN SIGNAL. EINE ANTWORT.`

**Credit-Block (Pflicht, immer, Wortlaut fix)**

- Zeile A: `GRUPPE 17 PRÄSENTIERT`
- Zeile B (Namen, immer): `EIN FILM VON DANIEL SAWAZKI UND FABIAN WEISMÜLLER`
- Zeile C (klein): `HOCHSCHULE FULDA · MODUL KI IN DER MEDIENPRODUKTION · AB 07.03.2027`

Regeln zum Credit-Block:

- Zeile B ist **nicht verhandelbar und nie weglassen**; der Name heißt korrekt **Weismüller** mit einfachem S — im Plakat-Großbuchstaben-Setting `WEISMÜLLER` (ein S, kein ß). Ü bleibt Ü.
- Voll-Billing (Prof. etc.) nur wenn explizit gewünscht — lange Mikrotexte ruiniert Krea fast immer (E012); dann Zeile C weglassen und Voll-Billing als Post-Overlay (§7.3).
- Zeilen A+B dürfen zu einer Zeile verschmelzen, wenn das Layout drängt: `GRUPPE 17 PRÄSENTIERT · DANIEL SAWAZKI · FABIAN WEISMÜLLER` (dann Ü als „German umlaut spelled correctly“ qualifizieren).

**Legal-Hinweis (Pflicht, immer lesbar)**

- String exakt: `KI-generiert`
- Placement: unten, mittig, unter dem Credit-Block.
- Lesbarkeits-Satz (immer in die Caption): `a small but clearly legible note KI-generiert sits centered at the very bottom edge in clean cream letters with even spacing and strong contrast against its backdrop, in a calm quiet size but unmistakably readable`
- Nie über strukturierter Textur platzieren; nie `barely visible`/`whisper`-Formulierungen dafür benutzen (einmal verheizt = unlesbar).

**Prima-Ankerblock (unverändert einfügbar — Figurenkonsistenz)**

`its lower body is a matte cream sphere covered in rust-brown scratches with an olive-green lower shell resting on two small gray rubber wheels; a black corrugated coil neck joins the sphere to a smaller dome head of the same scratched cream shell across a rusty ring gap; one large round amber glass-lens eye glows softly in the dome center; a thin straight bright red antenna with a small red ball tip rises from the crown; a worn faded blue-gray canvas backpack with brown leather straps is mounted on its back; two small segmented white arms with dark joints and three-fingered pincer hands hang at its sides`

**Stil-Anker (Pflichtsatz, Position 1 der Caption)**

`Photorealistic theatrical one-sheet movie poster, indistinguishable from genuine printed key art, a 35mm anamorphic film photograph with fine grain, natural color and a gentle vignette.`

**Palette-Schluss-Satz (Standard, je Motiv anpassen)**

`Palette: fog white, pearl gray, moss green, rust brown, slate gray, with amber and signal-red accents.`

**Typografie-Closer (Pflichtsatz, letzte Caption-Zeile)**

`All lettering set in one consistent elegant sans-serif, flat graphic design layered over the photograph, perfectly horizontal, correctly spelled including German umlauts, each word appearing exactly once.`

**Licht-Physik-Bausteine** (realistisches Licht = ein motivierter Lichtgrund + Gefälle + Separation):

- Nebel: `a hidden sun diffusing through the haze creating a smooth volumetric luminance gradient that brightens toward the top`
- Filigran-Trennung: `a thin rim of light separating the shell from the mist` + `soft cool ambient bounce shaping the dome`
- Emissive Akzente = echte Lichtquellen mit Blüte: `the amber eye casting a soft warm glow on the shell below it`, `the red ball tip blooming gently in the fog` (E021: warmer Punkt braucht warme Quelle — Auge/Antenne sind solche Quellen, nie „is warm“ behaupten)
- Nasse Straßen-Reflexion nur wenn Asphalt Thema: `faint blurred red reflection on the wet cracked asphalt`

## 3. Typografie-Layer (Pflicht, vor der Caption-Montage)

1. **Textbudget:** maximal 6 Zeilen, vorzugsweise 5 (Titel, Subtitle, Zeile A+B, Zeile C, `KI-generiert`). Tagline nur auf Kosten von Zeile C.
2. Jede Zeile **wörtlich in Hochkommas-artiger Nennung** in der Caption (`the title ECHO IM ROST appears ...`), Placement pro Zeile (was/wo/größer-kleiner/Kontrast), ein Schriftsystem gesamt.
3. Zonen zuweisen: Titel-Block = obere Nebel-/Himmelsband (oberes Drittel), Credit-Block = unteres Band (Asphalt/Dunkel), `KI-generiert` = Abschluss darunter mittig. Wenn Bildidee den Boden besetzt (Kopf-Poster): Credits nach oben unter den Titel wandern lassen, `KI-generiert` bleibt unten auf freier Nebelfläche.
4. Nie zwei Zeilen derselben Hierarchiestufe unterschiedliche Größe; nie Text über dem Antennen-Spitzenpunkt oder Auge platzieren.
5. Lesbarkeit contra Nebel: heller Schrift auf dunkler Zone oder (Standard hier) cream-weiße Schrift mit `strong contrast` in mittlerem Grau des Nebels — nie weiße Schrift auf weißem Ausfressen.

## 4. Poster-Komposition (statt freier Kreativwahl; Kreativität innerhalb dieser Bahnen)

Hauptkomposition **eine** Wahl, Hilfsmechanik max. 1 (verweise auf kreatool §3 — Raum Beschreibung der „was es ist“-Form ist Pflicht). Bewährte Poster-Bahnen (verifiziert oder recipes-abgeleitet):

| Schema | Aufbau in Raum-Wörtern | Wann |
| --- | --- | --- |
| **Nebel-Minimal** (Hauptempfehlung) | Negativraum: fast das ganze Bild Nebel-Gradient, Ruinen nur als schwache Andeutung an den Bildrändern; Kopf des Roboters unten, mutig am unteren Rand beschnitten, Antenne steigt als vertikale Nadel exakt auf der Bildmittelachse, rote Kugel = einziger gesättigter Punkt im oberen Mittelfeld; Titel-Block darüber zentriert | minimalistisch, Arthouse, seriös |
| **Straßen-Fluchtpunkt** | Straßenmitte als Mittelachse, Fassaden/Kurbs/Wracks konvergieren auf den Roboter, Signalrot flammt im Fluchtpunkt; Roboter mittlere/untere Zone, Himmel oben als Nebel-Typosone | epischer, klassisches One-Sheet |
| **Kupfer-Hero (Zentrum)** | Roboter zentral, große Augenseite zur Kamera, dunkler überwucherter Hintergrund + Rim Light, Signal rot glimmend im unscharfen Hintergrund | Charakter-Poster, Teaser |
| **Kuppel-Finale** | Glas-Kuppel als C-Bogen/Strahlenkranz um den Lichtkern, Prima unten davor winzig, Morgenrot-Himmel (Nacht→Dämmerung) | Finale/Emotion |
| **Zwei-Punkt-Kontrast** | kleines dunkles Stadt-Panorama unten an der Grundlinie, oben hohler Himmel, zwei Rotpunkte (Antenne ↔ Signal) diagonal | Mood-Teaser |

Canvas: 2:3 Hochformat, ~1.1 MP (848–880 × 1264–1312). 16:9 nur auf ausdrücklichen Wunsch (Teaser-Querformat).

**Realismus-Check (aus E001/E005):** Roboter als Einzelmotiv zwischen 10 % (Minimal) und 55 % (Hero) Bildhöhe; niemals „mittig klein im Leeren“ ohne Achsenfunktion — dann Negativraum bewusst formulieren (`negative space IS the design, the robot's antenna pins the vertical axis`).

## 5. Caption-Montage (Template mit Slots)

Reihenfolge strikt; jeder Slot ein Satz-Klotz, Semantik nie doppelt:

```
[1 Stil-Anker §2] [2 Subjekt-Ankerblock §2 (in Motiv-Situation gesetzt)]
[3 Szenen-/Lichtphysik-Schicht §2-Bausteine + Ort nach Motivschema §4]
[4 Raum-Erzählung: Komposition §4 in „was es ist“-Sätzen + Kamera/Fokus aus §3.5-Fotolayer (Motivschema-Wahl: Low-Angle/Ground-Level, 35mm, deep focus; Hero: 85mm, shallow DOF eye-sharp)]
[5 Typografie-Block §3: pro Zeile ein kurzer Placement-Satz]
[6 Legal-Satz §2 KI-generiert (wörtlich)]
[7 Palette-Schluss §2]
[8 Typografie-Closer §2 (wörtlich)]
```

- Wortziel ~180–240. [2]+[3] tragen die Bildidee, [5] trägt die Plakat-Idee.
- Keine „no text“-Formulierungen (aktiviert Text), wenn Typografie gewünscht ist. Wenn bewusst textfreier Print für Post-Overlay: Textkomplett weglassen und stattdessen schreiben `a large clean empty fog band across the upper third reserved for title typography`, Legal-Satz entfällt dann (wird in Post gesetzt).

## 6. Voll-Beispiel (Nebel-Minimal, finaler Stand — als Referenz-Stil für neue Varianten)

```
Photorealistic theatrical one-sheet movie poster, indistinguishable from genuine printed key art, a 35mm anamorphic film photograph with fine grain, natural color and a gentle vignette. Almost the entire frame is a soft gradient of pale luminous mist, brightening toward the top where a hidden sun diffuses through the haze; only at the far edges the faintest ghostly suggestion of moss-covered ruined facades dissolving away. Rising from the very bottom edge, cropped boldly at its coil neck so only the head is visible, the robot's dome sits low of center, slightly right of the vertical axis: its lower body is a matte cream sphere covered in rust-brown scratches with an olive-green lower shell; a black corrugated coil neck joins the sphere to the smaller dome head of the same scratched cream shell across a rusty ring gap; one large round amber glass-lens eye glows softly and reads clearly toward the viewer; a worn faded blue-gray canvas backpack with brown leather straps sits behind the dome; two small segmented white arms with three-fingered pincer hands rest at the sides. From the crown a thin straight red antenna with a small red ball tip rises vertically along the exact central axis of the frame, the glowing tip floating in the open upper middle — the only saturated color mark in the whole poster, a red period over a page of fog, the amber eye casting a soft warm glow on the shell below it, the red ball tip blooming gently in the mist. A thin rim of light separates the dome from the fog, soft cool ambient bounce shaping the cream shell. Typography as flat elegant design: across the top fog the title ECHO IM ROST in enormous thin cream-white capital letters with very wide letter-spacing, perfectly horizontal; directly beneath, much smaller and finely spaced, the line EIN KURZFILM. Below the head on the darkest bottom band of the poster, centered small cream capitals read GRUPPE 17 PRÄSENTIERT, then one line EIN FILM VON DANIEL SAWAZKI UND FABIAN WEISMÜLLER, then a smaller line HOCHSCHULE FULDA · MODUL KI IN DER MEDIENPRODUKTION · AB 07.03.2027. Beneath all of that, a small but clearly legible note KI-generiert sits centered at the very bottom edge in clean cream letters with even spacing and strong contrast, calm and quiet but unmistakably readable. Palette: fog white, pearl gray, cream, faint moss green, rust brown, with amber and signal-red accents. All lettering set in one consistent elegant sans-serif, flat graphic design layered over the photograph, perfectly horizontal, correctly spelled including German umlauts, each word appearing exactly once.
```

## 7. QA & Roll-Strategie (Text = Risikofeld E012)

1. **Submit:** `batch_size=1`, eigener Seed pro Versuch (nie fix — der Seed ist hier Roulette-Rad, keine Konstante). 2–4 Versuche parallel, dann den Take mit fehlerfreiem Titel **und** korrekten Namen nehmen.
2. **Checkliste pro Bild** (Buchstabe für Buchstabe): ECHO IM ROST · EIN KURZFILM · GRUPPE 17 PRÄSENTIERT · DANIEL SAWAZKI · FABIAN WEISMÜLLER (ein einfaches S + Ü!) · Datum/Linie C · `KI-generiert` vorhanden und lesbar · keine Doppelgänger-Zeilen.
3. **Wiederkehrende Ausfälle → Gegenmaßnahme:** eine bestimmte Zeile verstümmelt → ihre Placement-Beschreibung kürzen und Kontrastwort erhöhen; ß/Ü kaputt → Prompt-Zeile auf `DANIEL SAWAZKI UND FABIAN WEISMULLER` (ohne Ü) degradieren ist **verboten** — stattdessen Plan B:
4. **Plan B (Post-Overlay):** saubere Print-Platte ohne Typografie rendern (Template-Ast §5 unten) und Credit-/KI-Zeile in DaVinci Resolve/GIMP als echte Schrift setzen. Titel-Zone bleibt als Nebel-Negativraum bestehen.

## 8. Renderstraße auf diesem Rechner (Mac, ohne comfyui-skill/RTX-VSR)

Arbeitsworkflow: `comfy_workflows/image_krea2_turbo_t2i.json` (API-Format) per HTTP auf `http://127.0.0.1:8188` (ComfyUI ≥ 0.45, Krea2-Turbo-fp8-Mac-Variante). Patchen:

| Node | Feld | Wert |
| --- | --- | --- |
| `30:19` | `inputs.value` | fertige Caption (Expander-Switch `30:24` bleibt `false`) |
| `49` | `inputs.aspect_ratio` / `megapixels` / `multiple` | `2:3 (Portrait Photo)` / `1.1` / `16` (quer: `3:2 (Photo)`) |
| `30:5` | `inputs.batch_size` | `1` |
| `30:3` | `inputs.seed` | neue Zufallszahl pro Versuch |
| `29` | `inputs.filename_prefix` | `krea2/plakat_prima_<konzept>` |

Ablauf: `POST /prompt` (`{"prompt": wf, "client_id": uuid}`) → `/history/<prompt_id>` bis `outputs["29"].images[0]` (≈2–3 min) → Ergebnis nach `renders/plakat/` kopieren (Name `Krea2_turbo_plakat_prima_<konzept>_<nr>_.png`) → `log.md`-Eintrag (Seed, MP, Konzept, Take-Entscheidung). Negativ-Branch ist `ConditioningZeroOut` (cfg=1) — kein Feld dafür patchen; LoRA-Switch `30:23` bleibt `false`.

Auf Windows/RTX-Maschinen mit installiertem `comfyui-skill`-CLI: dieser §8 entfällt, regulär `comfyui-manager` mit `local/krea2-turbo-txt2img` (Turbo-Upscale-Kette inklusive RTX VSR).

## 9. Pre-Submit-Checkliste (Delta zu kreatool §15)

- [ ] Stil-Anker-Satz wörtlich an Position 1
- [ ] Prima-Ankerblock unfragmentiert (Konsistenz > Eleganz)
- [ ] Komposition gewählt (§4) und in Raum-Sätzen beschrieben, Achse benannt
- [ ] max. 6 Textzeilen, jede mit Placement + Kontrast; Namen-Zeile vorhanden; `KI-generiert` mit Lesbarkeits-Satz
- [ ] keine `muted/desaturated/subdued`-Wörter, Palette als Enumeration
- [ ] Safe Area: Ränder ≥ 8 %; `KI-generiert` nicht am Bildrand angeschnitten
- [ ] Canvas 2:3 / 1.1 MP (oder begründet)
- [ ] frischer Seed, `batch_size=1`, Prefix gesetzt
