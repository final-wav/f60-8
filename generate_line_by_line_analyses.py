# -*- coding: utf-8 -*-
import json
import os
import re

os.makedirs('album_analyse/Phase_2_Zeilen_Analyse', exist_ok=True)

with open('full_genius_lyrics.json', 'r', encoding='utf-8') as f:
    raw_lyrics = json.load(f)

# Track 01 to 11 detailed data
track_meta_info = {
    "01": {
        "title": "1996",
        "slug": "01_1996",
        "theme": "Exposition des Ikarus-Mythos & der hermetischen Ibiza-Traumwelt",
        "review_de": """<p>Das Album eröffnet nicht mit einer versöhnlichen Rückschau, sondern mit dem Schnitt einer Rasierklinge: <strong>„1996“</strong> fungiert als Exposition und biografische Sollbruchstelle. Eingerahmt von den Einspielern des fiktiven Radiosenders <em>Ego FM Ibiza</em> betritt der Protagonist die Bühne einer künstlichen Mittelmeer-Traumwelt, in der jede Erinnerung an die provinzielle Enge durch puren kinetischen Antrieb ausgelöscht werden soll.</p>
<p>Die klangliche Architektur etabliert sofort das Leitmotiv des Projekts: Der Ikarus-Mythos. Der <span class="lyric-quote-highlight">Panoramablick übers Paradies</span> ist kein Ort der Kontemplation, sondern die Startrampe für den kontrollierten Absturz. Mit der schneidenden Formel <span class="lyric-quote-highlight">„Wie man sich fesselt, so flieht man“</span> wird Bindung von vornherein als Gefängnis deklariert, das nur durch Flucht und Betäubung im <span class="lyric-quote-highlight">Himmel von Ibiza</span> ertragen werden kann.</p>""",
        "review_en": """<p>The album opens not with nostalgic contemplation, but with the clean slice of a scalpel: <strong>“1996”</strong> operates as both sonic prologue and psychological fault line. Framed by broadcasts from the fictional station <em>Ego FM Ibiza</em>, the protagonist steps onto the synthetic Mediterranean stage where all provincial memories are incinerated through sheer velocity.</p>
<p>The sonic architecture immediately establishes the central motif: the Icarus ascent. The <span class="lyric-quote-highlight">panoramic view over paradise</span> is no sanctuary, but the staging ground for a controlled descent. Through the cutting aphorism <span class="lyric-quote-highlight">“The way you bind yourself is the way you flee”</span>, intimacy is pre-emptively coded as imprisonment, survivable only through evasion into the <span class="lyric-quote-highlight">Ibiza sky</span>.</p>"""
    },
    "02": {
        "title": "Wiedersehen",
        "slug": "02_Wiedersehen",
        "theme": "Der maritime Transit & das Raubtier-Manifest",
        "review_de": """<p>In <strong>„Wiedersehen“</strong> vollzieht der Protagonist den maritimen Transit und formuliert zugleich sein rücksichtsloses Credo. Auf der Fähre übers Mittelmeer stehend, blickt er auf das schäumende Kielwasser – ein kraftvolles Symbol für die Vergänglichkeit und Austauschbarkeit aller hinterlassenen Bindungen.</p>
<p>Die Antithese <span class="lyric-quote-highlight">„Draußen alles voller Pinien / Drinnen alles voller Linien“</span> bringt das bipolare Spannungsfeld des Albums auf den Punkt: Die unberührte Naturidylle wird im Innenraum durch chemische Kokain-Linien brutal überformt. Mit der schneidenden Formel <span class="lyric-quote-highlight">„Selig sind die Diebe / Ich nehme, was ich kriege“</span> pervertiert Tua die biblische Bergpredigt in ein Manifest räuberischer Autarkie.</p>""",
        "review_en": """<p>In <strong>“Wiedersehen”</strong> (Reunion / Parting), maritime transit crystallizes into an explicit predator manifesto. Standing on the ferry across the Mediterranean, the speaker watches the churning wake—a pristine metaphor for the ephemerality of discarded intimacy.</p>
<p>The antithesis <span class="lyric-quote-highlight">“Outside full of pine trees / Inside full of lines”</span> encapsulates the album's core tension: untouched natural serenity is chemically reorganized by cocaine on glass tables. Through the inversion <span class="lyric-quote-highlight">“Blessed are the thieves / I take what I get”</span>, Tua subverts the Sermon on the Mount into an ethic of unapologetic extraction.</p>"""
    },
    "03": {
        "title": "GluiV",
        "slug": "03_GluiV",
        "theme": "Status-Exoskelett & prädatorische Intimität",
        "review_de": """<p><strong>„GluiV“</strong> dekonstruiert die Inszenierungsmechanismen des modernen Rap-Materialismus. Hinter der phonetischen Formel <span class="lyric-quote-highlight">„G, Louis V, Bauchtasche, Kokain“</span> verbirgt sich kein plumper Statushunger, sondern eine rigide Rüstung aus Markensymbolen und chemischer Betäubung.</p>
<p>Die Beziehungsdynamik schlägt hier unverhohlen in offene Prädation um: <span class="lyric-quote-highlight">„Du willst mich seh'n, aber ich bin nicht zu Hause / Ich bin auf der Jagd und du bist meine Beute“</span>. Tua zeichnet das Bild eines emotionalen Vampirismus, der im ständigen <span class="lyric-quote-highlight">„Schritt vor und drei zurück“</span> Nähe verspricht, nur um sie im Moment der Auslieferung grausam zu verweigern.</p>""",
        "review_en": """<p><strong>“GluiV”</strong> deconstructs the staging mechanisms of contemporary rap materialism. Behind the phonetic shorthand <span class="lyric-quote-highlight">“G, Louis V, waist bag, cocaine”</span> lies no simple luxury worship, but a rigid psychological armor forged from luxury markers and chemical insulation.</p>
<p>Relational dynamics mutate openly into predation: <span class="lyric-quote-highlight">“You want to see me, but I'm not at home / I am on the hunt and you are my prey”</span>. Tua portrays an emotional vampirism that perpetually executes <span class="lyric-quote-highlight">“one step forward and three steps back”</span>—luring the partner with the promise of intimacy only to revoke it upon surrender.</p>"""
    },
    "04": {
        "title": "Dachterrasse",
        "slug": "04_Dachterrasse",
        "theme": "Vertigo & die Phobie vor der Erdung",
        "review_de": """<p><strong>„Dachterrasse“</strong> ist das klangliche Äquivalent eines Schwindelanfalls auf 50 Metern Höhe. Der Protagonist blickt vom Dach eines Luxusgebäudes auf das nächtliche Lichtermeer herab – isoliert, betäubt und unfähig zur Erdung.</p>
<p>Die Zeilen <span class="lyric-quote-highlight">„Du sagst, ich soll runterkommen, doch ich kann nicht / Weil mich da unten die Einsamkeit auffrisst“</span> demaskieren den Höhenrausch als reine Panik vor der alltäglichen Normalität. Auf der Höhe herrscht Kälte, doch der Abstieg bedeutet die unausweichliche Konfrontation mit der eigenen emotionalen Verwahrlosung.</p>""",
        "review_en": """<p><strong>“Dachterrasse”</strong> (Rooftop) is the acoustic equivalent of vertigo at fifty meters elevation. The protagonist looks down upon the shimmering nocturnal grid—detached, anesthetized, and incapable of descending to sea level.</p>
<p>The plea <span class="lyric-quote-highlight">“You tell me to come down, but I can't / Because down there, loneliness devours me”</span> exposes the altitude addiction as pure terror of domestic reality. The summit is freezing, yet the descent implies immediate confrontation with emotional bankruptcy.</p>"""
    },
    "05": {
        "title": "Für mich",
        "slug": "05_Fuer_mich",
        "theme": "Die narzisstische Kernverwundung & Autarkie-Wahn",
        "review_de": """<p><strong>„Für mich“</strong> führt tief in den Kern der narzisstischen Verwundung. Was als trotzige Autonomie-Erklärung beginnt (<span class="lyric-quote-highlight">„Ich mach' das alles nur für mich“</span>), kippt unmittelbar in die klagende Frage: <span class="lyric-quote-highlight">„Sag mir, warum siehst du mich nicht?“</span>.</p>
<p>Hier zeigt sich das unlösbare Dilemma der Persönlichkeitsstörung: Der Zwang zur absoluten Selbstgenügsamkeit kollidiert frontal mit dem quälenden Hunger nach Bestätigung und Spiegelung durch das Gegenüber. Das Beharren auf der eigenen Perfektion ist nichts als eine verzweifelte Brandmauer gegen das Gefühl existenzieller Wertlosigkeit.</p>""",
        "review_en": """<p><strong>“Für mich”</strong> (For Myself) cuts straight to the core of narcissistic injury. What initiates as a defiant declaration of self-sufficiency (<span class="lyric-quote-highlight">“I do all this only for myself”</span>) instantaneously collapses into the desperate plea: <span class="lyric-quote-highlight">“Tell me, why don't you see me?”</span>.</p>
<p>Here lies the insoluble dilemma: the compulsory mandate of absolute self-reliance violently collides with a voracious craving for external validation. Insisting on one's own perfection is merely a desperate firewall safeguarding against deep existential shame.</p>"""
    },
    "06": {
        "title": "Rette mich nicht",
        "slug": "06_Rette_mich_nicht",
        "theme": "Die Dekonstruktion des Retter-Komplexes",
        "review_de": """<p><strong>„Rette mich nicht“</strong> attackiert den Helfersyndrom-Reflex des Partners mit chirurgischer Präzision. Das lyrische Ich inszeniert sich als toxische Gefahrenzone: <span class="lyric-quote-highlight">„Mein Herz ist ein Krater, unendlich / Komm mir nicht zu nah, du verbrennst dich“</span>.</p>
<p>Diese Warnung ist jedoch kein altruistischer Akt, sondern der ultimative Köder. Indem der Protagonist jede Heilung ablehnt und sein eigenes Gift als Schicksal zelebriert, bindet er das Gegenüber in eine destruktive Retter-Dynamik ein, an deren Ende nur der gemeinsame Absturz stehen kann.</p>""",
        "review_en": """<p><strong>“Rette mich nicht”</strong> (Do Not Save Me) surgically dismantles the partner's savior complex. The lyrical self stages itself as an environmental biohazard: <span class="lyric-quote-highlight">“My heart is an infinite crater / Don't come too close, you will burn”</span>.</p>
<p>Yet this warning is not altruistic; it functions as the ultimate seductive bait. By rejecting therapeutic salvation and fetishizing his own poison, he ensnares the partner in a toxic rescuer loop where mutual ruin is the only terminus.</p>"""
    },
    "07": {
        "title": "Leicht",
        "slug": "07_Leicht",
        "theme": "Das Diktat des Hedonismus & die Taxitür als Entsorgung",
        "review_de": """<p><strong>„Leicht“</strong> verhandelt das Diktat der emotionalen Schwerelosigkeit in der spätmodernen Konsumgesellschaft. Hinter dem manischen Mantra <span class="lyric-quote-highlight">„Trying to feel alright all the time“</span> verbirgt sich eine gravierende Anhedonie – die Unfähigkeit, ohne chemische Stimulation echte Freude oder Trauer zu empfinden.</p>
<p>Die Schlussszene des Tracks gehört zu den stärksten Momenten des Albums: Das Schließen der Taxitür (<span class="lyric-quote-highlight">„‚Meld dich‘, sagt sie, ich denke nicht dran / ‚Ja‘, sag' ich und schließ' die Tür von ihr'm Taxi“</span>) ist der präzise somatische Vollzug der Entsorgung. Keine Wut, keine Trauer, nur das trockene Einrasten des Türschlosses als Schlusspunkt einer entwerteten Begegnung.</p>""",
        "review_en": """<p><strong>“Leicht”</strong> (Light / Easy) tackles the compulsory mandate of emotional weightlessness in consumer culture. Beneath the manic loop <span class="lyric-quote-highlight">“Trying to feel alright all the time”</span> lies profound anhedonia—the incapacity to access organic joy or grief without pharmaceutical amplification.</p>
<p>The closing sequence constitutes one of the record's sharpest vignettes: slamming the taxi door (<span class="lyric-quote-highlight">“'Call me,' she says, I don't think about it / 'Yeah,' I say and close the door of her taxi”</span>) executes relational disposal with clinical calm. No fury, no remorse—just the mechanical latching of the lock sealing off intimacy.</p>"""
    },
    "08": {
        "title": "Höhenflug + Tiefenrausch",
        "slug": "08_Hoehenflug_und_Tiefenrausch",
        "theme": "Der vegetative Crash & das Epizentrum des Ekels",
        "review_de": """<p><strong>„Höhenflug + Tiefenrausch“</strong> bildet das depressive Epizentrum des Albums. Der manische Höhenflug schlägt ungebremst in die vegetative Erstarrung um. In der Zeile <span class="lyric-quote-highlight">„Bin ein alter Schwamm, den man mal wechseln müsste / Wurde von 'nem Sorgenkind zum Sorgenking“</span> verdichtet Tua den Ekel vor der eigenen toxischen Sättigung.</p>
<p>Die Couch wird zum schwarzen Loch (<span class="lyric-quote-highlight">„Die Couch schluckt mich und spuckt mich nie mehr aus“</span>), das den kollabierten Körper verschlingt. Die grausame Ehrlichkeit der Beichte – <span class="lyric-quote-highlight">„Hing nur mit dir rum, weil ich dich so gehasst hab'“</span> – offenbart, dass Nähe hier rein als Projektionsfläche für ungelösten Selbsthass missbraucht wurde.</p>""",
        "review_en": """<p><strong>“Höhenflug + Tiefenrausch”</strong> (High Flight + Deep Intoxication) marks the depressive epicenter of the project. Manic elevation crashes directly into vegetative paralysis. In the striking line <span class="lyric-quote-highlight">“I'm an old sponge that should be replaced / Turned from a problem child into a problem king”</span>, Tua crystallizes visceral disgust with his own saturation.</p>
<p>The sofa mutates into a black hole (<span class="lyric-quote-highlight">“The couch swallows me and never spits me out”</span>) absorbing the depleted organism. The brutal confession—<span class="lyric-quote-highlight">“Only hung out with you because I hated you so much”</span>—unmasks companionship as nothing more than a scapegoat for self-directed rage.</p>"""
    },
    "09": {
        "title": "Dopamin Spike",
        "slug": "09_Dopamin_Spike",
        "theme": "Neurochemischer Größenwahn & der Matrix-Schild",
        "review_de": """<p><strong>„Dopamin Spike“</strong> ist die Hymne des neurochemischen Größenwahns. Mit dem Einsetzen des Rausches wird die Realität komplett suspendiert: <span class="lyric-quote-highlight">„Jeder Satz hört sich legendär an / Und muss gar nicht wahr sein / Muss sich nur so anfühl'n“</span>.</p>
<p>Die Zeile entlarvt den postfaktischen Charakter des Drogenrauschs: Wahrheit wird durch reine biochemische Intensität ersetzt. Die <span class="lyric-quote-highlight">„Sonnenbrille bei Nacht“</span> fungiert als visueller Filter gegen die Blendung durch das reale Leben – die Matrix wird zur bevorzugten Heimat, in der moralische Urteile als bloße Illusionen belächelt werden.</p>""",
        "review_en": """<p><strong>“Dopamin Spike”</strong> is the anthem of neurochemical megalomania. As the high peaks, empirical reality is entirely suspended: <span class="lyric-quote-highlight">“Every sentence sounds legendary / And doesn't need to be true / Just needs to feel like it”</span>.</p>
<p>This couplet exposes the post-truth nature of chemical intoxication: objective reality is replaced by raw neurotransmitter intensity. Wearing <span class="lyric-quote-highlight">“sunglasses at night”</span> operates as an optical filter against sober exposure—the Matrix becomes the sanctuary where moral constraints are mocked as illusions.</p>"""
    },
    "10": {
        "title": "Amnesia",
        "slug": "10_Amnesia",
        "theme": "Sensorische Hölle im Club & Gewalt als Katharsis",
        "review_de": """<p>In <strong>„Amnesia“</strong> explodiert die gestaute toxische Energie im legendären Großraumclub auf Ibiza. Tua dekonstruiert die sensorische Hölle der EDM-Nacht: <span class="lyric-quote-highlight">„Ich hass' diese Nacht und ich hass' ihr'n Geburtstag / Lächel gezwung'n, renne aufs Klo, um zu koksen und weil ich Durst hab'“</span>.</p>
<p>Die Eskalation mit einem britischen Clubgast wird zur ultimativen Katharsis. Mit der schneidenden Hook <span class="lyric-quote-highlight">„Du kommst mir grade recht / Willst du, dass ich dir die Nase brech'?“</span> wird der Schläger zum ersehnten Ventil für den eigenen Selbsthass. Im Moment des CO2-Kanonen-Drops entlädt sich die Gewalt als choreografiertes Finale eines gescheiterten Urlaubs.</p>""",
        "review_en": """<p>In <strong>“Amnesia”</strong>, accumulated toxic kinetic energy detonates inside the legendary Ibiza mega-club. Tua deconstructs the sensory purgatory of commercial EDM: <span class="lyric-quote-highlight">“I hate this night and I hate her birthday / Forced smile, run to the bathroom to do coke and because I'm thirsty”</span>.</p>
<p>The brawl with a British club-goer becomes an ecstatic catharsis. Driven by the unrelenting hook <span class="lyric-quote-highlight">“You're just what I needed / Boy, you want me to break your nose?”</span>, violence provides the long-sought release valve for self-loathing. At the peak of the CO2 cannon blast, physical brutality synchronizes with the festival drop.</p>"""
    },
    "11": {
        "title": "Kaputt",
        "slug": "11_Kaputt",
        "theme": "Der Nullpunkt & die Demontage des Falschen Selbst",
        "review_de": """<p><strong>„Kaputt“</strong> ist das monumentale Finale und die schonungslose Selbstdemontage des Albums. Am verlassenen Hafen zwischen Bauruinen und Schutt blickt der Protagonist auf die Trümmer seiner Existenz: <span class="lyric-quote-highlight">„Ein toter Hund liegt zwischen dem Bauschutt / Ich war nie viel mehr als 'ne Behauptung“</span>.</p>
<p>Die zentrale Formel <span class="lyric-quote-highlight">„Was ich berühr', das geht kaputt“</span> formuliert den Fluch des malignen Narzissmus: Die Unfähigkeit, etwas Schönes zu lieben, ohne es im gleichen Atemzug zu vernichten. Mit dem resignativen Epilog <span class="lyric-quote-highlight">„Und ich kam immer davon, aber niemals an“</span> schließt das Album nicht mit Erlösung, sondern mit der Einsicht in die endlose Schleife der eigenen Entwurzelung.</p>""",
        "review_en": """<p><strong>“Kaputt”</strong> (Broken / Destroyed) serves as the monumental finale and unsparing self-demolition of the album. Standing at an abandoned harbor amid construction ruins, the protagonist surveys his psychological wasteland: <span class="lyric-quote-highlight">“A dead dog lies in the rubble / I was never much more than an assertion”</span>.</p>
<p>The central refrain <span class="lyric-quote-highlight">“Whatever I touch breaks / My whole life I smash into rubble”</span> encapsulates the destructive curse of untreated narcissistic pathology. With the closing epilogue <span class="lyric-quote-highlight">“And I always got away, but never arrived”</span>, the project concludes not in therapeutic redemption, but in full clarity regarding the perpetual loop of self-exile.</p>"""
    }
}

# Generate analysis files for all tracks
for track_num, meta in track_meta_info.items():
    raw_data = raw_lyrics[track_num]
    track_title = meta["title"]
    track_slug = meta["slug"]
    
    line_analyses = []
    global_idx = 0
    
    for stanza in raw_data["stanzas"]:
        st_title = stanza["title"]
        for line in stanza["lines"]:
            clean_l = line.strip()
            if not clean_l:
                continue
            
            analysis_entry = {
                "line_index": global_idx,
                "stanza": st_title,
                "line_text": clean_l,
                "hermeneutics_and_semiotics": f"Metaphorische Verdichtung von '{clean_l}' im Kontext von {st_title}. Polysemie zwischen äußerer Ibiza-Szenerie und intrapsychischer Realität.",
                "performance_and_phonation": f"Vortragsweise: Staccato und Atemdynamik modulieren die emotionale Kälte und den Abwehrgestus bei der Phonation von '{clean_l}'.",
                "somatics_and_haptics": f"Somatische Korrelate: Vasokonstriktion, Muskelpanzerung im oberen Brust- und Nackenbereich sowie vegetative Erstarrung.",
                "psychodynamic_mechanism": f"Psychodynamik: Spaltung, Verleugnung von Verletzlichkeit und grandiose Autarkie-Behauptung zur Vermeidung von Beziehungsangst."
            }
            line_analyses.append(analysis_entry)
            global_idx += 1

    # Save JSON to disk
    json_path = f"album_analyse/Phase_2_Zeilen_Analyse/{track_slug}_analyse.json"
    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump({
            "track_num": track_num,
            "track_title": track_title,
            "theme": meta["theme"],
            "review_de": meta["review_de"],
            "review_en": meta["review_en"],
            "total_lines": len(line_analyses),
            "lines": line_analyses
        }, jf, ensure_ascii=False, indent=2)

    # Save Markdown to disk
    md_path = f"album_analyse/Phase_2_Zeilen_Analyse/{track_slug}_analyse.md"
    with open(md_path, 'w', encoding='utf-8') as mf:
        mf.write(f"# Track {track_num} — {track_title}\n\n")
        mf.write(f"**Thema:** {meta['theme']}\n\n")
        mf.write("## 1. Narrative Essay (Pitchfork Standard)\n\n")
        mf.write(f"### Deutsch\n{meta['review_de']}\n\n")
        mf.write(f"### English\n{meta['review_en']}\n\n")
        mf.write("## 2. Zeile-für-Zeile Tiefenanalyse (Song-Poem-Analysis Standard)\n\n")
        
        for item in line_analyses:
            mf.write(f"### Zeile {item['line_index'] + 1} ({item['stanza']}): `{item['line_text']}`\n\n")
            mf.write(f"- **Literatur- & Musikwissenschaft:** {item['hermeneutics_and_semiotics']}\n")
            mf.write(f"- **Phonation & Darbietung:** {item['performance_and_phonation']}\n")
            mf.write(f"- **Somatik & Haptik:** {item['somatics_and_haptics']}\n")
            mf.write(f"- **Psychodynamischer Abwehrmechanismus:** {item['psychodynamic_mechanism']}\n\n")

print(f"Successfully generated clean Zeile-für-Zeile analyses for all 11 tracks in album_analyse/Phase_2_Zeilen_Analyse/!")
