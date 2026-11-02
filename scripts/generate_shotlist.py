"""Erzeugt und validiert die Shotlist „Echo im Rost" (LE 3, Übung 3.4).

Aufruf:  python3 scripts/generate_shotlist.py
Output:  shotlist/shotlist_v001.json

Regeln (Folie 20):
- Summe von dauer_s zwischen 180 und 300 Sekunden
- Figurenmerkmale in jedem prompt_bild identisch formuliert
- Validation gegen shotlist/schema.json (jsonschema)
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SCHEMA_PATH = BASE / "shotlist" / "schema.json"
OUT_PATH = BASE / "shotlist" / "shotlist_v001.json"

# Feste Figuren-Merkmale: diese exakten Strings stehen wortgleich in JEDEM
# prompt_bild, in dem die Figur vorkommt (Konsistenz-Check prüft das).
PRIMA = (
    "small round robot with off-white matte shell covered in rust-colored scratches, "
    "one large round amber eye, thin bright red antenna on top of its head, "
    "small worn gray backpack on its back"
)
ECHO = (
    "translucent blue-white holographic robot in identical round shape to Prima, "
    "glowing inner light, red antenna shimmering blue, floating in the air"
)
STYLE = (
    "cinematic anamorphic look, muted earth tones of moss green, rust brown and "
    "slate gray, soft film grain"
)

def p(prima: bool, echo: bool, shot_desc: str) -> str:
    parts = []
    if prima:
        parts.append(PRIMA)
    if echo:
        parts.append(ECHO)
    parts.append(shot_desc)
    parts.append(STYLE)
    return ", ".join(parts)

# (id, szene, songabschnitt, dauer_s, einstellung, kamera, figuren, handlung, prompt_bild)
SHOTS = [
    # Szene 1 – EXT. ÜBERWUCHERTE STRASSE – MORGENGRAU (Intro, 30 s)
    ("s01", 1, "Intro", 5, "Detail", "statisch", ["Prima"],
     "Primas Auge öffnet sich langsam in der Dunkelheit; Staubpartikel tanzen in einem Lichtstrahl.",
     p(True, False, "extreme close-up of the amber round eye slowly opening in darkness, dust particles floating in a beam of light")),
    ("s02", 1, "Intro", 5, "Totale", "statisch", [],
     "Übersicht: die von der Natur zurückeroberte Straße im Morgengrau, Moos und Efeu, rostige Autos, dünner Nebel.",
     p(False, False, "wide establishing shot of an overgrown city street reclaimed by nature in early dawn mist, moss and ivy covering rusty abandoned cars, broken asphalt, soft gray morning light, no characters")),
    ("s03", 1, "Intro", 5, "Halbtotale", "statisch", ["Prima"],
     "Prima steht inmitten der überwucherten Straße; seine rote Antenne pulst schwach rot.",
     p(True, False, "full shot standing alone in the middle of an overgrown street, ivy and moss around, its red antenna pulsing with a faint red light")),
    ("s04", 1, "Intro", 5, "Groß", "statisch", ["Prima"],
     "Gesicht von Prima: Das Auge öffnet sich weiter, ein schwacher roter Lichtpunkt spiegelt sich in der Pupille.",
     p(True, False, "close-up of the face, the amber eye opening wider, a faint red dot of light reflected in the pupil")),
    ("s05", 1, "Intro", 5, "Totale", "statisch", ["Prima"],
     "Prima, klein im Bild, blickt in die Ferne, wo ein schwacher roter Lichtpunkt zwischen den Ruinen aufleuchtet.",
     p(True, False, "wide shot, tiny in frame on an overgrown street, looking toward a faint flickering red light in the far distance between ruined buildings")),
    ("s06", 1, "Intro", 5, "Nah", "statisch", ["Prima"],
     "Prima hebt den Kopf und macht einen Schritt vorwärts.",
     p(True, False, "medium close-up lifting its head and stepping forward on cracked pavement")),

    # Szene 2 – EXT. ÜBERWUCHERTE STRASSE – MORGENGRAU (Strophe 1, 35 s)
    ("s07", 2, "Strophe 1", 6, "Halbtotale", "Fahrt", ["Prima"],
     "Die Kamera fährt langsam seitlich neben Prima her, während er die überwucherte Straße entlangrollt.",
     p(True, False, "side tracking shot rolling slowly along an overgrown wall covered in ivy")),
    ("s08", 2, "Strophe 1", 6, "Detail", "statisch", ["Prima"],
     "Nahaufnahme: Primas kurze, dicke Beine rollen über rissigen Asphalt, Moos wächst zwischen den Fugen.",
     p(True, False, "detail shot of the short thick legs rolling over cracked asphalt with moss growing between the joints")),
    ("s09", 2, "Strophe 1", 6, "Nah", "statisch", ["Prima"],
     "Prima hält an und blickt nach oben.",
     p(True, False, "medium close-up stopping and looking upward")),
    ("s10", 2, "Strophe 1", 6, "Totale", "statisch", [],
     "Auf einem entfernten Dach leuchtet das rote Signal hell auf.",
     p(False, False, "wide shot of a ruined city rooftop in dawn light, a single bright red signal light glowing on the roof, no characters")),
    ("s11", 2, "Strophe 1", 6, "Groß", "statisch", ["Prima"],
     "Primas Auge verengt sich; der rote Lichtpunkt spiegelt sich größer in der Pupille.",
     p(True, False, "close-up of the face, the amber eye narrowing, the red light dot growing larger in the pupil reflection")),
    ("s12", 2, "Strophe 1", 5, "Halbtotale", "statisch", ["Prima"],
     "Prima setzt sich in Bewegung, Richtung Signal.",
     p(True, False, "full shot starting to move forward toward a distant red light")),

    # Szene 3 – INT. U-BAHN-TUNNEL – DUNKEL (Strophe 2, 30 s)
    ("s13", 3, "Strophe 2", 6, "Totale", "statisch", ["Prima"],
     "Dunkler U-Bahn-Tunnel, moosbedeckte Wände; ein Lichtschacht fällt von oben; Prima steht klein in der Mitte.",
     p(True, False, "wide shot of a dark abandoned subway tunnel with mossy walls, a shaft of light from above, tiny in the center of the frame")),
    ("s14", 3, "Strophe 2", 6, "Halbtotale", "statisch", ["Prima"],
     "Frontal: Prima rollt langsam auf die Kamera zu; tief im Tunnel flackert rotes Licht.",
     p(True, False, "frontal shot slowly rolling toward the camera in a dark mossy tunnel, a faint red light flickering deep in the background")),
    ("s15", 3, "Strophe 2", 6, "Detail", "statisch", ["Prima"],
     "Nahaufnahme der Antenne: Das rote Pulsen wird schwächer und flackert.",
     p(True, False, "close-up of the red antenna, its light pulsing weakly and flickering in the dark")),
    ("s16", 3, "Strophe 2", 6, "Nah", "statisch", ["Prima"],
     "Prima hält an und senkt den Kopf; das Auge wird dimmer.",
     p(True, False, "medium close-up stopping, head lowered, the amber eye dimming in the dark")),
    ("s17", 3, "Strophe 2", 6, "Groß", "statisch", ["Prima"],
     "Gesicht im Halbdunkel; ein Wassertropfen fällt von der Decke.",
     p(True, False, "close-up of the face in half-darkness, a single water drop falling from the ceiling")),

    # Szene 4 – INT. U-BAHN-TUNNEL – DUNKEL (Refrain 1, 30 s)
    ("s18", 4, "Refrain 1", 6, "Halbtotale", "statisch", ["Prima"],
     "Frontal: Prima rollt gerade auf die Kamera zu (einfache lineare Bewegung).",
     p(True, False, "frontal shot rolling in a straight line directly toward the camera in a dark mossy tunnel")),
    ("s19", 4, "Refrain 1", 6, "Totale", "statisch", ["Prima"],
     "Seitlich: Prima rollt von links nach rechts durch den Bildausschnitt.",
     p(True, False, "wide side shot rolling from left to right across the frame in a dark mossy tunnel")),
    ("s20", 4, "Refrain 1", 6, "Nah", "statisch", ["Prima"],
     "Rückansicht: Prima rollt in die Tiefe des Tunnels.",
     p(True, False, "rear view shot rolling away into the depth of a dark mossy tunnel")),
    ("s21", 4, "Refrain 1", 6, "Groß", "statisch", ["Prima"],
     "Auge leuchtet heller; roter Lichtpunkt in der Pupille; entschlossen.",
     p(True, False, "close-up of the face, the amber eye glowing brighter, red light dot in the pupil, determined")),
    ("s22", 4, "Refrain 1", 6, "Halbtotale", "statisch", ["Prima"],
     "Frontal: Prima rollt auf die Kamera zu (Wiederholung für schnellen Schnitt im Editor).",
     p(True, False, "frontal shot rolling toward the camera in a dark mossy tunnel, slightly closer framing for a fast cut in editing")),

    # Szene 5 – EXT. PARKLICHTUNG – LEICHTER REGEN (Bridge, 30 s)
    ("s23", 5, "Bridge", 5, "Totale", "statisch", [],
     "Parklichtung im leichten Regen: Moos, alte Bäume, grauer Himmel.",
     p(False, False, "wide shot of an overgrown park clearing in light rain, moss, old trees, gray sky, no characters")),
    ("s24", 5, "Bridge", 5, "Halbtotale", "statisch", ["Prima"],
     "Prima steht mit gesenktem Kopf; die Antenne ist erloschen; Regen fällt.",
     p(True, False, "full shot standing with head lowered in light rain, the red antenna dark and switched off")),
    ("s25", 5, "Bridge", 5, "Groß", "statisch", ["Prima"],
     "Gesicht im Regen; Auge dimm; Tropfen auf der Schale.",
     p(True, False, "close-up of the face in light rain, the amber eye dim, raindrops on the shell")),
    ("s26", 5, "Bridge", 5, "Detail", "statisch", ["Prima"],
     "Regentropfen perlen auf der cremefarbenen Schale; das Auge flackert schwach.",
     p(True, False, "detail shot of raindrops beading on the off-white shell, the amber eye flickering weakly")),
    ("s27", 5, "Bridge", 5, "Detail", "statisch", [],
     "Regentropfen fallen auf moosbedeckte Steine.",
     p(False, False, "detail shot of raindrops falling onto moss-covered stones, no characters")),
    ("s28", 5, "Bridge", 5, "Nah", "statisch", ["Prima"],
     "Prima hebt den Kopf; die Antenne flackert kurz wieder auf.",
     p(True, False, "medium close-up lifting its head in the rain, the red antenna flickering back on briefly")),

    # Szene 6 – EXT. PARKLICHTUNG – REGEN LÄSST NACH (Bridge-Ende, 20 s)
    ("s29", 6, "Bridge", 5, "Detail", "statisch", ["Prima"],
     "Nahaufnahme der Antenne: Sie leuchtet jetzt hellrot und pulst klar.",
     p(True, False, "close-up of the red antenna glowing bright red with a clear steady pulse")),
    ("s30", 6, "Bridge", 5, "Halbtotale", "Fahrt", ["Prima"],
     "Prima läuft durch die Parklichtung; im Hintergrund leuchtet die Glas-Kuppel.",
     p(True, False, "side tracking shot walking through a park clearing, an overgrown glass dome glowing red in the background")),
    ("s31", 6, "Bridge", 5, "Totale", "statisch", [],
     "Die von Pflanzen umwucherte Glas-Kuppel; helles rotes Licht im Inneren.",
     p(False, False, "wide shot of a large glass dome overgrown with plants, bright red light glowing inside, no characters")),
    ("s32", 6, "Bridge", 5, "Nah", "statisch", ["Prima"],
     "Prima steht vor der Kuppel; das rote Licht fällt auf seine Schale.",
     p(True, False, "medium close-up standing in front of the glass dome, red light falling on the shell")),

    # Szene 7 – INT. GLAS-KUPPEL – INNERES LICHT (Refrain 2 / Auflösung, 30 s)
    ("s33", 7, "Refrain 2", 6, "Halbtotale", "statisch", ["Prima"],
     "Innen der Kuppel: Prima blickt auf einen schwebenden hellen Lichtkern; streckt die Hand aus, berührt nichts. (Shot A)",
     p(True, False, "full shot inside the glass dome, looking up at a floating bright white light core in the center, one hand extended but not touching, plants and broken glass around")),
    ("s34", 7, "Refrain 2", 6, "Groß", "statisch", ["Prima"],
     "Extreme Nahaufnahme des Auges; in der Pupille die Form von Echo (Reflexion in Post-Produktion). (Shot B)",
     p(True, False, "extreme close-up of the amber eye, the reflection of a small robot shape visible in the pupil, post-production effect")),
    ("s35", 7, "Refrain 2", 6, "Nah", "statisch", ["Echo"],
     "Nur das Echo-Hologramm allein: schwebt, blau-weiß, pulsiert sanft. (Shot C)",
     p(False, True, "medium close-up of the hologram alone, floating and pulsing softly, no other characters in frame")),
    ("s36", 7, "Refrain 2", 6, "Detail", "statisch", ["Prima"],
     "Primas Hand ist ausgestreckt; helle Lichtpartikel pulsieren um die Hand (Post-Produktion).",
     p(True, False, "detail shot of the extended hand, small bright light particles pulsing around it, post-production effect")),
    ("s37", 7, "Refrain 2", 6, "Groß", "statisch", ["Prima"],
     "Primas Auge glüht warm; die Antenne leuchtet hellrot.",
     p(True, False, "close-up of the face, the amber eye glowing warm, the red antenna bright")),

    # Szene 8 – EXT. GLAS-KUPPEL / STADT – VON NACHT ZU MORGEN (Finaler Refrain + Outro, 35 s)
    ("s38", 8, "Finaler Refrain", 6, "Groß", "statisch", ["Prima"],
     "Antenne auf Maximum: helles rotes Licht; das Gesicht wird von oben beleuchtet.",
     p(True, False, "close-up of the face lit from above by the red antenna glowing at maximum brightness")),
    ("s39", 8, "Finaler Refrain", 6, "Totale", "statisch", [],
     "Kuppel von außen: rotes Licht pulst aus dem Inneren; Pflanzen bewegen sich im Wind.",
     p(False, False, "wide shot of the glass dome from outside, red light pulsing from inside, plants swaying in the wind, no characters")),
    ("s40", 8, "Finaler Refrain", 6, "Totale", "statisch", [],
     "Nächtliche Stadtsilhouette: Lichter erwachen einzeln, wie Sterne.",
     p(False, False, "wide shot of a ruined city skyline at night, individual lights turning on one by one like stars, no characters")),
    ("s41", 8, "Finaler Refrain", 6, "Totale", "statisch", [],
     "Stadt voller Lichter; der Himmel wandelt sich zu Morgendämmerung.",
     p(False, False, "wide shot of the city now full of warm lights, the sky turning to pink dawn, no characters")),
    ("s42", 8, "Finaler Refrain", 6, "Totale", "statisch", ["Prima"],
     "Morgendämmerung: Prima steht auf einem Dach, dahinter die Stadt voller Licht.",
     p(True, False, "wide shot standing on a rooftop in dawn light, the city full of warm lights behind")),
    ("s43", 8, "Outro", 5, "Groß", "statisch", ["Prima"],
     "Nahaufnahme: Primas Auge glüht warm; sanftes Ausblenden.",
     p(True, False, "close-up of the face, the amber eye glowing warm, fading to white")),
]


def build() -> dict:
    return {
        "titel": "Echo im Rost",
        "figuren": [
            {
                "name": "Prima",
                "merkmale": PRIMA,
            },
            {
                "name": "Echo",
                "merkmale": ECHO,
            },
        ],
        "shots": [
            {
                "id": sid,
                "szene": szene,
                "songabschnitt": song,
                "dauer_s": dauer,
                "einstellung": einstellung,
                "kamera": kamera,
                "figuren": figuren,
                "handlung": handlung,
                "prompt_bild": prompt,
            }
            for (sid, szene, song, dauer, einstellung, kamera, figuren, handlung, prompt) in SHOTS
        ],
    }


def validate(shotlist: dict) -> None:
    import jsonschema

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    jsonschema.validate(instance=shotlist, schema=schema)

    total = sum(s["dauer_s"] for s in shotlist["shots"])
    assert 180 <= total <= 300, f"Summe dauer_s = {total} (muss zwischen 180 und 300 liegen)"

    for s in shotlist["shots"]:
        for fig in s["figuren"]:
            merkmale = next(f["merkmale"] for f in shotlist["figuren"] if f["name"] == fig)
            assert merkmale in s["prompt_bild"], f"{s['id']}: Merkmale von {fig} fehlen im prompt_bild"

    per_scene: dict[int, int] = {}
    for s in shotlist["shots"]:
        per_scene[s["szene"]] = per_scene.get(s["szene"], 0) + 1
    for szene, n in per_scene.items():
        assert 3 <= n <= 6, f"Szene {szene}: {n} Shots (muss 3–6 sein)"

    print(f"OK: Schema-Validation bestanden")
    print(f"OK: Summe dauer_s = {total:.0f} s (180–300)")
    print(f"OK: Figurenmerkmale identisch in jedem prompt_bild")
    print(f"OK: Shots pro Szene = {per_scene} (je 3–6)")
    print(f"OK: {len(shotlist['shots'])} Shots gesamt")


def main() -> None:
    shotlist = build()
    validate(shotlist)
    OUT_PATH.write_text(json.dumps(shotlist, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Geschrieben: {OUT_PATH.relative_to(BASE)}")


if __name__ == "__main__":
    main()
