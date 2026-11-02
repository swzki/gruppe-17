---
marp: true
theme: default
paginate: true
style: |
  section {
    font-family: "Helvetica Neue", "Segoe UI", Arial, sans-serif;
    background: radial-gradient(ellipse at 30% 10%, #1f2a2b 0%, #12181a 55%, #0a0e10 100%);
    color: #ece6da;
    padding: 1.5vh 3.2vw;
    font-size: 0.86em;
  }
  section::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(0,0,0,0) 60%, rgba(0,0,0,0.22) 100%);
    pointer-events: none;
  }
  section:not(.lead)::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #8a4b2a, #b5561f, #d97a2b, #8a4b2a);
  }
  h1, h2, h3 { color: #f5efe5; font-weight: 700; letter-spacing: 0.01em; }
  h1 { font-size: 1.9em; margin: 0.1em 0 0.2em; }
  h2 {
    font-size: 1.35em;
    border-bottom: 2px solid rgba(217, 122, 43, 0.55);
    padding-bottom: 0.18em;
    margin: 0 0 0.55em;
  }
  h3 { font-size: 1.02em; color: #f0c288; margin: 0.45em 0 0.25em; }
  a { color: #f0c288; }
  strong { color: #f5d6a0; }
  em { color: #d8cfc0; }
  code {
    font-family: "SF Mono", Menlo, monospace;
    background: rgba(217, 122, 43, 0.16);
    color: #f0c288;
    padding: 0.1em 0.35em;
    border-radius: 4px;
  }
  pre {
    background: rgba(0,0,0,0.5);
    border-left: 3px solid #b5561f;
    border-radius: 6px;
    padding: 0.7em 0.9em;
    font-size: 0.95em;
  }
  pre code { background: none; padding: 0; }
  blockquote {
    border-left: 4px solid #d97a2b;
    background: rgba(217, 122, 43, 0.12);
    padding: 0.5em 0.9em;
    margin: 0.5em 0;
    color: #ece6da;
    border-radius: 0 6px 6px 0;
  }
  hr { border: none; border-top: 1px solid rgba(217, 122, 43, 0.35); margin: 1em 0; }
  li { margin: 0.18em 0; line-height: 1.35; }
  ul { padding-left: 1.2em; }
  li::marker { color: #d97a2b; }
  p { margin: 0.32em 0; line-height: 1.35; }
  table { width: 100%; border-collapse: collapse; font-size: 0.86em; }
  th {
    color: #f0c288;
    text-align: left;
    border-bottom: 2px solid rgba(217, 122, 43, 0.6);
    padding: 0.32em 0.6em;
  }
  td {
    padding: 0.32em 0.6em;
    border-bottom: 1px solid rgba(236, 230, 218, 0.14);
    color: #ece6da;
  }
  tr:nth-child(even) td { background: rgba(255,255,255,0.03); }
  section > footer {
    position: absolute;
    bottom: 1.1vh;
    left: 3.2vw;
    right: 3.2vw;
    font-size: 0.72em;
    color: #b0a898;
    display: flex;
    justify-content: space-between;
  }
  section > footer .meta { color: #8a8378; }
  section.lead {
    background:
      radial-gradient(ellipse at 70% 20%, rgba(217, 122, 43, 0.20) 0%, rgba(0,0,0,0) 55%),
      radial-gradient(ellipse at 20% 90%, rgba(90, 120, 90, 0.16) 0%, rgba(0,0,0,0) 50%),
      linear-gradient(160deg, #17211f 0%, #0e1315 60%, #080b0c 100%);
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  section.lead::before { display: none; }
  section.lead h1 { font-size: 2.8em; margin-bottom: 0.1em; }
  section.lead h2 {
    font-size: 1.2em;
    border-bottom: none;
    color: #d8cfc0;
    margin-top: 0.4em;
  }
  section.lead .badge {
    display: inline-block;
    margin-top: 1.3em;
    padding: 0.45em 1.3em;
    border: 1px solid rgba(217, 122, 43, 0.7);
    border-radius: 999px;
    color: #f0c288;
    font-size: 0.9em;
    letter-spacing: 0.05em;
  }
  section img {
    border-radius: 10px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.5);
    border: 1px solid rgba(217, 122, 43, 0.25);
    max-height: 48vh;
    object-fit: contain;
  }
  section .two {
    display: flex;
    gap: 2.2vw;
    align-items: flex-start;
    flex-wrap: wrap;
  }
  section .two > div { flex: 1 1 46%; min-width: 0; }
  section .figures3 {
    display: flex;
    gap: 1.5vw;
    align-items: flex-start;
    flex-wrap: wrap;
  }
  section .figures3 > div {
    flex: 1 1 28%;
    min-width: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.45em;
  }
  section .figures3 img { width: 100%; max-height: 38vh; object-fit: contain; }
  section .cards3 {
    display: flex;
    gap: 1.3vw;
    align-items: stretch;
    flex-wrap: wrap;
  }
  section .cards3 > div {
    flex: 1 1 28%;
    min-width: 0;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(217, 122, 43, 0.28);
    border-radius: 10px;
    padding: 0.65em 0.85em;
    font-size: 0.88em;
  }
  section .figure { text-align: center; }
  section .figure img { max-height: 44vh; object-fit: contain; }
  section .figure p, section .figure em { font-size: 0.8em; color: #b0a898; }
  section .card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(217, 122, 43, 0.28);
    border-radius: 10px;
    padding: 0.65em 0.85em;
    font-size: 0.9em;
  }
  section .card h3 { margin: 0 0 0.3em; font-size: 1em; }
---

<!-- _class: lead -->
# „Echo im Rost"

## Aktuellder Stand der Roboter-Idee

**Gruppe 17 · KI in der Medienproduktion · 02.11.2026**

<div class="badge">Exposé-Kandidat · Abgabe 08.11. · Gruppenentscheidung offen</div>

---

# Auf einen Blick

::: two
::: figure
![akt1](assets/akt1_strasse.svg)
:::
::: figure
**Logline:** Ein einsamer Roboter entdeckt in einer von der Natur zurückeroberten Stadt, dass seine verlorene Partnerin nie weg war, sondern in ihm lebt – und weckt mit seinem Signal die Lichter der toten Stadt wieder zum Leben.

- **Format:** Musikvideo, 3–5 Min., vollständig KI-generiert (lokal)
- **Figuren:** 2 → Roboter „Prima" + Echo als Hologramm
- **Orte:** 4 → Straße, U-Bahn-Tunnel, Parklichtung, Glas-Kuppel
- **Leitmotiv:** das rote Signal
:::
:::

---

# Die Figuren

::: two
::: figure
### Prima (Protagonist)

- Kleiner, runder Roboter, ~30 cm, cremefarbene Schale mit rostfarbenen Kratzern
- Ein großes, rundes **Bernstein-Auge** (Emotionen via Helligkeit/Fokus)
- Dünne, **leuchtend rote Antenne** als Signalgeber
- Kleiner, abgenutzter **grauer Rucksack**
- Kompakt und stämmig, kurze dicke Beine
:::
::: figure
### Echo (nur als Hologramm)

- Identische runde Schale, aber **ohne Rost**, mit innerem Glimmen
- Stärker strahlendes Auge, Antenne schimmert **blau**
- Halbtransparent, Pixel-Artefakte an den Rändern, schwebend

> Visuell bewusst von Prima abgesetzt → kein physischer Konsistenz-Druck
:::
:::

---

# Handlung in drei Akten

::: figures3
::: figure
![straße](assets/akt1_strasse.svg)
**Akt 1 · Das Signal**
:::
::: figure
![tunnel](assets/akt2_tunnel.svg)
**Akt 2 · Die Suche**
:::
::: figure
![kuppel](assets/akt3_kuppel.svg)
**Akt 3 · Die Erkenntnis**
:::
:::

- **Akt 1:** Primas Auge öffnet sich in einer überwucherten Straße, rote Antenne pulsiert schwach.
- **Akt 2:** U-Bahn-Tunnel, Moos, Signal wird schwächer. *Bridge:* Parklichtung, Regen, Antenne erlischt.
- **Akt 3:** Signal wird klar → Glas-Kuppel. **Twist:** Echo ist eine in Prima gespeicherte Erinnerung. Finale: Stadt erwacht.

---

# Bildstil

::: two
::: figure
**Farbpalette**
- Gedämpfte Erdtöne: Moosgrün, Rostbraun, Schiefergrau
- Kontrast-Akzente: Bernstein-Gelb (Auge), intensives Signal-Rot
- Finale: warmes Morgenrot + kühles Blau im Schatten

**Licht**
- Akt 1: diffuses Morgengrau
- Tunnel: hartes, kaltes Licht von oben
- Kuppel: weiches, inneres Leuchten

**Kamera**
- Cinematisch, leicht anamorpher Look
- **Nur statische oder lineare Bewegungen** (Dolly/Truck)
- Keine Follow-Shots → Dynamik ausschließlich im Schnitt
:::
::: figure
![palette](assets/palette.svg)
:::
:::

---

# Musikstil (ACE-Step 1.5)

**Stil:** Cinematic Post-Rock mit orchestralen Elementen

| Abschnitt | Klang |
| --- | --- |
| **Intro/Strophe** | Tiefe Drums, Synth-Pads, Gitarren-Klirrer, ~70 BPM, melancholisch |
| **Refrain** | Percussion, epische Streicher, hallende Synths, **weibliche ethereale Vocals** |
| **Bridge** | Minimalistisch: pulsierender Bass + Antennen-Sounddesign |
| **Finale Refrain** | Volles Orchester, triumphale Melodie, Vocals klarer; Ende = hallender Akkord + „Einschalten" der Stadt |

> ⚠️ Weibliche ethereale Vocals im Refrain – **noch von der Gruppe zu bestätigen**

---

# Produktions-Pipeline

::: two
::: figure
```
Exposé → Drehbuch → Storyboard
       → Shotlist (JSON)
       → Song (ACE-Step)
       → Master-Posen (FLUX.1 dev)
       → I2V-Clips (Wan 2.2)
       → Schnitt & Mix → Film + Poster
```

- **Bild:** FLUX.1 dev · **Video:** Wan 2.2 (I2V)
- **Musik:** ACE-Step 1.5 · **Post:** ComfyUI / DaVinci Resolve
:::
::: figure
![finale](assets/akt3_finale.svg)
:::
:::

---

# Technik: Konsistenz & I2V

::: two
::: figure
**Kern-Problem:** Wan 2.2 hat **keinen Gedächtnis-Kontext** über Clips hinweg.

**Lösung: I2V für jeden Clip**
1. FLUX.1 dev: **ein** perfektes Master-Bild in der Ziel-Pose
2. Als **Startframe** für Wan 2.2 nutzen
3. Im Wan-Prompt **nur die Bewegung**, keine Figur
4. Identität via **IP-Adapter / LoRA** erzwingen

**5 Master-Posen:** stehend · rollend · Kopf gesenkt · Hand ausgestreckt · Auge offen
:::
::: figure
![master posen](assets/master_posen.svg)
:::
:::

---

# Risiken & Lösungen (Kritik-Runde)

::: cards3
::: card
### 1 · Hologramm-Interaktion
**Risiko:** Prima + Echo im selben Frame → Licht/Schatten-Physik bricht zusammen.

**Lösung:** *Interaktion durch Schnitt* – Shot A (Prima + Lichtkern), Shot B (Auge, Reflexion in Post), Shot C (nur Echo). A+C wechseln.
:::
::: card
### 2 · „Wackelkamera"
**Risiko:** Handheld + schnelle Schnitte = Morphing, frisst Clip-Budget.

**Lösung:** 3–4 *statische/lineare Shots* (frontal, seitlich, Rückansicht). Dynamik durch Schnitttempo.
:::
::: card
### 3 · Figurenkonsistenz
**Risiko:** Modell interpretiert Figur neu (Antenne rot/orange, Auge groß/klein).

**Lösung:** Strenge *I2V-Pipeline* mit 5 Master-Images, Identität via IP-Adapter/LoRA.
:::
:::

---

# Finale: Interaktion durch Schnitt

::: two
::: figure
**Kein gemeinsamer Frame.** Die emotionale „Berührung" entsteht im Rhythmus des Schnitts:

- **Shot A:** Prima + Lichtkern, Hand ohne Berührung (Partikel in Post)
- **Shot B:** Großaufnahme Auge mit Echo-Reflexion (Post)
- **Shot C:** nur Echo-Hologramm, allein, pulsierend
- **Montage:** A + C schnell wechseln → Verbindung im Kopf des Zuschauers
:::
::: figure
![schnitt](assets/schnitt_montage.svg)
:::
:::

---

# Was wurde verworfen (und warum)

| Verworfen | Grund |
| --- | --- |
| Wackelkamera / Follow-Shots | technisch nicht zuverlässig mit Wan 2.2 |
| Gemeinsamer Frame Prima + Echo | nicht renderbar, physikalisch unsinnig |
| „Refrain = schnelle Schnitte im Modell" | Clip-Budget + Artefakt-Risiko |

> **Prinzip: Dynamik entsteht im Schnitt, nicht im Modell.**

---

# Entscheidungen (diese Sitzung, 02.11.)

- **Roboter-Name:** Prima
- **Echo:** ausschließlich als Hologramm (zählt zur 2-Figuren-Grenze)
- **Prima:** 5 feste Merkmale, in jedem Prompt identisch
- **4 Orte:** Straße, U-Bahn-Tunnel, Parklichtung, Glas-Kuppel
- **Twist** (Erinnerung) in Szene 7, direkt nach der leisen Bridge
- **Finale:** Signal + Stadt erwacht
- **Musik:** Cinematic Post-Rock, ~70 BPM, weibliche ethereale Vocals

---

# Offene Punkte & Nächste Schritte

- [ ] **Gruppenentscheidung:** „Echo im Rost" vs. „Gravity of Wild" (Fabian) → Abgabe 08.11.
- [ ] **Musik:** weibliche ethereale Vocals bestätigen (ACE-Step 1.5)
- [ ] **Drehbuch + Storyboard** aus dem Exposé ableiten
- [ ] **Shotlist** als JSON (gemeinsames Schema)
- [ ] **Master-Posen** generieren (FLUX.1 dev, 5 Poses, IP-Adapter/LoRA)
- [ ] **Pilot-Clips** mit Wan 2.2 (I2V) – Konsistenz testen

**Rechte-Status:** Originalfiktion der Gruppe, frei für das Kursprojekt verwendbar.

---

# Quellen & Dateien im Repo

| Datei | Inhalt |
| --- | --- |
| `expose/echo-im-rost.md` | Endgültiges Exposé (inkl. manueller Korrektur) |
| `prompts/expose_robostadt.txt` | Prompt-Vorlage (Rolle, Kontext, Aufgabe, Format, Einschränkungen) |
| `prompts/expose_kritik.txt` | Kritiker-Prompt |
| `prompts/expose_ueberarbeitung.txt` | Überarbeitungs-Prompt |
| `prompts/kritik_ergebnis.md` | Kritiker-Output (3 Schwächen) |
| `log.md` | Alle Generierungen: Modell, Parameter, Laufzeit, Entscheidungen |

**Modell:** Qwen3.8-27B (Ollama, Q4_K_M), `think=false`, Kontext 262k
**Laufzeiten:** Entwurf T=0,8 · ~93 s · Kritik T=0,7 · ~66 s · Überarbeitung T=0,7 · ~58 s
