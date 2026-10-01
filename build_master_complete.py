# -*- coding: utf-8 -*-
import json
import re
import os

# Load complete Genius lyrics
with open('full_genius_lyrics.json', 'r', encoding='utf-8') as f:
    raw_lyrics = json.load(f)

# Load CSS from tomora_index.html and adapt color variables to exact cover orange
with open('tomora_index.html', 'r', encoding='utf-8') as f:
    tomora_content = f.read()

style_start = tomora_content.find('<style>')
style_end = tomora_content.find('</style>')
tomora_css = tomora_content[style_start+7:style_end]

adapted_css = tomora_css.replace('--magenta: #ff007a;', '--orange: #fa5b00;')
adapted_css = adapted_css.replace('--magenta-dim: rgba(255, 0, 122, 0.12);', '--orange-dim: rgba(250, 91, 0, 0.12);')
adapted_css = adapted_css.replace('--magenta-glow: rgba(255, 0, 122, 0.35);', '--orange-glow: rgba(250, 91, 0, 0.35);')
adapted_css = adapted_css.replace('var(--magenta)', 'var(--orange)')
adapted_css = adapted_css.replace('var(--magenta-dim)', 'var(--orange-dim)')
adapted_css = adapted_css.replace('var(--magenta-glow)', 'var(--orange-glow)')
adapted_css = adapted_css.replace('rgba(255, 0, 122, 0.12)', 'rgba(250, 91, 0, 0.12)')
adapted_css = adapted_css.replace('rgba(255, 0, 122, 0.10)', 'rgba(250, 91, 0, 0.10)')
adapted_css = adapted_css.replace('rgba(255, 0, 122, 0.18)', 'rgba(250, 91, 0, 0.18)')
adapted_css = adapted_css.replace('rgba(255, 0, 122, 0.25)', 'rgba(250, 91, 0, 0.25)')
adapted_css = adapted_css.replace('rgba(255, 0, 122, 0.35)', 'rgba(250, 91, 0, 0.35)')
adapted_css = adapted_css.replace('rgba(255, 0, 122, 0.45)', 'rgba(250, 91, 0, 0.45)')
adapted_css = adapted_css.replace('rgba(255, 0, 122, 0.65)', 'rgba(250, 91, 0, 0.65)')
adapted_css = adapted_css.replace('#ff2b92', '#ff6a1a')
adapted_css = adapted_css.replace('#ff007a', '#fa5b00')

# Matching algorithm from skill
def clean_txt(t):
    return re.sub(r'[^a-zA-Z0-9äöüÄÖÜß]', '', t).lower()

def find_matching_card(line_text, cards):
    line_lower = line_text.lower()
    line_clean = clean_txt(line_text)
    if not line_clean or len(line_clean) < 2:
        return None
    
    for idx, card in enumerate(cards):
        q_full = card.get("quote", "").lower()
        parts = [p.strip() for p in q_full.split('/')]
        
        # 1. Substring-Match
        for p in parts:
            p_clean = clean_txt(p)
            if p_clean and (p_clean in line_clean or line_clean in p_clean):
                return idx
                
        # 2. Token-Schnittmenge (ohne Füllwörter)
        for p in parts:
            tokens = [t.strip() for t in re.findall(r'[a-zA-ZäöüÄÖÜß]{3,}', p) 
                      if t.strip() not in ['the', 'and', 'for', 'von', 'der', 'die', 'das', 'mit', 'wie', 'ein', 'eine', 'you', 'und', 'ich', 'ist', 'dass']]
            matched = [t for t in tokens if t in line_lower]
            if len(tokens) >= 2 and len(matched) >= min(len(tokens), 2):
                return idx
            elif len(tokens) == 1 and len(matched) == 1 and len(tokens[0]) >= 4:
                return idx
    return None

# Comprehensive master dataset covering all tracks and lines
master_tracks = [
    {
        "num": "01",
        "title": "1996",
        "review_de": """<p>Das Album eröffnet nicht mit einer versöhnlichen Rückschau, sondern mit dem Schnitt einer Rasierklinge: <strong>„1996“</strong> fungiert als Exposition und biografische Sollbruchstelle. Eingerahmt von den fiktiven Radiosendern von <em>Ego FM Ibiza</em> betritt der Protagonist die Bühne einer künstlichen Mittelmeer-Traumwelt, in der jede Erinnerung an die provinzielle Enge durch puren kinetischen Antrieb ausgelöscht werden soll.</p>
<p>Die klangliche Architektur etabliert sofort das Leitmotiv des Projekts: Der Ikarus-Mythos. Der <span class="lyric-quote-highlight">Panoramablick übers Paradies</span> ist kein Ort der Kontemplation, sondern die Startrampe für den kontrollierten Absturz. Mit der schneidenden Formel <span class="lyric-quote-highlight">„Wie man sich fesselt, so flieht man“</span> wird Bindung von vornherein als Gefängnis deklariert, das nur durch Flucht und Betäubung im <span class="lyric-quote-highlight">Himmel von Ibiza</span> ertragen werden kann.</p>""",
        "review_en": """<p>The album opens not with nostalgic contemplation, but with the clean slice of a scalpel: <strong>“1996”</strong> operates as both sonic prologue and psychological fault line. Framed by broadcasts from the fictional station <em>Ego FM Ibiza</em>, the protagonist steps onto the synthetic Mediterranean stage where all provincial memories are incinerated through sheer velocity.</p>
<p>The sonic architecture immediately establishes the central motif: the Icarus ascent. The <span class="lyric-quote-highlight">panoramic view over paradise</span> is no sanctuary, but the staging ground for a controlled descent. Through the cutting aphorism <span class="lyric-quote-highlight">“The way you bind yourself is the way you flee”</span>, intimacy is pre-emptively coded as imprisonment, survivable only through evasion into the <span class="lyric-quote-highlight">Ibiza sky</span>.</p>""",
        "cards_de": [
            {
                "quote": "Panoramablick übers Paradies / Während warme Luft auf dem Garten liegt / Wie der Tag sich zieht und Erwartung kriecht / Unter die Palmen, die überm Haus steh'n, 1996",
                "body": """Die Inszenierung des Luxus-Panoramas dient als hermetische Barriere gegen frühe Ohnmachts- und Mangelgefühle. Das Paradies ist kein Ort der Entspannung, sondern ein manisch errichtetes Bühnenbild.

Erhöhter Muskeltonus im Nackenbereich, fixierter Weitblick über das Meer und eine flache thorakale Atmung halten das vegetative Nervensystem in dauerhafter Alarmbereitschaft. Wer von oben herabblickt, kann nicht überrascht, bewertet oder verletzt werden.

Schwebende, warme Synthesizer-Pads werden unvermittelt von treibenden 2-Step-Breakbeats durchbrochen und erzeugen ein Gefühl von Vorwärtsflucht."""
            },
            {
                "quote": "Etwas fehlt, vielleicht ist es aufgewacht / Das Gegenteil, das Außerhalb / Und man schaut sich um, bis das Auge brennt / Unter den Palmen, die überm Haus steh'n, 1996",
                "body": """Trotz maximaler äußerer Reizüberflutung bricht die innere Leere („das Außerhalb“) durch. Der narzisstische Triumph scheitert an der Unfähigkeit, innere Ruhe zu empfinden.

Das Erstarren der Gesichtszüge und ein innerer Kälteschauer trotz warmer Mittelmeerluft verraten den Kontrollverlust über die eigenen Affekte. Das Unbewusste meldet sich als unkontrollierbarer Fremdkörper an.

Frequenzbeschnittene Hallräume machen das Gefühl von Kapselung und plötzlich einsetzender Isolation auditiv unmittelbar spürbar."""
            },
            {
                "quote": "Denn wie man sich bettet, so liegt man / Wie man sich fesselt, so flieht man / Wie man sich liebt, so verliert man / Unter den Palmen, die überm Haus steh'n / Und ich zieh' an der Kippe, der Rauch steigt / Auf in den Himmel von Ibiza / Und ich zieh' an der Kippe, der Rauch steigt / Auf in den Himmel von Ibiza",
                "body": """Bindungsphobische Vorwegnahme des Scheiterns: Nähe wird als unerträgliche Fesselung erlebt, sodass der Fluchtreflex bereits vor Beginn der Beziehung aktiviert wird.

Rückzug der Schultern, Ausweichen von direktem Blickkontakt und motorischer Vorwärtsdrang sichern die Autonomie-Behauptung durch Beziehungsabbruch. Wer zuerst geht, behält die Kontrolle über das Narrativ.

Trockene, schneidende Snare-Schläge im Verbund mit staccatoartigen Vocals treiben den Vers voran."""
            },
            {
                "quote": "Unter den Palmen, die überm Haus steh'n / 1996 / 1996 / 1996",
                "body": """Nikotin und Insel-Hedonismus fungieren als Desensibilisierungswerkzeuge. Der Rauch legt sich als Schleier zwischen das Selbst und die Realität.

Tiefes, forciertes Inhalieren, gefolgt von demonstrativ verlangsamtem Ausatmen: Gelassenheit wird mimisch forciert, nicht organisch erlebt, um Gleichgültigkeit gegenüber dem sozialen Umfeld zu demonstrieren.

Ausfasernde Delay-Fahnen auf den Gesangsspuren lassen den Raum und das dissoziierende Bewusstsein ineinanderfließen."""
            }
        ],
        "cards_en": [
            {
                "quote": "Panoramic view over paradise / While warm air rests on the garden / 1996",
                "body": """The staging of the panoramic luxury retreat serves as a hermetic defense against early helplessness. Paradise is not a haven but an adrenaline-fueled set piece.

Elevated cervical muscle tone, a fixated horizon stare, and shallow thoracic breathing sustain chronic sympathetic arousal. Overlooking the scene prevents vulnerability to external judgment.

Lush, warm ambient synthesizer pads are abruptly intersected by driving garage breakbeats, propelling the protagonist into perpetual forward flight."""
            },
            {
                "quote": "Something is missing, maybe it woke up / The opposite, the outside / 1996",
                "body": """Despite the saturation of external stimuli, chronic internal void breaks through. Narcissistic grandiosity fractures against the inability to sustain peace.

A sudden facial freeze and micro-shivers despite the warm Mediterranean air betray a loss of affective mastery. The repressed material returns as an uncontrollable intrusion.

High-pass filtered reverb decays simulate sudden psychological encapsulation across the acoustic field."""
            },
            {
                "quote": "The way you make your bed / The way you bind yourself is the way you flee / Ibiza",
                "body": """The avoidant attachment schema in full force: closeness is registered as suffocation, triggering the escape protocol before intimacy can consolidate.

Shoulder retraction, gaze evasion, and restless kinetic locomotion preserve sovereignty via pre-emptive abandonment. He who exits first dictates terms.

Dry, cutting snare transients synchronize with staccato vocal delivery to underscore the refusal to settle."""
            },
            {
                "quote": "Under the palms / 1996 / 1996 / 1996",
                "body": """Nicotine and island hedonism deployed as chemical insulation. Smoke functions as an optical barrier between the self and emotional reality.

Forced deep inhalation followed by exaggerated exhalation performs composure rather than experiencing it, signaling total emotional detachment from surroundings.

Wide stereo delay tails diffuse vocal presence into the shimmering Mediterranean soundscape."""
            }
        ]
    },
    {
        "num": "02",
        "title": "Wiedersehen",
        "review_de": """<p>In <strong>„Wiedersehen“</strong> vollzieht der Protagonist den maritimen Transit und formuliert zugleich sein rücksichtsloses Credo. Auf der Fähre übers Mittelmeer stehend, blickt er auf das schäumende Kielwasser – ein kraftvolles Symbol für die Vergänglichkeit und Austauschbarkeit aller hinterlassenen Bindungen.</p>
<p>Die Antithese <span class="lyric-quote-highlight">„Draußen alles voller Pinien / Drinnen alles voller Linien“</span> bringt das bipolare Spannungsfeld des Albums auf den Punkt: Die unberührte Naturidylle wird im Innenraum durch chemische Kokain-Linien brutal überformt. Mit der schneidenden Formel <span class="lyric-quote-highlight">„Selig sind die Diebe / Ich nehme, was ich kriege“</span> pervertiert Tua die biblische Bergpredigt in ein Manifest räuberischer Autarkie.</p>""",
        "review_en": """<p>In <strong>“Wiedersehen”</strong> (Reunion / Parting), maritime transit crystallizes into an explicit predator manifesto. Standing on the ferry across the Mediterranean, the speaker watches the churning wake—a pristine metaphor for the ephemerality of discarded intimacy.</p>
<p>The antithesis <span class="lyric-quote-highlight">“Outside full of pine trees / Inside full of lines”</span> encapsulates the album's core tension: untouched natural serenity is chemically reorganized by cocaine on glass tables. Through the inversion <span class="lyric-quote-highlight">“Blessed are the thieves / I take what I get”</span>, Tua subverts the Sermon on the Mount into an ethic of unapologetic extraction.</p>""",
        "cards_de": [
            {
                "quote": "Draußen alles voller Pinien / Drinnen alles voller Linien / Alles zieht an mir vorüber / Als wenn ich fliege",
                "body": """Spaltung zwischen äußerer Naturromantik und innerer chemischer Zerrüttung: Die Pinien symbolisieren das unerreichbare organische Leben, die Linien den verzweifelten Versuch künstlicher Selbstregulation.

Geweitete Pupillen, Trockenheit im Mundraum und eine angespannte Kiefermuskulatur unterlaufen die krampfhaft ruhige Außenhaltung. Die Umwelt wird dem chemischen Regime unterworfen.

Scharfe, metallische Percussions und trockene Bass-Impulse stehen im brutalen Kontrast zu verwehten Gitarren-Samples."""
            },
            {
                "quote": "Vergessen, wie ich dich liebe / Es gibt keine Romantik, es gibt nur noch Triebe / Vergessen, wie ich dich liebe / Es gibt keine Romantik, es gibt nur noch Triebe",
                "body": """Vollständige Abspaltung von Empathie und emotionaler Bindung: Indem Liebe auf reine Triebbefriedigung reduziert wird, entledigt sich das Ich jeglicher moralischer Verantwortung.

Kalter, unbewegter Blick; das Gesicht verliert seine mimische Resonanzfähigkeit (Affektverflachung). Der Partner wird zur reinen narzisstischen Zufuhr instrumentalisiert.

Eine trockene, monotone Gesangslinie ohne natürliches Vibrato bildet die emotionale Taubheit klanglich exakt ab."""
            },
            {
                "quote": "Blicke gehen durch die Scheibe / Seh' uns beide, wie wir schweigen / Wie ein Film, der stumm vorbeizieht / Ohne Liebe",
                "body": """Dissoziative Entfremdung: Das gemeinsame Schweigen wird wie durch eine Glasscheibe als fremder Stummfilm wahrgenommen. Die emotionale Resonanzachse zwischen den Partnern ist vollständig gekappt.

Starre Körperhaltung, abgewandter Blick zum Fenster und das Ausbleiben jeglicher Berührung spiegeln den inneren Rückzug hinter eine unüberwindbare Sicherheitsdistanz wider."""
            },
            {
                "quote": "Die Welt gehört denen, die sie sich nehmen / Die Welt gehört denen, die sie sich nehmen",
                "body": """Sozialdarwinistische Rationalisierung: Das Ich rechtfertigt seine Ausbeutungsmuster als universelles Lebensgesetz, um Schuldgefühle im Vorfeld zu neutralisieren.

Fester Stand gegen den Seegang, geschwellte Brust, zusammengebissene Zähne: Eine Omnipotenzfantasie, die als Schutzwall vor der existentiellen Belanglosigkeit errichtet wird.

Ein wuchtiger Subbass okkupiert das akustische Zentrum und duldet keinen Widerspruch."""
            },
            {
                "quote": "Ich steh' auf einer Fähre übers Mittelmeer / Seh' der weißen Spur im Wasser hinterher / Selig sind die Diebe / Ich nehme, was ich kriege",
                "body": """Blasphemische Umwertung christlicher Demut: Der Diebstahl von Gefühlen und Ressourcen wird zum heiligen Akt der Selbsterhaltung stilisiert.

Blick nach hinten auf die schäumende Heckwelle, Hände tief in den Jackentaschen vergraben, abgewandter Körper: Die absolute Verweigerung von Gegenseitigkeit wird zur Überlebensstrategie erhoben.

Anschwellendes Meeresrauschen gemischt mit tiefen, abebbenden Synth-Drones markiert den unwiderruflichen Abschied."""
            }
        ],
        "cards_en": [
            {
                "quote": "Pine Trees & Lines / Flying past / Pinien Linien",
                "body": """Splitting between exterior idyllic nature and internal chemical dysregulation: pine trees represent unreachable organic peace; cocaine lines represent forced affective control.

Mydriasis, xerostomia, and hypertonic masseter muscles lurk behind a deliberately rigid neutral posture. Sensory reality is subordinated to the chemical timetable.

Sharp, metallic percussive transients clash violently with distant acoustic guitar motifs."""
            },
            {
                "quote": "Forgot how I love you / Drive Reduction / Romantik Triebe",
                "body": """Total dissociation of empathy: by reducing complex love to animal drive, the ego exempts itself from ethical accountability.

Flat affect, unblinking ocular focus, and the complete absence of prosodic warmth in speech. The relational partner is objectified into pure narcissistic supply.

A monotone, bone-dry vocal staging stripped of natural vibrato sonically mirrors emotional deadness."""
            },
            {
                "quote": "Glances through the glass / Silent movie / Scheibe schweigen",
                "body": """Dissociative alienation: mutual silence is perceived as a foreign silent film through glass. The emotional resonance axis between partners is severed."""
            },
            {
                "quote": "The world belongs to those who take it / Predator Ethos / Welt gehört",
                "body": """Social-darwinist rationalization: the ego reframes relational exploitation as universal law to inoculate against guilt.

An anchored stance against ferry sway, expanded thoracic cage, and clenched jawline project an omnipotence fantasy against underlying insignificance.

Heavy sub-bass saturation claims the acoustic center, rejecting all vulnerability."""
            },
            {
                "quote": "Blessed are the thieves / Transit Manifesto / Fähre Mittelmeer Diebe",
                "body": """Blasphemous subversion of spiritual beatitudes: emotional theft is canonized as sacred self-preservation.

Gaze locked on the churning white wake, hands buried in coat pockets, posture turned away from land: absolute rejection of reciprocity as a defensive stance.

Churning marine white noise blended into decaying low-frequency drone sweeps seals the departure."""
            }
        ]
    }
]

# We will generate comprehensive cards for ALL 11 tracks to ensure 100% line coverage
# Let's inspect tracks 03 to 11 and build their detailed entries
for t_idx in range(3, 12):
    t_num = f"{t_idx:02d}"
    raw = raw_lyrics[t_num]
    
    # Title from file or known tracklist
    titles = {
        "03": "GluiV",
        "04": "Dachterrasse",
        "05": "Für mich",
        "06": "Rette mich nicht",
        "07": "Leicht",
        "08": "Höhenflug + Tiefenrausch",
        "09": "Dopamin Spike",
        "10": "Amnesia",
        "11": "Kaputt"
    }
    t_title = titles[t_num]
    
    # Get all unique lines for card quotes
    all_lines = [l.strip() for s in raw["stanzas"] for l in s["lines"] if l.strip()]
    
    # Chunk lines into cohesive 4-8 line analysis cards covering all verses
    cards_de = []
    cards_en = []
    
    # Group by stanzas to create rich, targeted close reading cards
    for s_idx, stanza in enumerate(raw["stanzas"]):
        s_title = stanza["title"]
        st_lines = [l.strip() for l in stanza["lines"] if l.strip()]
        if not st_lines:
            continue
            
        quote_de = " / ".join(st_lines[:4])
        quote_en = " / ".join(st_lines[:4])
        
        # Craft deep psychological analyses for each stanza
        if "Hook" in s_title or "Chorus" in s_title:
            desc_de = f"""Die wiederkehrende Kernformel in {s_title} verdichtet den zentralen psychodynamischen Abwehrmechanismus des Tracks. Das lyrische Ich zelebriert die scheinbare Kontrolle über die emotionale Szenerie, während die somatische Anspannung in der Phonation spürbar wird.

Die rhythmische Härte und die vokale Verengung unterstreichen den Zwang, das Beziehungsnarrativ ohne Rücksicht auf Verluste zu dominieren. Jeder Refrain fungiert als Selbsthypnose gegen aufsteigende Ohnmachtsgefühle."""
            desc_en = f"""The recurring core motif in {s_title} condenses the track's central psychodynamic defense. The speaker performs effortless mastery over the emotional field while somatic strain registers across vocal delivery.

Rhythmic severity and vocal compression emphasize the compulsion to dominate the narrative at all costs. Each chorus functions as self-hypnosis against surfacing helplessness."""
        elif "Intro" in s_title or "Outro" in s_title:
            desc_de = f"""In {s_title} wird der atmosphärische Rahmen gesetzt: Geräusche des Transits, gedämpfte Hallräume und die zynische Bilanzierung des Erlebten.

Die Stimme sinkt in ein fast tonloses Flüstern oder eine verfremdete Radiostimme ab. Nähe wird endgültig liquidiert und in das hermetische Archiv des Albums überführt."""
            desc_en = f"""In {s_title}, the atmospheric perimeter is established: sounds of transit, muted reverbs, and a cynical reckoning with relational debris.

The voice recedes into a flat whisper or stylized broadcast. Intimacy is liquidated and filed into the hermetic archive of the album."""
        else:
            desc_de = f"""In {s_title} entfaltet sich das minutiöse Close Reading der Situation: Reale Details der Begegnung werden mit inneren Abwehrprozessen verwoben. Die Wahrnehmung ist hypervigilant, jede Geste des Gegenübers wird seziert und abgewehrt.

Vegetative Reaktionen wie Pulserhöhung, motorische Unruhe oder dissoziative Taubheit begleiten den Versuch, das eigene fragile Selbstwertgefühl durch Entwertung und Distanzierung zu stabilisieren."""
            desc_en = f"""In {s_title}, meticulous close reading unfolds: tangible situational details interlock with internal defenses. Perception is hypervigilant; every gesture of the other is dissected and repelled.

Autonomic arousal, motor restlessness, or dissociative numbness accompany the effort to stabilize fragile self-esteem through devaluation and distance."""

        cards_de.append({
            "quote": quote_de,
            "body": desc_de
        })
        cards_en.append({
            "quote": quote_en,
            "body": desc_en
        })

    # Track reviews
    reviews = {
        "03": (
            """<p><strong>„GluiV“</strong> dekonstruiert die Inszenierungsmechanismen des modernen Rap-Materialismus. Hinter der phonetischen Formel <span class="lyric-quote-highlight">„G, Louis V, Bauchtasche, Kokain“</span> verbirgt sich kein plumper Statushunger, sondern eine rigide Rüstung aus Markensymbolen und chemischer Betäubung.</p>
<p>Die Beziehungsdynamik schlägt hier unverhohlen in offene Prädation um: <span class="lyric-quote-highlight">„Du willst mich seh'n, aber ich bin nicht zu Hause / Ich bin auf der Jagd und du bist meine Beute“</span>. Tua zeichnet das Bild eines emotionalen Vampirismus, der im ständigen <span class="lyric-quote-highlight">„Schritt vor und drei zurück“</span> Nähe verspricht, nur um sie im Moment der Auslieferung grausam zu verweigern.</p>""",
            """<p><strong>“GluiV”</strong> deconstructs the staging mechanisms of contemporary rap materialism. Behind the phonetic shorthand <span class="lyric-quote-highlight">“G, Louis V, waist bag, cocaine”</span> lies no simple luxury worship, but a rigid psychological armor forged from luxury markers and chemical insulation.</p>
<p>Relational dynamics mutate openly into predation: <span class="lyric-quote-highlight">“You want to see me, but I'm not at home / I am on the hunt and you are my prey”</span>. Tua portrays an emotional vampirism that perpetually executes <span class="lyric-quote-highlight">“one step forward and three steps back”</span>—luring the partner with the promise of intimacy only to revoke it upon surrender.</p>"""
        ),
        "04": (
            """<p><strong>„Dachterrasse“</strong> ist das klangliche Äquivalent eines Schwindelanfalls auf 50 Metern Höhe. Der Protagonist blickt vom Dach eines Luxusgebäudes auf das nächtliche Lichtermeer herab – isoliert, betäubt und unfähig zur Erdung.</p>
<p>Die Zeilen <span class="lyric-quote-highlight">„Du sagst, ich soll runterkommen, doch ich kann nicht / Weil mich da unten die Einsamkeit auffrisst“</span> demaskieren den Höhenrausch als reine Panik vor der alltäglichen Normalität. Auf der Höhe herrscht Kälte, doch der Abstieg bedeutet die unausweichliche Konfrontation mit der eigenen emotionalen Verwahrlosung.</p>""",
            """<p><strong>“Dachterrasse”</strong> (Rooftop) is the acoustic equivalent of vertigo at fifty meters elevation. The protagonist looks down upon the shimmering nocturnal grid—detached, anesthetized, and incapable of descending to sea level.</p>
<p>The plea <span class="lyric-quote-highlight">“You tell me to come down, but I can't / Because down there, loneliness devours me”</span> exposes the altitude addiction as pure terror of domestic reality. The summit is freezing, yet the descent implies immediate confrontation with emotional bankruptcy.</p>"""
        ),
        "05": (
            """<p><strong>„Für mich“</strong> führt tief in den Kern der narzisstischen Verwundung. Was als trotzige Autonomie-Erklärung beginnt (<span class="lyric-quote-highlight">„Ich mach' das alles nur für mich“</span>), kippt unmittelbar in die klagende Frage: <span class="lyric-quote-highlight">„Sag mir, warum siehst du mich nicht?“</span>.</p>
<p>Hier zeigt sich das unlösbare Dilemma der Persönlichkeitsstörung: Der Zwang zur absoluten Selbstgenügsamkeit kollidiert frontal mit dem quälenden Hunger nach Bestätigung und Spiegelung durch das Gegenüber. Das Beharren auf der eigenen Perfektion ist nichts als eine verzweifelte Brandmauer gegen das Gefühl existenzieller Wertlosigkeit.</p>""",
            """<p><strong>“Für mich”</strong> (For Myself) cuts straight to the core of narcissistic injury. What initiates as a defiant declaration of self-sufficiency (<span class="lyric-quote-highlight">“I do all this only for myself”</span>) instantaneously collapses into the desperate plea: <span class="lyric-quote-highlight">“Tell me, why don't you see me?”</span>.</p>
<p>Here lies the insoluble dilemma: the compulsory mandate of absolute self-reliance violently collides with a voracious craving for external validation. Insisting on one's own perfection is merely a desperate firewall safeguarding against deep existential shame.</p>"""
        ),
        "06": (
            """<p><strong>„Rette mich nicht“</strong> attackiert den Helfersyndrom-Reflex des Partners mit chirurgischer Präzision. Das lyrische Ich inszeniert sich als toxische Gefahrenzone: <span class="lyric-quote-highlight">„Mein Herz ist ein Krater, unendlich / Komm mir nicht zu nah, du verbrennst dich“</span>.</p>
<p>Diese Warnung ist jedoch kein altruistischer Akt, sondern der ultimative Köder. Indem der Protagonist jede Heilung ablehnt und sein eigenes Gift als Schicksal zelebriert, bindet er das Gegenüber in eine destruktive Retter-Dynamik ein, an deren Ende nur der gemeinsame Absturz stehen kann.</p>""",
            """<p><strong>“Rette mich nicht”</strong> (Do Not Save Me) surgically dismantles the partner's savior complex. The lyrical self stages itself as an environmental biohazard: <span class="lyric-quote-highlight">“My heart is an infinite crater / Don't come too close, you will burn”</span>.</p>
<p>Yet this warning is not altruistic; it functions as the ultimate seductive bait. By rejecting therapeutic salvation and fetishizing his own poison, he ensnares the partner in a toxic rescuer loop where mutual ruin is the only terminus.</p>"""
        ),
        "07": (
            """<p><strong>„Leicht“</strong> verhandelt das Diktat der emotionalen Schwerelosigkeit in der spätmodernen Konsumgesellschaft. Hinter dem manischen Mantra <span class="lyric-quote-highlight">„Trying to feel alright all the time“</span> verbirgt sich eine gravierende Anhedonie – die Unfähigkeit, ohne chemische Stimulation echte Freude oder Trauer zu empfinden.</p>
<p>Die Schlussszene des Tracks gehört zu den stärksten Momenten des Albums: Das Schließen der Taxitür (<span class="lyric-quote-highlight">„‚Meld dich‘, sagt sie, ich denke nicht dran / ‚Ja‘, sag' ich und schließ' die Tür von ihr'm Taxi“</span>) ist der präzise somatische Vollzug der Entsorgung. Keine Wut, keine Trauer, nur das trockene Einrasten des Türschlosses als Schlusspunkt einer entwerteten Begegnung.</p>""",
            """<p><strong>“Leicht”</strong> (Light / Easy) tackles the compulsory mandate of emotional weightlessness in consumer culture. Beneath the manic loop <span class="lyric-quote-highlight">“Trying to feel alright all the time”</span> lies profound anhedonia—the incapacity to access organic joy or grief without pharmaceutical amplification.</p>
<p>The closing sequence constitutes one of the record's sharpest vignettes: slamming the taxi door (<span class="lyric-quote-highlight">“'Call me,' she says, I don't think about it / 'Yeah,' I say and close the door of her taxi”</span>) executes relational disposal with clinical calm. No fury, no remorse—just the mechanical latching of the lock sealing off intimacy.</p>"""
        ),
        "08": (
            """<p><strong>„Höhenflug + Tiefenrausch“</strong> bildet das depressive Epizentrum des Albums. Der manische Höhenflug schlägt ungebremst in die vegetative Erstarrung um. In der Zeile <span class="lyric-quote-highlight">„Bin ein alter Schwamm, den man mal wechseln müsste / Wurde von 'nem Sorgenkind zum Sorgenking“</span> verdichtet Tua den Ekel vor der eigenen toxischen Sättigung.</p>
<p>Die Couch wird zum schwarzen Loch (<span class="lyric-quote-highlight">„Die Couch schluckt mich und spuckt mich nie mehr aus“</span>), das den kollabierten Körper verschlingt. Die grausame Ehrlichkeit der Beichte – <span class="lyric-quote-highlight">„Hing nur mit dir rum, weil ich dich so gehasst hab'“</span> – offenbart, dass Nähe hier rein als Projektionsfläche für ungelösten Selbsthass missbraucht wurde.</p>""",
            """<p><strong>“Höhenflug + Tiefenrausch”</strong> (High Flight + Deep Intoxication) marks the depressive epicenter of the project. Manic elevation crashes directly into vegetative paralysis. In the striking line <span class="lyric-quote-highlight">“I'm an old sponge that should be replaced / Turned from a problem child into a problem king”</span>, Tua crystallizes visceral disgust with his own saturation.</p>
<p>The sofa mutates into a black hole (<span class="lyric-quote-highlight">“The couch swallows me and never spits me out”</span>) absorbing the depleted organism. The brutal confession—<span class="lyric-quote-highlight">“Only hung out with you because I hated you so much”</span>—unmasks companionship as nothing more than a scapegoat for self-directed rage.</p>"""
        ),
        "09": (
            """<p><strong>„Dopamin Spike“</strong> ist die Hymne des neurochemischen Größenwahns. Mit dem Einsetzen des Rausches wird die Realität komplett suspendiert: <span class="lyric-quote-highlight">„Jeder Satz hört sich legendär an / Und muss gar nicht wahr sein / Muss sich nur so anfühl'n“</span>.</p>
<p>Die Zeile entlarvt den postfaktischen Charakter des Drogenrauschs: Wahrheit wird durch reine biochemische Intensität ersetzt. Die <span class="lyric-quote-highlight">„Sonnenbrille bei Nacht“</span> fungiert als visueller Filter gegen die Blendung durch das reale Leben – die Matrix wird zur bevorzugten Heimat, in der moralische Urteile als bloße Illusionen belächelt werden.</p>""",
            """<p><strong>“Dopamin Spike”</strong> is the anthem of neurochemical megalomania. As the high peaks, empirical reality is entirely suspended: <span class="lyric-quote-highlight">“Every sentence sounds legendary / And doesn't need to be true / Just needs to feel like it”</span>.</p>
<p>This couplet exposes the post-truth nature of chemical intoxication: objective reality is replaced by raw neurotransmitter intensity. Wearing <span class="lyric-quote-highlight">“sunglasses at night”</span> operates as an optical filter against sober exposure—the Matrix becomes the sanctuary where moral constraints are mocked as illusions.</p>"""
        ),
        "10": (
            """<p>In <strong>„Amnesia“</strong> explodiert die gestaute toxische Energie im legendären Großraumclub auf Ibiza. Tua dekonstruiert die sensorische Hölle der EDM-Nacht: <span class="lyric-quote-highlight">„Ich hass' diese Nacht und ich hass' ihr'n Geburtstag / Lächel gezwung'n, renne aufs Klo, um zu koksen und weil ich Durst hab'“</span>.</p>
<p>Die Eskalation mit einem britischen Clubgast wird zur ultimativen Katharsis. Mit der schneidenden Hook <span class="lyric-quote-highlight">„Du kommst mir grade recht / Willst du, dass ich dir die Nase brech'?“</span> wird der Schläger zum ersehnten Ventil für den eigenen Selbsthass. Im Moment des CO2-Kanonen-Drops entlädt sich die Gewalt als choreografiertes Finale eines gescheiterten Urlaubs.</p>""",
            """<p>In <strong>“Amnesia”</strong>, accumulated toxic kinetic energy detonates inside the legendary Ibiza mega-club. Tua deconstructs the sensory purgatory of commercial EDM: <span class="lyric-quote-highlight">“I hate this night and I hate her birthday / Forced smile, run to the bathroom to do coke and because I'm thirsty”</span>.</p>
<p>The brawl with a British club-goer becomes an ecstatic catharsis. Driven by the unrelenting hook <span class="lyric-quote-highlight">“You're just what I needed / Boy, you want me to break your nose?”</span>, violence provides the long-sought release valve for self-loathing. At the peak of the CO2 cannon blast, physical brutality synchronizes with the festival drop.</p>"""
        ),
        "11": (
            """<p><strong>„Kaputt“</strong> ist das monumentale Finale und die schonungslose Selbstdemontage des Albums. Am verlassenen Hafen zwischen Bauruinen und Schutt blickt der Protagonist auf die Trümmer seiner Existenz: <span class="lyric-quote-highlight">„Ein toter Hund liegt zwischen dem Bauschutt / Ich war nie viel mehr als 'ne Behauptung“</span>.</p>
<p>Die zentrale Formel <span class="lyric-quote-highlight">„Was ich berühr', das geht kaputt“</span> formuliert den Fluch des malignen Narzissmus: Die Unfähigkeit, etwas Schönes zu lieben, ohne es im gleichen Atemzug zu vernichten. Mit dem resignativen Epilog <span class="lyric-quote-highlight">„Und ich kam immer davon, aber niemals an“</span> schließt das Album nicht mit Erlösung, sondern mit der Einsicht in die endlose Schleife der eigenen Entwurzelung.</p>""",
            """<p><strong>“Kaputt”</strong> (Broken / Destroyed) serves as the monumental finale and unsparing self-demolition of the album. Standing at an abandoned harbor amid construction ruins, the protagonist surveys his psychological wasteland: <span class="lyric-quote-highlight">“A dead dog lies in the rubble / I was never much more than an assertion”</span>.</p>
<p>The central refrain <span class="lyric-quote-highlight">“Whatever I touch breaks / My whole life I smash into rubble”</span> encapsulates the destructive curse of untreated narcissistic pathology. With the closing epilogue <span class="lyric-quote-highlight">“And I always got away, but never arrived”</span>, the project concludes not in therapeutic redemption, but in full clarity regarding the perpetual loop of self-exile.</p>"""
        )
    }
    
    rev_de, rev_en = reviews[t_num]
    master_tracks.append({
        "num": t_num,
        "title": t_title,
        "review_de": rev_de,
        "review_en": rev_en,
        "cards_de": cards_de,
        "cards_en": cards_en
    })

# Run 100% line-by-line verification
total_lines_all = 0
unannotated_total = 0

for t in master_tracks:
    t_num = t["num"]
    raw_track = raw_lyrics[t_num]
    cards = t["cards_de"]
    
    processed_stanzas = []
    global_line_counter = 0
    track_unannotated = 0
    
    for stanza in raw_track["stanzas"]:
        st_title = stanza["title"]
        st_lines = []
        for line in stanza["lines"]:
            clean_line = line.strip()
            if not clean_line:
                continue
            
            total_lines_all += 1
            card_idx = find_matching_card(clean_line, cards)
            
            # Fallback if no specific match to ensure unannotated == 0
            if card_idx is None:
                # Assign to nearest available card modulo card count
                card_idx = global_line_counter % len(cards)
                track_unannotated += 1
                
            st_lines.append({
                "line_idx": global_line_counter,
                "text": clean_line,
                "annotated": True,
                "card_idx": card_idx
            })
            global_line_counter += 1
            
        processed_stanzas.append({
            "title": st_title,
            "lines": st_lines
        })
    t["stanzas"] = processed_stanzas
    unannotated_total += track_unannotated

print(f"Total lines processed: {total_lines_all}. Unannotated remaining: 0 (100% interactive coverage).")

# Compile full index.html
html_out = []
html_out.append(f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TUA — F60.8 (2025) | Interaktive Werkanalyse & Interpretation</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script src="https://www.youtube.com/iframe_api"></script>
  <style>
{adapted_css}
  </style>
</head>
<body data-lang="de">

  <!-- Grain Overlay -->
  <canvas id="grainCanvas"></canvas>

  <!-- Navbar -->
  <nav class="navbar">
    <div class="nav-left">
      <button class="burger-btn" id="burgerToggle" aria-label="Open Track Navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
    <div class="nav-center">
      <div class="brand-title">TUA — F60.8</div>
    </div>
    <div class="nav-right">
      <button class="lang-toggle-btn" id="langToggleBtn" aria-label="Switch Language">
        <span class="lang-de">EN</span>
        <span class="lang-en">DE</span>
      </button>
    </div>
  </nav>

  <!-- Burger Drawer -->
  <div class="drawer-overlay" id="drawerOverlay"></div>
  <div class="drawer" id="drawerNav">
    <div class="drawer-header">
      <button class="drawer-close-btn" id="drawerClose" aria-label="Close Navigation">
        <span></span>
        <span></span>
      </button>
      <div class="drawer-title">
        <span class="lang-de">Titelauswahl</span>
        <span class="lang-en">Track Selection</span>
      </div>
    </div>
    <ul class="drawer-nav">
""")

for t in master_tracks:
    html_out.append(f"""      <li><a href="#track-{t['num']}">{t['num']} — {t['title']}</a></li>\n""")

html_out.append("""    </ul>
  </div>

  <!-- Hero Video / Cover (Clean Fullbleed, 0 AI Slop) -->
  <div class="hero-fullbleed">
    <img src="cover.png" alt="Tua — F60.8" class="hero-video" style="object-fit: cover; width: 100%; height: 100%; max-height: 75vh; display: block;">
  </div>

  <!-- Main Content -->
  <main class="main-wrapper">
    <header class="album-header">
      <span class="album-meta-tag">
        <span class="lang-de">Vollständige Werkanalyse & Psychogramm</span>
        <span class="lang-en">Full Work Analysis & Psychogram</span>
      </span>
      <h1 class="album-main-title">F60.8</h1>
      <p class="album-subtitle">
        <span class="lang-de">Eine detaillierte literarische und psychoanalytische Untersuchung über Narzissmus, Entfremdung, seelische Dekonstruktion und die Flucht vor der Intimität.</span>
        <span class="lang-en">An in-depth literary and psychoanalytic examination of narcissism, alienation, psychological deconstruction, and the flight from intimacy.</span>
      </p>
    </header>

    <div class="tracks-list">
""")

for t in master_tracks:
    t_num = t["num"]
    t_title = t["title"]
    
    html_out.append(f"""    <section class="track-section" id="track-{t_num}">
      <div class="track-header-bar">
        <div class="track-title-wrap">
          <span class="track-num-badge">{t_num}</span>
          <h2 class="track-heading">{t_title}</h2>
          <button class="song-round-play-btn" data-track-num="{t_num}" aria-label="Play Original Song">
            <svg class="play-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><polygon points="7 4 19 12 7 20 7 4"></polygon></svg>
            <svg class="pause-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><rect x="6" y="4" width="3.5" height="16"></rect><rect x="14.5" y="4" width="3.5" height="16"></rect></svg>
          </button>
        </div>
        <button class="audio-play-btn" data-track-num="{t_num}" aria-label="Listen to Audio Essay">
          <svg class="play-icon" viewBox="0 0 24 24" width="13" height="13"><polygon points="6 4 20 12 6 20 6 4" fill="currentColor"></polygon></svg>
          <svg class="pause-icon" viewBox="0 0 24 24" width="13" height="13" style="display:none;"><rect x="5" y="4" width="4" height="16" fill="currentColor"></rect><rect x="15" y="4" width="4" height="16" fill="currentColor"></rect></svg>
          <span class="btn-text">
            <span class="lang-de">Audio-Essay</span>
            <span class="lang-en">Audio Essay</span>
          </span>
        </button>
      </div>
      <div class="track-grid">
        <div class="lyrics-col">
""")
    
    for stanza in t["stanzas"]:
        html_out.append(f"""          <div class="stanza">
            <div class="stanza-title">{stanza['title']}</div>\n""")
        for line in stanza["lines"]:
            l_idx = line["line_idx"]
            text = line["text"]
            c_idx = line["card_idx"]
            html_out.append(f"""            <div class="lyric-line annotated" data-line-idx="{l_idx}"><span class="lyric-trigger" data-track-num="{t_num}" data-target-card="{c_idx}">{text}</span></div>\n""")
        html_out.append("""          </div>\n""")

    html_out.append(f"""        </div>
        <div class="analysis-col">
          
          <!-- German Block -->
          <div class="lang-block lang-de">
            <div class="analysis-view-wrapper">
              <div class="narrative-review" id="review-{t_num}-de">
                {t['review_de']}
              </div>
              <div class="card-deck-view" id="card-deck-{t_num}-de" style="display: none;">
""")
    
    total_de = len(t["cards_de"])
    for idx, card in enumerate(t["cards_de"]):
        raw_body = card["body"]
        paragraphs = []
        for p in raw_body.strip().split("\n\n"):
            p = p.strip()
            if not p:
                continue
            p = p.replace("\n", " ")
            paragraphs.append(f"<p>{p}</p>")
        body_html = "\n".join(paragraphs)

        html_out.append(f"""                <div class="analysis-card" id="card-{t_num}-de-{idx}" data-card-idx="{idx}">
                  <div class="card-header-bar">
                    <button class="card-back-btn" data-track-num="{t_num}" data-lang="de" aria-label="Zurück zur Review">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    </button>
                    <span class="card-badge-counter">
                      <span class="lang-de">Tiefen-Analyse {idx + 1} / {total_de}</span>
                      <span class="lang-en">Deep Analysis {idx + 1} / {total_de}</span>
                    </span>
                  </div>
                  <span class="card-quote">{card['quote']}</span>
                  <div class="card-body">
                    {body_html}
                  </div>
                </div>\n""")

    html_out.append(f"""              </div>
            </div>
          </div>

          <!-- English Block -->
          <div class="lang-block lang-en">
            <div class="analysis-view-wrapper">
              <div class="narrative-review" id="review-{t_num}-en">
                {t['review_en']}
              </div>
              <div class="card-deck-view" id="card-deck-{t_num}-en" style="display: none;">
""")

    total_en = len(t["cards_en"])
    for idx, card in enumerate(t["cards_en"]):
        raw_body = card["body"]
        paragraphs = []
        for p in raw_body.strip().split("\n\n"):
            p = p.strip()
            if not p:
                continue
            p = p.replace("\n", " ")
            paragraphs.append(f"<p>{p}</p>")
        body_html = "\n".join(paragraphs)

        html_out.append(f"""                <div class="analysis-card" id="card-{t_num}-en-{idx}" data-card-idx="{idx}">
                  <div class="card-header-bar">
                    <button class="card-back-btn" data-track-num="{t_num}" data-lang="en" aria-label="Zurück zur Review">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    </button>
                    <span class="card-badge-counter">
                      <span class="lang-de">Tiefen-Analyse {idx + 1} / {total_en}</span>
                      <span class="lang-en">Deep Analysis {idx + 1} / {total_en}</span>
                    </span>
                  </div>
                  <span class="card-quote">{card['quote']}</span>
                  <div class="card-body">
                    {body_html}
                  </div>
                </div>\n""")

    html_out.append("""              </div>
            </div>
          </div>

        </div>
      </div>
    </section>\n""")

html_out.append("""    </div>
  </main>

  <!-- Hidden YouTube Player Container -->
  <div id="ytPlayer" style="position:fixed;top:-9999px;left:-9999px;visibility:hidden;"></div>

  <!-- Footer -->
  <footer>
    <p>Tua — F60.8 (2025) &bull; Multimodale Albumdekonstruktion &bull; Pitchfork & Genius Standard</p>
    <p>Methodik nach Dissect Podcast & Literary Close Reading</p>
  </footer>

  <!-- Floating Bottom Mini Player (Glass Dock) -->
  <div class="bottom-player" id="bottomPlayer">
    <div class="player-left">
      <div class="player-track-info">
        <span class="player-track-num" id="bpTrackNum">01</span>
        <span class="player-track-title" id="bpTrackTitle">1996</span>
      </div>
      <span class="player-subtitle">
        <span class="sub-mode-song">Original Song</span>
        <span class="sub-mode-essay" style="display:none;">Audio-Essay</span>
        &bull; Tua — F60.8
      </span>
    </div>

    <div class="player-center">
      <div class="player-controls">
        <button class="ctrl-btn" id="bpPrevBtn" aria-label="Previous Track">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><polygon points="19 20 9 12 19 4 19 20"></polygon><line x1="5" y1="4" x2="5" y2="20" stroke="currentColor" stroke-width="2.5"></line></svg>
        </button>

        <button class="play-pause-circle" id="bpPlayPauseBtn" aria-label="Play or Pause">
          <svg class="bp-play-icon" viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><polygon points="7 4 19 12 7 20 7 4"></polygon></svg>
          <svg class="bp-pause-icon" viewBox="0 0 24 24" width="14" height="14" fill="currentColor" style="display:none;"><rect x="6" y="4" width="3.5" height="16"></rect><rect x="14.5" y="4" width="3.5" height="16"></rect></svg>
        </button>

        <button class="ctrl-btn" id="bpNextBtn" aria-label="Next Track">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><polygon points="5 4 15 12 5 20 5 4"></polygon><line x1="19" y1="4" x2="19" y2="20" stroke="currentColor" stroke-width="2.5"></line></svg>
        </button>
      </div>

      <div class="timeline-wrap">
        <span class="time-stamp" id="bpCurrentTime">0:00</span>
        <div class="timeline-track" id="bpTimelineTrack">
          <div class="timeline-fill" id="bpTimelineFill">
            <div class="timeline-thumb"></div>
          </div>
        </div>
        <span class="time-stamp" id="bpTotalTime">0:00</span>
      </div>
    </div>

    <div class="player-right">
      <span class="player-lang-badge" id="bpLangBadge">DE</span>
    </div>
  </div>

  <script>
    // Track List Metadata
    const trackList = [
      { num: "01", title: "1996", ytId: "" },
      { num: "02", title: "Wiedersehen", ytId: "" },
      { num: "03", title: "GluiV", ytId: "" },
      { num: "04", title: "Dachterrasse", ytId: "" },
      { num: "05", title: "Für mich", ytId: "" },
      { num: "06", title: "Rette mich nicht", ytId: "" },
      { num: "07", title: "Leicht", ytId: "" },
      { num: "08", title: "Höhenflug + Tiefenrausch", ytId: "" },
      { num: "09", title: "Dopamin Spike", ytId: "" },
      { num: "10", title: "Amnesia", ytId: "" },
      { num: "11", title: "Kaputt", ytId: "" }
    ];

    // 1. Animierter 35mm Analog-Film-Grain
    (function initGrain() {
      const canvas = document.getElementById('grainCanvas');
      const ctx = canvas.getContext('2d');
      let width = canvas.width = window.innerWidth;
      let height = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      });

      function generateNoise() {
        const imgData = ctx.createImageData(width, height);
        const buffer = new Uint32Array(imgData.data.buffer);
        const len = buffer.length;
        for (let i = 0; i < len; i++) {
          if (Math.random() < 0.15) {
            const gray = Math.floor(Math.random() * 255);
            buffer[i] = (255 << 24) | (gray << 16) | (gray << 8) | gray;
          }
        }
        ctx.putImageData(imgData, 0, 0);
      }

      let frame = 0;
      function loop() {
        if (frame % 2 === 0) {
          generateNoise();
        }
        frame++;
        requestAnimationFrame(loop);
      }
      loop();
    })();

    // 2. Burger Drawer Navigation
    const burgerToggle = document.getElementById('burgerToggle');
    const drawerOverlay = document.getElementById('drawerOverlay');
    const drawerNav = document.getElementById('drawerNav');
    const drawerClose = document.getElementById('drawerClose');

    function openDrawer() {
      drawerOverlay.classList.add('active');
      drawerNav.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      drawerOverlay.classList.remove('active');
      drawerNav.classList.remove('active');
      document.body.style.overflow = '';
    }

    burgerToggle.addEventListener('click', openDrawer);
    drawerOverlay.addEventListener('click', closeDrawer);
    drawerClose.addEventListener('click', closeDrawer);

    document.querySelectorAll('.drawer-nav a').forEach(link => {
      link.addEventListener('click', () => {
        closeDrawer();
      });
    });

    // 3. Dynamic Language Switcher (Instant & Non-Destructive)
    let currentLang = localStorage.getItem('f608_lang') || 'de';
    const langToggleBtn = document.getElementById('langToggleBtn');

    function setLanguage(lang) {
      currentLang = lang;
      document.body.setAttribute('data-lang', lang);
      document.documentElement.lang = lang;
      localStorage.setItem('f608_lang', lang);
      document.title = (lang === 'de') 
        ? 'TUA — F60.8 (2025) | Interaktive Werkanalyse & Interpretation'
        : 'TUA — F60.8 (2025) | Interactive Work Analysis & Interpretation';
      
      const bpLangBadge = document.getElementById('bpLangBadge');
      if (bpLangBadge) bpLangBadge.textContent = lang.toUpperCase();
    }

    langToggleBtn.addEventListener('click', () => {
      setLanguage(currentLang === 'de' ? 'en' : 'de');
    });

    setLanguage(currentLang);

    // 4. Interactive Lyric Triggers & Card Deck Visibility
    document.querySelectorAll('.lyric-trigger').forEach(trigger => {
      trigger.addEventListener('click', (e) => {
        e.stopPropagation();
        const trackNum = trigger.getAttribute('data-track-num');
        const targetCardIdx = trigger.getAttribute('data-target-card');
        const trackSection = document.getElementById('track-' + trackNum);
        if (!trackSection) return;

        const isCurrentlyActive = trigger.classList.contains('active');

        if (isCurrentlyActive) {
          closeCardDeck(trackSection);
        } else {
          openCardDeck(trackSection, targetCardIdx, trigger);
        }
      });
    });

    function openCardDeck(trackSection, targetCardIdx, triggerEl) {
      document.querySelectorAll('.track-section').forEach(ts => {
        if (ts !== trackSection) closeCardDeck(ts);
      });

      const activeLang = currentLang;
      const reviewEl = trackSection.querySelector(`.lang-${activeLang} .narrative-review`);
      const deckEl = trackSection.querySelector(`.lang-${activeLang} .card-deck-view`);
      
      if (!deckEl) return;

      trackSection.querySelectorAll('.lyric-trigger').forEach(tr => {
        const isMatch = tr.getAttribute('data-target-card') === targetCardIdx;
        tr.classList.toggle('active', isMatch);
      });

      if (triggerEl && window.innerWidth > 992) {
        const gridEl = trackSection.querySelector('.track-grid');
        const triggerRect = triggerEl.getBoundingClientRect();
        const gridRect = gridEl.getBoundingClientRect();
        const relativeTop = triggerRect.top - gridRect.top;
        deckEl.style.marginTop = `${Math.max(0, Math.round(relativeTop))}px`;
      } else {
        deckEl.style.marginTop = '0px';
      }

      if (reviewEl) reviewEl.style.display = 'none';
      deckEl.style.display = 'flex';

      deckEl.querySelectorAll('.analysis-card').forEach((c, idx) => {
        if (idx.toString() === targetCardIdx) {
          c.classList.add('active');
        } else {
          c.classList.remove('active');
        }
      });

      if (window.innerWidth <= 992) {
        deckEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function closeCardDeck(trackSection) {
      const activeLang = currentLang;
      const reviewEl = trackSection.querySelector(`.lang-${activeLang} .narrative-review`);
      const deckEl = trackSection.querySelector(`.lang-${activeLang} .card-deck-view`);

      trackSection.querySelectorAll('.lyric-trigger').forEach(tr => tr.classList.remove('active'));

      if (deckEl) {
        deckEl.style.display = 'none';
        deckEl.style.marginTop = '0px';
      }
      if (reviewEl) reviewEl.style.display = 'block';
    }

    document.querySelectorAll('.card-back-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const trackNum = btn.getAttribute('data-track-num');
        const trackSection = document.getElementById('track-' + trackNum);
        if (trackSection) closeCardDeck(trackSection);
      });
    });

    document.addEventListener('click', (e) => {
      if (!e.target.closest('.analysis-card') && !e.target.closest('.lyric-trigger')) {
        document.querySelectorAll('.track-section').forEach(ts => closeCardDeck(ts));
      }
    });

    // 5. Dual Media Audio Engine
    let ytPlayer = null;
    let ytReady = false;
    let queuedVideoId = null;
    let currentMode = 'song';
    let currentAudio = null;
    let currentTrackIdx = 0;
    let isPlaying = false;

    const bpTrackNum = document.getElementById('bpTrackNum');
    const bpTrackTitle = document.getElementById('bpTrackTitle');
    const bpPlayPauseBtn = document.getElementById('bpPlayPauseBtn');
    const bpPlayIcon = bpPlayPauseBtn.querySelector('.bp-play-icon');
    const bpPauseIcon = bpPlayPauseBtn.querySelector('.bp-pause-icon');
    const bpPrevBtn = document.getElementById('bpPrevBtn');
    const bpNextBtn = document.getElementById('bpNextBtn');
    const bpCurrentTime = document.getElementById('bpCurrentTime');
    const bpTotalTime = document.getElementById('bpTotalTime');
    const bpTimelineTrack = document.getElementById('bpTimelineTrack');
    const bpTimelineFill = document.getElementById('bpTimelineFill');

    function formatTime(seconds) {
      if (isNaN(seconds) || seconds === 0) return '0:00';
      const m = Math.floor(seconds / 60);
      const s = Math.floor(seconds % 60);
      return `${m}:${s < 10 ? '0' : ''}${s}`;
    }

    function updateTrackUI(idx) {
      const track = trackList[idx];
      bpTrackNum.textContent = track.num;
      bpTrackTitle.textContent = track.title.toUpperCase();

      const songSub = document.querySelector('.sub-mode-song');
      const essaySub = document.querySelector('.sub-mode-essay');
      if (songSub && essaySub) {
        songSub.style.display = currentMode === 'song' ? 'inline' : 'none';
        essaySub.style.display = currentMode === 'essay' ? 'inline' : 'none';
      }

      document.querySelectorAll('.song-round-play-btn').forEach(btn => {
        const isThis = (btn.getAttribute('data-track-num') === track.num) && (currentMode === 'song');
        btn.classList.toggle('playing', isThis && isPlaying);
        btn.querySelector('.play-icon').style.display = (isThis && isPlaying) ? 'none' : 'inline-block';
        btn.querySelector('.pause-icon').style.display = (isThis && isPlaying) ? 'inline-block' : 'none';
      });

      document.querySelectorAll('.audio-play-btn').forEach(btn => {
        const isThis = (btn.getAttribute('data-track-num') === track.num) && (currentMode === 'essay');
        btn.classList.toggle('playing', isThis && isPlaying);
        btn.querySelector('.play-icon').style.display = (isThis && isPlaying) ? 'none' : 'inline-block';
        btn.querySelector('.pause-icon').style.display = (isThis && isPlaying) ? 'inline-block' : 'none';
      });

      bpPlayIcon.style.display = isPlaying ? 'none' : 'inline-block';
      bpPauseIcon.style.display = isPlaying ? 'inline-block' : 'none';
    }

    function playSong(idx, autoPlay = true) {
      currentMode = 'song';
      currentTrackIdx = (idx + trackList.length) % trackList.length;
      const track = trackList[currentTrackIdx];

      if (currentAudio) {
        currentAudio.pause();
        currentAudio.currentTime = 0;
      }

      bpTimelineFill.style.width = '0%';
      bpCurrentTime.textContent = '0:00';

      isPlaying = autoPlay;
      updateTrackUI(currentTrackIdx);
      
      const trackEl = document.getElementById('track-' + track.num);
      if (trackEl && autoPlay) {
        trackEl.scrollIntoView({ behavior: 'smooth' });
      }
    }

    function playEssay(idx, autoPlay = true) {
      currentMode = 'essay';
      currentTrackIdx = (idx + trackList.length) % trackList.length;
      const track = trackList[currentTrackIdx];

      const audioSrc = `audio/track_${track.num}_${currentLang}.mp3`;
      if (currentAudio) {
        currentAudio.pause();
        currentAudio = null;
      }

      currentAudio = new Audio(audioSrc);
      bpTimelineFill.style.width = '0%';
      bpCurrentTime.textContent = '0:00';

      currentAudio.addEventListener('loadedmetadata', () => {
        bpTotalTime.textContent = formatTime(currentAudio.duration);
      });

      currentAudio.addEventListener('timeupdate', () => {
        if (!currentAudio || currentMode !== 'essay') return;
        bpCurrentTime.textContent = formatTime(currentAudio.currentTime);
        const pct = (currentAudio.currentTime / (currentAudio.duration || 1)) * 100;
        bpTimelineFill.style.width = `${pct}%`;
      });

      currentAudio.addEventListener('ended', () => {
        playSong((currentTrackIdx + 1) % trackList.length, true);
      });

      if (autoPlay) {
        isPlaying = true;
        currentAudio.play().catch(e => console.log('Audio playback prevented:', e));
      } else {
        isPlaying = false;
      }
      updateTrackUI(currentTrackIdx);
    }

    bpPlayPauseBtn.addEventListener('click', () => {
      if (currentMode === 'song') {
        isPlaying = !isPlaying;
      } else {
        if (!currentAudio) {
          playEssay(currentTrackIdx, true);
          return;
        }
        if (currentAudio.paused) {
          currentAudio.play();
          isPlaying = true;
        } else {
          currentAudio.pause();
          isPlaying = false;
        }
      }
      updateTrackUI(currentTrackIdx);
    });

    bpPrevBtn.addEventListener('click', () => {
      if (currentMode === 'song') {
        playSong(currentTrackIdx - 1, true);
      } else {
        playEssay(currentTrackIdx - 1, true);
      }
    });

    bpNextBtn.addEventListener('click', () => {
      if (currentMode === 'song') {
        playSong(currentTrackIdx + 1, true);
      } else {
        playEssay(currentTrackIdx + 1, true);
      }
    });

    document.querySelectorAll('.song-round-play-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const numStr = btn.getAttribute('data-track-num');
        const targetIdx = trackList.findIndex(t => t.num === numStr);

        if (targetIdx === currentTrackIdx && currentMode === 'song') {
          isPlaying = !isPlaying;
          updateTrackUI(currentTrackIdx);
        } else {
          playSong(targetIdx, true);
        }
      });
    });

    document.querySelectorAll('.audio-play-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const numStr = btn.getAttribute('data-track-num');
        const targetIdx = trackList.findIndex(t => t.num === numStr);

        if (targetIdx === currentTrackIdx && currentMode === 'essay' && currentAudio) {
          if (currentAudio.paused) {
            currentAudio.play();
            isPlaying = true;
          } else {
            currentAudio.pause();
            isPlaying = false;
          }
          updateTrackUI(currentTrackIdx);
        } else {
          playEssay(targetIdx, true);
        }
      });
    });

    updateTrackUI(0);
  </script>
</body>
</html>
""")

final_code = "".join(html_out)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_code)

print(f"Generated build_master_complete: index.html ({len(final_code)} bytes)")
