Als strenger Regisseur und Produktionsleiter sage ich dir: Dieser Entwurf ist emotional anrührend, aber technisch für dein lokales Stack-Setup (FLUX/Wan 2.2) ein Desaster. Du verwechselst "cinematisch" mit "umsetzbar". Hier sind deine drei tödlichen Schwächen, sortiert nach der Dringlichkeit der Korrektur.

### 1. Die Hologramm-Interaktion im Finale (Akt 3, Szene 7)

**(a) Was genau falsch ist:**
Du planst, dass Prima und das Echo-Hologramm sich "Auge auf Auge" stellen und Prima die Luft berührt. Du schreibst zwar, dass du das Hologramm post-produzierst, aber die *Bewegung* und der *Blickkontakt* sind Teil des Video-Clips. Wan 2.2 kann keine transparente, physisch nicht vorhandene Figur (Echo) mit einer festen Figur (Prima) in einem einzigen Shot konsistent rendern, insbesondere wenn es um räumliche Tiefe und Lichtwechsel (das Hologramm leuchtet Prima an) geht. Selbst wenn du das Hologramm in Resolve einblendest, wird das Licht von Echo auf Prima im generierten Video nicht korrekt berechnet sein, da das Videomodell die Quelle des Lichts nicht "weiß".

**(b) Warum es die Bewertung kostet:**
Verstoß gegen Kriterium 2 (einfache Bewegung, keine komplexen Interaktionen) und Kriterium 3 (Konsistenz). Wenn du zwei Objekte in einem Frame hast, eines fest und eines "virtuell", bricht die physikalische Logik zusammen. Das Licht wird falsch fallen, Schatten werden fehlen oder sich widersprüchlich verhalten, und die "Berührung der Luft" wird als Artefakt oder statisches Bild wirken, nicht als emotionale Geste. Das zerstört den emotionalen Höhepunkt (Bridge/Finale), weil es technisch billig aussieht.

**(c) Konkrete Lösung:**
Entferne die direkte Interaktion im selben Frame.
*   **Shot A:** Prima steht in der Kuppel, blickt in die Mitte, wo ein helles, weißes Lichtkern (kein Hologramm, nur ein Lichtpunkt) schwebt. Prima streckt die Hand aus, aber berührt nichts. Das Licht pulsiert *um* seine Hand herum (post-produziert als Partikeleffekt).
*   **Shot B (Insert):** Nahaufnahme von Primas Auge, das reflektiert (im Post-Produktion einblenden) die Form von Echo.
*   **Shot C (Cutaway):** Nur das Hologramm von Echo (einzeln generiert, statisch oder schwebend, ohne Prima im Bild), das pulsiert.
*   **Montage:** Schneide A und C schnell abwechselnd. Das suggeriert Interaktion durch Schnitt, nicht durch Rendering. Das ist sicher, konsistent und emotional stärker, weil der Zuschauer die Verbindung selbst im Kopf schließt.

### 2. Der "Schnelle, dynamische Schnitt" im Tunnel (Akt 2, Szene 4)

**(a) Was genau falsch ist:**
Du beschreibst "Schnelle, dynamische Schnitte" und "Kamera folgt ihm aus der Frontansicht, leicht wackelnd für Dynamik". Das ist ein Widerspruch in sich für Wan 2.2. "Wackelnd" (Handheld-Kamera-Effect) ist einer der schwersten Effekte für aktuelle lokale Videomodelle zu simulieren, da sie keine echte physikalische Kamera-Simulation haben, sondern nur Interpolation. Wenn du dazu noch "schnelle Schnitte" willst, brauchst du viele kurze Clips. Aber du hast nur 30–60 Clips für das ganze Video. Wenn du 10 Clips nur für den Refrain-Tunnel verbrauchst, hast du keine Clips mehr für die Story-Aufbau-Phasen. Zudem neigt Wan 2.2 bei schnellen Bewegungen durch komplexe Texturen (Moos, Rost) zu "Morphing" der Umgebung, was bei Nahaufnahmen sofort auffällt.

**(b) Warum es die Bewertung kostet:**
Verstoß gegen Kriterium 2 (Umsetzbarkeit mit lokalen Modellen). "Wackelkamera" ist kein simples Motion-Burst, sondern erfordert eine simulierte Schwerkraft und Unschärfe, die Wan 2.2 oft als Verformung der Objekte (z.B. der Antenne oder des Rucksacks) darstellt. Das führt zu visuellem Rauschen und bricht die Immersion. Zudem frisst es dein Clip-Budget für den Rest des Songs, wodurch der Spannungsbogen flach wirkt.

**(c) Konkrete Lösung:**
Ersetze "Wackelkamera" durch **Statische Positionen mit Perspektivwechsel**.
*   Generiere 3–4 statische oder sehr langsam drehende Shots von Prima im Tunnel:
    1.  Frontal: Prima rollt direkt auf die Kamera zu (einfache lineare Bewegung).
    2.  Seitlich: Prima rollt von links nach rechts durch den Bildausschnitt (einfache lineare Bewegung).
    3.  Hinter der Kamera: Wir sehen Prima von hinten, wie er in die Tiefe des Tunnels verschwindet.
*   Diese Shots sind technisch trivial für Wan 2.2 (ein Objekt, einfache Bewegung, statischer Hintergrund).
*   Erreiche die Dynamik durch **Schnitttempo** im Editor, nicht durch Kamerabewegung im Modell. Schnelle Schnitte zwischen diesen drei stabilen Shots erzeugen mehr Energie als eine schlechte, wackelige Follow-Kamera.

### 3. Die Figuren-Konsistenz über 30–60 Clips (Globales Problem)

**(a) Was genau falsch ist:**
Du schreibst: "In den Text-Prompts für das Video die Figur *nicht* neu beschreiben, sondern sich ausschließlich auf die Bewegung beziehen." Das ist technisch falsch. Wan 2.2 (und die meisten Diffusionsmodelle) haben **keinen Gedächtnis-Kontext** über Clips hinweg. Wenn du nur Bewegung beschreibst, aber keine visuelle Referenz im Prompt oder via Image-to-Video (I2V) streng verankerst, wird das Modell bei jedem neuen Clip die Figur neu interpretieren. "Nicht neu beschreiben" führt dazu, dass das Modell auf seine eigenen, variierenden Defaults zurückgreift. Die Antenne wird mal rot, mal orangefarben sein. Das Auge wird mal groß, mal klein. Der Rucksack wird mal links, mal rechts hängen.

**(b) Warum es die Bewertung kostet:**
Verstoß gegen Kriterium 3 (Figurenkonsistenz). Das ist der härteste Test. Wenn dein Protagonist in Clip 10 anders aussieht als in Clip 15, ist das Video sofort als "KI-Gebastel" erkennbar. Der Zuschauer verliert die emotionale Bindung an "Prima". Ein strenger Regisseur schneidet solche Clips sofort, weil sie das visuelle Narrativ zerfressen. Du hast kein Budget für 30 Versuche pro Clip, um eine konsistente Figur zu finden.

**(c) Konkrete Lösung:**
Du musst **Image-to-Video (I2V)** als Standard-Workflow für *jeden* Clip nutzen, nicht nur für die Referenz.
1.  Erstelle in FLUX.1 dev **ein** perfektes Master-Bild von Prima in der Ziel-Pose der jeweiligen Szene (z.B. "Prima steht im Tunnel, Blick nach vorne").
2.  Nutze dieses Bild als **Startframe** für Wan 2.2.
3.  Der Prompt für Wan 2.2 muss dann nur die *Bewegung* enthalten: "The robot rolls forward slowly, camera static."
4.  **Wichtig:** Du darfst in Wan 2.2 *keine* textuelle Beschreibung der Figur hinzufügen, da das Bild die visuelle Wahrheit liefert. Aber du musst sicherstellen, dass das Startbild (FLUX) in *jeder* Szene exakt dieselben Details hat. Das bedeutet: Du musst in FLUX nicht nur "Prima" prompten, sondern mit **IP-Adapter** oder **LoRA** (wie du es richtig erkannt hast) die Identität erzwingen.
5.  **Praktischer Tipp:** Generiere 5 verschiedene "Master-Posen" von Prima in FLUX (stehend, rollend, kopf gesenkt, Hand ausgestreckt, Auge offen). Nutze nur diese 5 Bilder als Basis für alle 30–60 Clips. Das begrenzt deine Variation, aber garantiert Konsistenz. Alles andere ist zu riskant.

**Fazit:** Dein Entwurf ist zu ambitioniert für die aktuelle lokale Hardware. Reduziere die Interaktionen, ersetze komplexe Kamerabewegungen durch statische Schnitte und zwinge die Konsistenz durch strenge I2V-Pipelines mit wenigen Master-Images. Dann wird es funktionieren.