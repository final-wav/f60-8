# -*- coding: utf-8 -*-
import json
import re

# Load complete Genius lyrics
with open('full_genius_lyrics.json', 'r', encoding='utf-8') as f:
    raw_lyrics = json.load(f)

# Load CSS from tomora_index.html and adapt color variables to exact cover orange
with open('tomora_index.html', 'r', encoding='utf-8') as f:
    tomora_content = f.read()

style_start = tomora_content.find('<style>')
style_end = tomora_content.find('</style>')
tomora_css = tomora_content[style_start+7:style_end]

# Replace magenta theme colors with cover orange #fa5b00
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

tracks_data = [
    {
        "num": "01",
        "title": "1996",
        "key_triggers": [
            ("Panoramablick übers Paradies", 0),
            ("Während warme Luft auf dem Garten liegt", 0),
            ("Etwas fehlt, vielleicht ist es aufgewacht", 1),
            ("Das Gegenteil, das Außerhalb", 1),
            ("Denn wie man sich bettet, so liegt man", 2),
            ("Wie man sich fesselt, so flieht man", 2),
            ("Und ich zieh' an der Kippe, der Rauch steigt", 3),
            ("Auf in den Himmel von Ibiza", 3)
        ],
        "review_de": """<p>Das Album eröffnet nicht mit einer versöhnlichen Rückschau, sondern mit dem Schnitt einer Rasierklinge: <strong>„1996“</strong> fungiert als Exposition und biografische Sollbruchstelle. Eingerahmt von den fiktiven Radiosendern von <em>Ego FM Ibiza</em> betritt der Protagonist die Bühne einer künstlichen Mittelmeer-Traumwelt, in der jede Erinnerung an die provinzielle Enge durch puren kinetischen Antrieb ausgelöscht werden soll.</p>
<p>Die klangliche Architektur etabliert sofort das Leitmotiv des Projekts: Der Ikarus-Mythos. Der <span class="lyric-quote-highlight">Panoramablick übers Paradies</span> ist kein Ort der Kontemplation, sondern die Startrampe für den kontrollierten Absturz. Mit der schneidenden Formel <span class="lyric-quote-highlight">„Wie man sich fesselt, so flieht man“</span> wird Bindung von vornherein als Gefängnis deklariert, das nur durch Flucht und Betäubung im <span class="lyric-quote-highlight">Himmel von Ibiza</span> ertragen werden kann.</p>""",
        "review_en": """<p>The album opens not with nostalgic contemplation, but with the clean slice of a scalpel: <strong>“1996”</strong> operates as both sonic prologue and psychological fault line. Framed by broadcasts from the fictional station <em>Ego FM Ibiza</em>, the protagonist steps onto the synthetic Mediterranean stage where all provincial memories are incinerated through sheer velocity.</p>
<p>The sonic architecture immediately establishes the central motif: the Icarus ascent. The <span class="lyric-quote-highlight">panoramic view over paradise</span> is no sanctuary, but the staging ground for a controlled descent. Through the cutting aphorism <span class="lyric-quote-highlight">“The way you bind yourself is the way you flee”</span>, intimacy is pre-emptively coded as imprisonment, survivable only through evasion into the <span class="lyric-quote-highlight">Ibiza sky</span>.</p>""",
        "cards_de": [
            {
                "quote": "Panoramablick übers Paradies / Die künstliche Idylle & der Fluchtpunkt",
                "body": """Die Inszenierung des Luxus-Panoramas dient als hermetische Barriere gegen frühe Ohnmachts- und Mangelgefühle. Das Paradies ist kein Ort der Entspannung, sondern ein manisch errichtetes Bühnenbild.

Erhöhter Muskeltonus im Nackenbereich, fixierter Weitblick über das Meer und eine flache thorakale Atmung halten das vegetative Nervensystem in dauerhafter Alarmbereitschaft. Wer von oben herabblickt, kann nicht überrascht, bewertet oder verletzt werden.

Schwebende, warme Synthesizer-Pads werden unvermittelt von treibenden 2-Step-Breakbeats durchbrochen und erzeugen ein Gefühl von Vorwärtsflucht."""
            },
            {
                "quote": "Das Gegenteil, das Außerhalb / Das Erwachen des Mangels",
                "body": """Trotz maximaler äußerer Reizüberflutung bricht die innere Leere („das Außerhalb“) durch. Der narzisstische Triumph scheitert an der Unfähigkeit, innere Ruhe zu empfinden.

Das Erstarren der Gesichtszüge und ein innerer Kälteschauer trotz warmer Mittelmeerluft verraten den Kontrollverlust über die eigenen Affekte. Das Unbewusste meldet sich als unkontrollierbarer Fremdkörper an.

Frequenzbeschnittene Hallräume machen das Gefühl von Kapselung und plötzlich einsetzender Isolation auditiv unmittelbar spürbar."""
            },
            {
                "quote": "Wie man sich fesselt, so flieht man / Die Bindungs-Dialektik",
                "body": """Bindungsphobische Vorwegnahme des Scheiterns: Nähe wird als unerträgliche Fesselung erlebt, sodass der Fluchtreflex bereits vor Beginn der Beziehung aktiviert wird.

Rückzug der Schultern, Ausweichen von direktem Blickkontakt und motorischer Vorwärtsdrang sichern die Autonomie-Behauptung durch Beziehungsabbruch. Wer zuerst geht, behält die Kontrolle über das Narrativ.

Trockene, schneidende Snare-Schläge im Verbund mit staccatoartigen Vocals treiben den Vers voran."""
            },
            {
                "quote": "Himmel von Ibiza / Dissipation & Hedonismus",
                "body": """Nikotin und Insel-Hedonismus fungieren als Desensibilisierungswerkzeuge. Der Rauch legt sich als Schleier zwischen das Selbst und die Realität.

Tiefes, forciertes Inhalieren, gefolgt von demonstrativ verlangsamtem Ausatmen: Gelassenheit wird mimisch forciert, nicht organisch erlebt, um Gleichgültigkeit gegenüber dem sozialen Umfeld zu demonstrieren.

Ausfasernde Delay-Fahnen auf den Gesangsspuren lassen den Raum und das dissoziierende Bewusstsein ineinanderfließen."""
            }
        ],
        "cards_en": [
            {
                "quote": "Panoramic view over paradise / The Synthetic Sanctuary",
                "body": """The staging of the panoramic luxury retreat serves as a hermetic defense against early helplessness. Paradise is not a haven but an adrenaline-fueled set piece.

Elevated cervical muscle tone, a fixated horizon stare, and shallow thoracic breathing sustain chronic sympathetic arousal. Overlooking the scene prevents vulnerability to external judgment.

Lush, warm ambient synthesizer pads are abruptly intersected by driving garage breakbeats, propelling the protagonist into perpetual forward flight."""
            },
            {
                "quote": "The opposite, the outside / The Void Awakes",
                "body": """Despite the saturation of external stimuli, chronic internal void breaks through. Narcissistic grandiosity fractures against the inability to sustain peace.

A sudden facial freeze and micro-shivers despite the warm Mediterranean air betray a loss of affective mastery. The repressed material returns as an uncontrollable intrusion.

High-pass filtered reverb decays simulate sudden psychological encapsulation across the acoustic field."""
            },
            {
                "quote": "The way you bind yourself is the way you flee / Attachment Dialectics",
                "body": """The avoidant attachment schema in full force: closeness is registered as suffocation, triggering the escape protocol before intimacy can consolidate.

Shoulder retraction, gaze evasion, and restless kinetic locomotion preserve sovereignty via pre-emptive abandonment. He who exits first dictates terms.

Dry, cutting snare transients synchronize with staccato vocal delivery to underscore the refusal to settle."""
            },
            {
                "quote": "Ibiza Sky / Dissipation and Hedonism",
                "body": """Nicotine and island hedonism deployed as chemical insulation. Smoke functions as an optical barrier between the self and emotional reality.

Forced deep inhalation followed by exaggerated exhalation performs composure rather than experiencing it, signaling total emotional detachment from surroundings.

Wide stereo delay tails diffuse vocal presence into the shimmering Mediterranean soundscape."""
            }
        ]
    },
    {
        "num": "02",
        "title": "Wiedersehen",
        "key_triggers": [
            ("Draußen alles voller Pinien", 0),
            ("Drinnen alles voller Linien", 0),
            ("Vergessen, wie ich dich liebe", 1),
            ("Es gibt keine Romantik, es gibt nur noch Triebe", 1),
            ("Die Welt gehört denen, die sie sich nehmen", 2),
            ("Ich steh' auf einer Fähre übers Mittelmeer", 3),
            ("Seh' der weißen Spur im Wasser hinterher", 3),
            ("Selig sind die Diebe", 3),
            ("Ich nehme, was ich kriege", 3)
        ],
        "review_de": """<p>In <strong>„Wiedersehen“</strong> vollzieht der Protagonist den maritimen Transit und formuliert zugleich sein rücksichtsloses Credo. Auf der Fähre übers Mittelmeer stehend, blickt er auf das schäumende Kielwasser – ein kraftvolles Symbol für die Vergänglichkeit und Austauschbarkeit aller hinterlassenen Bindungen.</p>
<p>Die Antithese <span class="lyric-quote-highlight">„Draußen alles voller Pinien / Drinnen alles voller Linien“</span> bringt das bipolare Spannungsfeld des Albums auf den Punkt: Die unberührte Naturidylle wird im Innenraum durch chemische Kokain-Linien brutal überformt. Mit der schneidenden Formel <span class="lyric-quote-highlight">„Selig sind die Diebe / Ich nehme, was ich kriege“</span> pervertiert Tua die biblische Bergpredigt in ein Manifest räuberischer Autarkie.</p>""",
        "review_en": """<p>In <strong>“Wiedersehen”</strong> (Reunion / Parting), maritime transit crystallizes into an explicit predator manifesto. Standing on the ferry across the Mediterranean, the speaker watches the churning wake—a pristine metaphor for the ephemerality of discarded intimacy.</p>
<p>The antithesis <span class="lyric-quote-highlight">“Outside full of pine trees / Inside full of lines”</span> encapsulates the album's core tension: untouched natural serenity is chemically reorganized by cocaine on glass tables. Through the inversion <span class="lyric-quote-highlight">“Blessed are the thieves / I take what I get”</span>, Tua subverts the Sermon on the Mount into an ethic of unapologetic extraction.</p>""",
        "cards_de": [
            {
                "quote": "Pinien & Linien / Naturidylle vs. Chemische Raserei",
                "body": """Spaltung zwischen äußerer Naturromantik und innerer chemischer Zerrüttung: Die Pinien symbolisieren das unerreichbare organische Leben, die Linien den verzweifelten Versuch künstlicher Selbstregulation.

Geweitete Pupillen, Trockenheit im Mundraum und eine angespannte Kiefermuskulatur unterlaufen die krampfhaft ruhige Außenhaltung. Die Umwelt wird dem chemischen Regime unterworfen.

Scharfe, metallische Percussions und trockene Bass-Impulse stehen im brutalen Kontrast zu verwehten Gitarren-Samples."""
            },
            {
                "quote": "Vergessen, wie ich dich liebe / Reduktion auf den Trieb",
                "body": """Vollständige Abspaltung von Empathie und emotionaler Bindung: Indem Liebe auf reine Triebbefriedigung reduziert wird, entledigt sich das Ich jeglicher moralischer Verantwortung.

Kalter, unbewegter Blick; das Gesicht verliert seine mimische Resonanzfähigkeit (Affektverflachung). Der Partner wird zur reinen narzisstischen Zufuhr instrumentalisiert.

Eine trockene, monotone Gesangslinie ohne natürliches Vibrato bildet die emotionale Taubheit klanglich exakt ab."""
            },
            {
                "quote": "Die Welt gehört denen, die sie sich nehmen / Das Raubtier-Dogma",
                "body": """Sozialdarwinistische Rationalisierung: Das Ich rechtfertigt seine Ausbeutungsmuster als universelles Lebensgesetz, um Schuldgefühle im Vorfeld zu neutralisieren.

Fester Stand gegen den Seegang, geschwellte Brust, zusammengebissene Zähne: Eine Omnipotenzfantasie, die als Schutzwall vor der existentiellen Belanglosigkeit errichtet wird.

Ein wuchtiger Subbass okkupiert das akustische Zentrum und duldet keinen Widerspruch."""
            },
            {
                "quote": "Selig sind die Diebe / Das Transit-Manifest",
                "body": """Blasphemische Umwertung christlicher Demut: Der Diebstahl von Gefühlen und Ressourcen wird zum heiligen Akt der Selbsterhaltung stilisiert.

Blick nach hinten auf die schäumende Heckwelle, Hände tief in den Jackentaschen vergraben, abgewandter Körper: Die absolute Verweigerung von Gegenseitigkeit wird zur Überlebensstrategie erhoben.

Anschwellendes Meeresrauschen gemischt mit tiefen, abebbenden Synth-Drones markiert den unwiderruflichen Abschied."""
            }
        ],
        "cards_en": [
            {
                "quote": "Pine Trees & Lines / Organic Serenity vs Chemical Velocity",
                "body": """Splitting between exterior idyllic nature and internal chemical dysregulation: pine trees represent unreachable organic peace; cocaine lines represent forced affective control.

Mydriasis, xerostomia, and hypertonic masseter muscles lurk behind a deliberately rigid neutral posture. Sensory reality is subordinated to the chemical timetable.

Sharp, metallic percussive transients clash violently with distant acoustic guitar motifs."""
            },
            {
                "quote": "Forgot how I love you / Drive Reduction",
                "body": """Total dissociation of empathy: by reducing complex love to animal drive, the ego exempts itself from ethical accountability.

Flat affect, unblinking ocular focus, and the complete absence of prosodic warmth in speech. The relational partner is objectified into pure narcissistic supply.

A monotone, bone-dry vocal staging stripped of natural vibrato sonically mirrors emotional deadness."""
            },
            {
                "quote": "The world belongs to those who take it / Predator Ethos",
                "body": """Social-darwinist rationalization: the ego reframes relational exploitation as universal law to inoculate against guilt.

An anchored stance against ferry sway, expanded thoracic cage, and clenched jawline project an omnipotence fantasy against underlying insignificance.

Heavy sub-bass saturation claims the acoustic center, rejecting all vulnerability."""
            },
            {
                "quote": "Blessed are the thieves / Transit Manifesto",
                "body": """Blasphemous subversion of spiritual beatitudes: emotional theft is canonized as sacred self-preservation.

Gaze locked on the churning white wake, hands buried in coat pockets, posture turned away from land: absolute rejection of reciprocity as a defensive stance.

Churning marine white noise blended into decaying low-frequency drone sweeps seals the departure."""
            }
        ]
    },
    {
        "num": "03",
        "title": "GluiV",
        "key_triggers": [
            ("G, Louis V, Bauchtasche, Kokain", 0),
            ("Weil du mich kennst, doch weißt du, wer ich bin?", 1),
            ("Wenn ich's dir sag', kriegst du's nicht mehr aus dem Sinn", 1),
            ("Du willst mich seh'n, aber ich bin nicht zu Hause", 2),
            ("Ich bin auf der Jagd und du bist meine Beute", 2),
            ("Eiskaltes Händchen, eiskalter Blick", 3),
            ("Ich mach' einen Schritt vor und drei zurück", 3)
        ],
        "review_de": """<p><strong>„GluiV“</strong> dekonstruiert die Inszenierungsmechanismen des modernen Rap-Materialismus. Hinter der phonetischen Formel <span class="lyric-quote-highlight">„G, Louis V, Bauchtasche, Kokain“</span> verbirgt sich kein plumper Statushunger, sondern eine rigide Rüstung aus Markensymbolen und chemischer Betäubung.</p>
<p>Die Beziehungsdynamik schlägt hier unverhohlen in offene Prädation um: <span class="lyric-quote-highlight">„Du willst mich seh'n, aber ich bin nicht zu Hause / Ich bin auf der Jagd und du bist meine Beute“</span>. Tua zeichnet das Bild eines emotionalen Vampirismus, der im ständigen <span class="lyric-quote-highlight">„Schritt vor und drei zurück“</span> Nähe verspricht, nur um sie im Moment der Auslieferung grausam zu verweigern.</p>""",
        "review_en": """<p><strong>“GluiV”</strong> deconstructs the staging mechanisms of contemporary rap materialism. Behind the phonetic shorthand <span class="lyric-quote-highlight">“G, Louis V, waist bag, cocaine”</span> lies no simple luxury worship, but a rigid psychological armor forged from luxury markers and chemical insulation.</p>
<p>Relational dynamics mutate openly into predation: <span class="lyric-quote-highlight">“You want to see me, but I'm not at home / I am on the hunt and you are my prey”</span>. Tua portrays an emotional vampirism that perpetually executes <span class="lyric-quote-highlight">“one step forward and three steps back”</span>—luring the partner with the promise of intimacy only to revoke it upon surrender.</p>""",
        "cards_de": [
            {
                "quote": "G, Louis V, Bauchtasche, Kokain / Die Rüstung der Symbole",
                "body": """Luxusgüter und Drogenkonsum als fetischistische Rüstung: Das fragile Selbst tarnt seine Verwundbarkeit durch Symbole unantastbarer Vormachtstellung und sozialer Distanzierung.

Schnelle, ruckartige Kopfbewegungen, nervöses Abtasten der Taschen und permanente Raumkontrolle spiegeln die innere Alarmbereitschaft wider.

Aggressive 808-Bässe, scharfe Trap-Hi-Hats und zerhackte Vokal-Loops schaffen eine kalte, bedrohliche Club-Ästhetik."""
            },
            {
                "quote": "Weißt du, wer ich bin? / Die verbotene Wahrheit",
                "body": """Panische Angst vor emotionaler Entblößung: Der Protagonist droht mit dem eigenen Abgrund, um das Gegenüber auf sicherer Distanz zu halten.

Intensiver, bedrohlicher Blickkontakt, leicht vorgeneigter Oberkörper und eine gedämpfte, raue Stimme schüchtern den Partner ein („Wenn ich's dir sag', kriegst du's nicht mehr aus dem Sinn“).

Gespenstische Pitch-Down-Effekte auf den Backing Vocals erzeugen eine unheimliche psychologische Raumtiefe."""
            },
            {
                "quote": "Jagd und Beute / Prädatorische Intimität",
                "body": """Verkehrung von Zuwendung in Jagdverhalten: Intimität wird als Machtkampf inszeniert, bei dem Unterwerfung die einzige akzeptierte Währung darstellt.

Raubtierhafter Gang, geschärfte Sinne und die Vermeidung von Berührungen abseits des sexuellen oder machtbezogenen Kontexts sichern die absolute Kontrolle über das Nähe-Distanz-Gefälle.

Tief grollende Bassläufe übersetzen das Gefühl eines sich unerbittlich schließenden Netzes in Klang."""
            },
            {
                "quote": "Eiskaltes Händchen / Schritt vor, drei zurück",
                "body": """Intermittierende Verstärkung und Bindungstraumatisierung: Das ständige Vor- und Zurückweichen hält das Gegenüber in permanenter emotionaler Abhängigkeit gefangen.

Kalte Peripherie (Hände/Füße) durch chronische Vasokonstriktion unter Stimulanzien, gepaart mit abruptem körperlichen Abwenden nach flüchtiger Zuwendung.

Stotternde Arpeggiatoren und Synkopen spiegeln rhythmisch die unberechenbare Sprunghaftigkeit des Protagonisten wider."""
            }
        ],
        "cards_en": [
            {
                "quote": "Louis V, Waist Bag, Cocaine / The Fetish Armor",
                "body": """Brand signifiers and narcotics functioning as armor: the fragile self shields against collapse by embodying impenetrable invulnerability and status boundaries.

Rapid saccadic head movements, repetitive checking of accessories, and hyper-vigilant scanning of the room reflect underlying sympathetic arousal.

Aggressive 808 sub-transients, slicing trap hi-hat rolls, and chopped vocal hooks create an icy, menacing club perimeter."""
            },
            {
                "quote": "Do you know who I am? / The Poisonous Core",
                "body": """Panic before genuine emotional exposure: the speaker threatens the partner with his destructive interior to maintain relational distance.

A piercing unyielding gaze, torso inclined forward, and a raspy dropped vocal register intimidate the partner into retreat.

Pitch-shifted backing doubles create an ominous, uncanny stereo spread across the acoustic space."""
            },
            {
                "quote": "Hunter & Prey / Predatory Intimacy",
                "body": """Eroticization of dominance: attachment is reframed as a predator-prey transaction where submission is demanded.

Prowling kinetic locomotion, heightened auditory reflexes, and calculated touch ensure unilateral control over relational access.

Resonant low-end rumbles sonically simulate an enclosing psychological trap."""
            },
            {
                "quote": "Ice cold hand / One step forward, three steps back",
                "body": """Intermittent reinforcement schedule: alternating between warm allure and glacial rejection engineers acute trauma bonding.

Peripheral vasoconstriction (freezing hands) from stimulant load pairs with abrupt physical disengagement following intimacy.

Stuttering arpeggiator figures and syncope breaks echo the structural instability of the persona."""
            }
        ]
    },
    {
        "num": "04",
        "title": "Dachterrasse",
        "key_triggers": [
            ("Steh' auf der Dachterrasse", 0),
            ("Was ich hier oben mache? Weiß ich schon lange nicht mehr", 0),
            ("Du sagst, ich soll runterkommen, doch ich kann nicht", 1),
            ("Weil mich da unten die Einsamkeit auffrisst", 1),
            ("Jeder Schritt ein Risiko, jeder Blick ein Verhör", 2),
            ("Bin gefangen in mei'm Kopf, während der Bass dröhnt", 2)
        ],
        "review_de": """<p><strong>„Dachterrasse“</strong> ist das klangliche Äquivalent eines Schwindelanfalls auf 50 Metern Höhe. Der Protagonist blickt vom Dach eines Luxusgebäudes auf das nächtliche Lichtermeer herab – isoliert, betäubt und unfähig zur Erdung.</p>
<p>Die Zeilen <span class="lyric-quote-highlight">„Du sagst, ich soll runterkommen, doch ich kann nicht / Weil mich da unten die Einsamkeit auffrisst“</span> demaskieren den Höhenrausch als reine Panik vor der alltäglichen Normalität. Auf der Höhe herrscht Kälte, doch der Abstieg bedeutet die unausweichliche Konfrontation mit der eigenen emotionalen Verwahrlosung.</p>""",
        "review_en": """<p><strong>“Dachterrasse”</strong> (Rooftop) is the acoustic equivalent of vertigo at fifty meters elevation. The protagonist looks down upon the shimmering nocturnal grid—detached, anesthetized, and incapable of descending to sea level.</p>
<p>The plea <span class="lyric-quote-highlight">“You tell me to come down, but I can't / Because down there, loneliness devours me”</span> exposes the altitude addiction as pure terror of domestic reality. The summit is freezing, yet the descent implies immediate confrontation with emotional bankruptcy.</p>""",
        "cards_de": [
            {
                "quote": "Dachterrasse & Lichtermeer / Der isolierte Aussichtspunkt",
                "body": """Räumliche Überhöhung als Metapher für narzisstische Abkapselung: Die Höhe garantiert Sicherheit vor unkontrollierten zwischenmenschlichen Kontakten auf Augenhöhe.

Schwindelgefühl (Vertigo), Festhalten am Geländer mit weißen Fingerknöcheln und vibrierende Brustmuskeln durch den von unten heraufdröhnenden Bass.

Weite Hallräume mit Tiefpassfilter lassen die Clubmusik von der Straße dumpf heraufschallen und verstärken das Gefühl absoluter Isolation."""
            },
            {
                "quote": "Ich kann nicht runterkommen / Angst vor der Erdung",
                "body": """Phobische Angst vor dem Absturz in die nüchterne depressive Leere: Die „Einsamkeit da unten“ steht für die reale, ungeschönte Lebenswirklichkeit ohne Rausch und Applaus.

Schüttelfrost und die vegetative Dissonanz zwischen Kälteempfinden und schweißnassen Handflächen begleiten die Verweigerung von Hilfsangeboten.

Scharf akzentuierte Synthesizer-Lead-Lines schneiden wie Alarmsignale durch den Raum."""
            },
            {
                "quote": "Blick ein Verhör / Paranoide Hypervigilanz",
                "body": """Projektion eigener Schuld- und Schamgefühle auf die Umwelt: Jeder Blick wird als feindlicher Entlarvungsversuch und polizeiliches Verhör interpretiert.

Flackernder Blick, Anspannung der Trapezmuskeln und ständiges Drehen des Kopfes zur Seite sichern die vorbeugende Aggression gegen Beobachter.

Komprimierte Bass-Stöße und beklemmende Panorama-Effekte schaffen eine klaustrophobische Atmosphäre im Kopf des Protagonisten."""
            }
        ],
        "cards_en": [
            {
                "quote": "Rooftop & Sea of Lights / The Solitary Vantage",
                "body": """Spatial elevation as a physical correlate of narcissistic detachment: altitude guarantees immunity from intimate encounters at eye level.

Vertigo, a white-knuckled grip on the balcony railing, and chest wall vibration from bass frequencies booming from below.

Expansive stereo reverb with low-pass filtering captures the muffled club bass thumping from ground level, amplifying isolation."""
            },
            {
                "quote": "I can't come down / Grounding Phobia",
                "body": """Phobic dread of crashing into baseline depressive emptiness: 'loneliness down there' represents sober, unvarnished existence without chemical elevation.

Shivering and autonomic dissonance between cold skin and clammy palms accompany the refusal of rescue.

Searing synthesizer leads slice across the frequency field like siren alarms in the night sky."""
            },
            {
                "quote": "Every glance an interrogation / Paranoid Hypervigilance",
                "body": """Projection of internal shame onto external observers: every neutral glance is decoded as an investigative intrusion.

Rapid ocular shifts, hypertonicity of trapezius muscles, and constant peripheral scanning drive pre-emptive hostility against perceived surveillance.

Compressed sub transients and claustrophobic stereo panning mimic the tightening grip of acute paranoia."""
            }
        ]
    },
    {
        "num": "05",
        "title": "Für mich",
        "key_triggers": [
            ("Ich mach' das alles nur für mich", 0),
            ("Sag mir, warum siehst du mich nicht?", 0),
            ("Du willst, dass ich mich ändere, doch ich bin perfekt", 1),
            ("In meiner eigenen Welt, die du nicht verstehst", 1),
            ("Und wenn ich falle, dann fall' ich allein", 2),
            ("Weil niemand es wert ist, bei mir zu sein", 2)
        ],
        "review_de": """<p><strong>„Für mich“</strong> führt tief in den Kern der narzisstischen Verwundung. Was als trotzige Autonomie-Erklärung beginnt (<span class="lyric-quote-highlight">„Ich mach' das alles nur für mich“</span>), kippt unmittelbar in die klagende Frage: <span class="lyric-quote-highlight">„Sag mir, warum siehst du mich nicht?“</span>.</p>
<p>Hier zeigt sich das unlösbare Dilemma der Persönlichkeitsstörung: Der Zwang zur absoluten Selbstgenügsamkeit kollidiert frontal mit dem quälenden Hunger nach Bestätigung und Spiegelung durch das Gegenüber. Das Beharren auf der eigenen Perfektion ist nichts als eine verzweifelte Brandmauer gegen das Gefühl existenzieller Wertlosigkeit.</p>""",
        "review_en": """<p><strong>“Für mich”</strong> (For Myself) cuts straight to the core of narcissistic injury. What initiates as a defiant declaration of self-sufficiency (<span class="lyric-quote-highlight">“I do all this only for myself”</span>) instantaneously collapses into the desperate plea: <span class="lyric-quote-highlight">“Tell me, why don't you see me?”</span>.</p>
<p>Here lies the insoluble dilemma: the compulsory mandate of absolute self-reliance violently collides with a voracious craving for external validation. Insisting on one's own perfection is merely a desperate firewall safeguarding against deep existential shame.</p>""",
        "cards_de": [
            {
                "quote": "Alles nur für mich / Warum siehst du mich nicht?",
                "body": """Die klassische narzisstische Paradoxie: Autarkie-Behauptung bei gleichzeitiger totaler Abhängigkeit vom spiegelnden Blick des Anderen. Das Nicht-Gesehen-Werden löst schwere Kränkung aus.

Krampfhafte Selbstumarmung, Heben der Stimme bis zum Überschlagen und unruhige Hyperventilation begleiten die vorwurfsvolle Umkehr der Täter-Opfer-Rolle.

Ein intimer E-Piano-Akkord wird unvermittelt von harten, schneidenden Vocals durchbrochen."""
            },
            {
                "quote": "Ich bin perfekt in meiner Welt / Grandiose Abkapselung",
                "body": """Grandiose Selbstüberhöhung als Schutzwall gegen Kritik: Jede Aufforderung zur Veränderung wird als feindlicher Vernichtungsversuch abgewehrt.

Starre Kopfhaltung, abfälliges Lächeln und hochgezogene Augenbrauen entwerten den Partner („du verstehst das nicht“), um die kognitive Überlegenheit zu sichern.

Monotone Synthesizer-Flächen erzeugen eine hermetische, künstliche Klangblase ohne Außengeräusche."""
            },
            {
                "quote": "Wenn ich falle, dann allein / Niemand ist es wert",
                "body": """Heroisierung der eigenen Isolation: Der Zusammenbruch wird zum exklusiven Monopol erklärt, um niemandem Dankbarkeit oder Verletzlichkeit schuldig zu sein.

Schließen der Augen, Abwenden des Oberkörpers vom Gegenüber und das Absinken der Schultern inszenieren Verachtung als letzten Rettungsanker des Ego.

Vereinzelte, hallüberladene Pianonoten schweben einsam im leeren Frequenzraum."""
            }
        ],
        "cards_en": [
            {
                "quote": "All for myself / Why don't you see me?",
                "body": """Classic narcissistic paradox: proclamation of total self-reliance coexisting with frantic dependency on external mirroring. Being unseen triggers acute shame.

Defensive self-clasping posture, vocal cracking at higher registers, and agitated hyperventilation drive the blaming inversion where the self is cast as victim.

An intimate electric piano chord is violently interrupted by aggressive dry vocal cuts."""
            },
            {
                "quote": "I am perfect in my world / Grandiose Isolation",
                "body": """Grandiose inflation deployed as a fortress against critique: any request for behavioral change is treated as an existential assault.

Rigid spinal alignment, a contemptuous micro-smirk, and elevated brows devalue the other ('you don't understand') to preserve cognitive supremacy.

Monolithic synth drones construct an acoustic glass enclosure shutting out all ambient air."""
            },
            {
                "quote": "If I fall, I fall alone / No one is worthy",
                "body": """Heroization of isolation: catastrophe is privatized into an elite solo performance to avoid indebted vulnerability.

Eye closure, torso rotated away from the interlocutor, and a sudden gravitational slump in posture deploy contempt as the ego's ultimate bunker.

Sparse, isolated piano keystrokes float inside an empty reverb chamber without harmonic resolution."""
            }
        ]
    },
    {
        "num": "06",
        "title": "Rette mich nicht",
        "key_triggers": [
            ("Komm mir nicht zu nah, du verbrennst dich", 0),
            ("Mein Herz ist ein Krater, unendlich", 0),
            ("Rette mich nicht, ich will ertrinken", 1),
            ("In mei'm eig'nen Gift, lass mich versinken", 1),
            ("Du denkst, du kannst mich heilen mit 'nem Blick?", 2),
            ("Ich zieh' dich nur mit mir in den Abgrund zurück", 2)
        ],
        "review_de": """<p><strong>„Rette mich nicht“</strong> attackiert den Helfersyndrom-Reflex des Partners mit chirurgischer Präzision. Das lyrische Ich inszeniert sich als toxische Gefahrenzone: <span class="lyric-quote-highlight">„Mein Herz ist ein Krater, unendlich / Komm mir nicht zu nah, du verbrennst dich“</span>.</p>
<p>Diese Warnung ist jedoch kein altruistischer Akt, sondern der ultimative Köder. Indem der Protagonist jede Heilung ablehnt und sein eigenes Gift als Schicksal zelebriert, bindet er das Gegenüber in eine destruktive Retter-Dynamik ein, an deren Ende nur der gemeinsame Absturz stehen kann.</p>""",
        "review_en": """<p><strong>“Rette mich nicht”</strong> (Do Not Save Me) surgically dismantles the partner's savior complex. The lyrical self stages itself as an environmental biohazard: <span class="lyric-quote-highlight">“My heart is an infinite crater / Don't come too close, you will burn”</span>.</p>
<p>Yet this warning is not altruistic; it functions as the ultimate seductive bait. By rejecting therapeutic salvation and fetishizing his own poison, he ensnares the partner in a toxic rescuer loop where mutual ruin is the only terminus.</p>""",
        "cards_de": [
            {
                "quote": "Komm mir nicht zu nah / Mein Herz ein Krater",
                "body": """Das Bild des Kraters markiert eine posttraumatische Verwüstungslandschaft: Nähe wird als Verbrennungsgefahr deklariert, um Verantwortung für spätere Verletzungen im Vorfeld abzuwälzen.

Ausgestreckte abwehrende Hände und ein Zurückweichen bei gleichzeitiger magnetischer Fixierung mit den Augen schaffen eine toxische Verführung durch Selbststigmatisierung („Ich habe dich gewarnt“).

Verzerrte Basslines und knisternde Noise-Artefakte klingen wie verglühende Asche."""
            },
            {
                "quote": "Rette mich nicht / Lust am Ertrinken",
                "body": """Todestrieb (Thanatos) und depressive Selbstaufgabe: Die Weigerung, gerettet zu werden, ist der letzte Versuch, Autonomie durch Selbstzerstörung auszuüben.

Schlaffe Muskulatur, resignatives Senken des Kopfes und ein dumpfer Stimmklang entmachten den Helfer vollständig: Wenn Hilfe verweigert wird, verliert der Partner jeglichen Einfluss.

Tiefpassgefilterte Pads klingen wie unter Wasser und inszenieren das Ertrinken akustisch."""
            },
            {
                "quote": "Keine Heilung / Mit in den Abgrund",
                "body": """Maligner Narzissmus und Neid auf das Gesunde: Die Unfähigkeit zur eigenen Genesung schlägt in den Wunsch um, den stabilen Partner mit in die Zerstörung zu reißen.

Zynisches Grinsen, ruckartiges Heranziehen des Gegenübers gefolgt von partiellem Wegstoßen: Die Zerstörung der Integrität des Partners wird zur Rache an dessen seelischer Gesundheit.

Ein schneidender Drop mit harten Drums macht den abrupten Sturz in den Abgrund hörbar."""
            }
        ],
        "cards_en": [
            {
                "quote": "Don't come too close / Heart is a Crater",
                "body": """The crater metaphor signifies a post-traumatic scorched-earth psyche: intimacy is framed as lethal to pre-emptively disclaim responsibility for inevitable harm.

Extended defensive palms and a step backward paired with a piercing magnetic gaze engineer dark mystique and the self-fulfilling prophecy of 'I warned you.'

Distorted bass textures layered with crackling vinyl artifacts evoke burning embers."""
            },
            {
                "quote": "Do not save me / Drowning in Poison",
                "body": """Thanatos and depressive surrender: refusing rescue serves as the ultimate assertion of autonomy via self-annihilation.

Muscular flaccidity, a downward head tilt, and deadened vocal timbre neutralize the helper's agency; rejecting aid renders the partner utterly powerless.

Submerged low-pass pads mimic underwater sensory deprivation across the mix."""
            },
            {
                "quote": "No healing / Dragged into the abyss",
                "body": """Malignant envy: the inability to integrate healing turns into the retaliatory drive to pull the healthy partner into the vortex.

A sardonic grin and an abrupt pull toward the partner followed by rejection destroy their emotional stability as retribution for their wholeness.

A searing sonic drop with abrasive percussion realizes the psychological plummet."""
            }
        ]
    },
    {
        "num": "07",
        "title": "Leicht",
        "key_triggers": [
            ("Mach' es mir leicht, mach' es mir leicht", 0),
            ("Trying to feel alright all the time", 0),
            ("Und geteiltes Leid ist halbes Leid", 1),
            ("Sie will ballern, ich schenk' ihr ein Gramm", 2),
            ("„Meld dich“, sagt sie, ich denke nicht dran", 2),
            ("„Danke für den nicen Abend“, sagt sie", 2),
            ("„Ja“, sag' ich und schließ' die Tür von ihr'm Taxi", 2)
        ],
        "review_de": """<p><strong>„Leicht“</strong> verhandelt das Diktat der emotionalen Schwerelosigkeit in der spätmodernen Konsumgesellschaft. Hinter dem manischen Mantra <span class="lyric-quote-highlight">„Trying to feel alright all the time“</span> verbirgt sich eine gravierende Anhedonie – die Unfähigkeit, ohne chemische Stimulation echte Freude oder Trauer zu empfinden.</p>
<p>Die Schlussszene des Tracks gehört zu den stärksten Momenten des Albums: Das Schließen der Taxitür (<span class="lyric-quote-highlight">„‚Meld dich‘, sagt sie, ich denke nicht dran / ‚Ja‘, sag' ich und schließ' die Tür von ihr'm Taxi“</span>) ist der präzise somatische Vollzug der Entsorgung. Keine Wut, keine Trauer, nur das trockene Einrasten des Türschlosses als Schlusspunkt einer entwerteten Begegnung.</p>""",
        "review_en": """<p><strong>“Leicht”</strong> (Light / Easy) tackles the compulsory mandate of emotional weightlessness in consumer culture. Beneath the manic loop <span class="lyric-quote-highlight">“Trying to feel alright all the time”</span> lies profound anhedonia—the incapacity to access organic joy or grief without pharmaceutical amplification.</p>
<p>The closing sequence constitutes one of the record's sharpest vignettes: slamming the taxi door (<span class="lyric-quote-highlight">“'Call me,' she says, I don't think about it / 'Yeah,' I say and close the door of her taxi”</span>) executes relational disposal with clinical calm. No fury, no remorse—just the mechanical latching of the lock sealing off intimacy.</p>""",
        "cards_de": [
            {
                "quote": "Mach' es mir leicht / Trying to feel alright",
                "body": """Zwanghafter Hedonismus als Abwehr von Depression: Jedes schwere Gefühl wird als Systemfehler interpretiert, der durch Ablenkung oder Substanzen sofort neutralisiert werden muss.

Rastloses Fußwippen und ein flaches Lächeln ohne Beteiligung der Augenpartie fordern von der Umwelt, keinerlei Ansprüche an emotionale Tiefe zu stellen.

Schnelle UK-Garage-Beats und federnde Basslines täuschen klanglich eine mühelose Schwerelosigkeit vor."""
            },
            {
                "quote": "Geteiltes Leid / Zynische Empathie",
                "body": """Verkehrung des Solidaritätsgedankens: Geteiltes Leid bedeutet hier nicht gegenseitiges Halten, sondern das rücksichtslose Abwälzen des eigenen Schmerzes auf das Gegenüber.

Schulterzucken, eine abfällige Handbewegung und ein flüchtiger Blick zur Seite vollziehen die emotionale Ausbeutung unter dem Deckmantel von Gleichberechtigung.

Schwebende, leicht verstimmt klingende Synthesizer-Akkorde erzeugen subtile psychologische Dissonanz."""
            },
            {
                "quote": "Die Taxitür / Klinische Entsorgung",
                "body": """Vollständige emotionale Entsorgung nach erfolgtem Konsum: Das Gegenüber wird mit Drogen bezahlt, betäubt und per Taxi aus dem eigenen Orbit befördert.

Trockenes Zuziehen der Wagentür mit einer Handbewegung und sofortiges Abwenden des Körpers ohne Blickkontakt besiegeln das Beziehungsende.

Das dumpfe, mechanische Zuschlagen der Autotür hallt isoliert im Stereopanorama nach."""
            }
        ],
        "cards_en": [
            {
                "quote": "Make it easy / Trying to feel alright",
                "body": """Compulsive hedonic regulation as defense against baseline depression: any heavy emotion is flagged as an error requiring chemical override.

Restless lower-limb bouncing and a mechanical smile failing to engage periocular muscles demand zero emotional depth from the environment.

Rapid UK garage syncopation and buoyant basslines fabricate effortless flotation across the track."""
            },
            {
                "quote": "Shared sorrow / Cynical Solidarity",
                "body": """Subversion of empathy: shared suffering is reframed not as mutual holding, but as unloading somatic distress onto the partner.

A nonchalant shoulder shrug, dismissive wrist flick, and transient gaze mask emotional dumping as relational equality.

Floating, micro-detuned synth chords create subtle psychological friction."""
            },
            {
                "quote": "The taxi door / Clinical Disposal",
                "body": """Total relational disposal post-transaction: the encounter is subsidized with a gram, extinguished, and transported offsite.

A single-motion mechanical door latching followed by an instant pivot of the torso away without visual farewell terminates intimacy with zero residual attachment.

The isolated transient of a car door thud reverberates across the stereo field."""
            }
        ]
    },
    {
        "num": "08",
        "title": "Höhenflug + Tiefenrausch",
        "key_triggers": [
            ("Kratze jede Wunde zu 'ner Narbe", 0),
            ("Hasse jede Stunde, die ich warte", 0),
            ("Bin ein alter Schwamm, den man mal wechseln müsste", 1),
            ("Wurde von 'nem Sorgenkind zum Sorgenking", 1),
            ("Die Couch schluckt mich und spuckt mich nie mehr aus", 2),
            ("Falle durch die Welt, bin im Fiebertraum", 2),
            ("Zwischen Höhenflug und Tiefenrausch", 2),
            ("Hing nur mit dir rum, weil ich dich so gehasst hab'", 3),
            ("Alkohol macht mich zu einer fetten Schnecke", 3),
            ("Lieg' in der Wanne, versuch' mich aufzulösen", 3)
        ],
        "review_de": """<p><strong>„Höhenflug + Tiefenrausch“</strong> bildet das depressive Epizentrum des Albums. Der manische Höhenflug schlägt ungebremst in die vegetative Erstarrung um. In der Zeile <span class="lyric-quote-highlight">„Bin ein alter Schwamm, den man mal wechseln müsste / Wurde von 'nem Sorgenkind zum Sorgenking“</span> verdichtet Tua den Ekel vor der eigenen toxischen Sättigung.</p>
<p>Die Couch wird zum schwarzen Loch (<span class="lyric-quote-highlight">„Die Couch schluckt mich und spuckt mich nie mehr aus“</span>), das den kollabierten Körper verschlingt. Die grausame Ehrlichkeit der Beichte – <span class="lyric-quote-highlight">„Hing nur mit dir rum, weil ich dich so gehasst hab'“</span> – offenbart, dass Nähe hier rein als Projektionsfläche für ungelösten Selbsthass missbraucht wurde.</p>""",
        "review_en": """<p><strong>“Höhenflug + Tiefenrausch”</strong> (High Flight + Deep Intoxication) marks the depressive epicenter of the project. Manic elevation crashes directly into vegetative paralysis. In the striking line <span class="lyric-quote-highlight">“I'm an old sponge that should be replaced / Turned from a problem child into a problem king”</span>, Tua crystallizes visceral disgust with his own saturation.</p>
<p>The sofa mutates into a black hole (<span class="lyric-quote-highlight">“The couch swallows me and never spits me out”</span>) absorbing the depleted organism. The brutal confession—<span class="lyric-quote-highlight">“Only hung out with you because I hated you so much”</span>—unmasks companionship as nothing more than a scapegoat for self-directed rage.</p>""",
        "cards_de": [
            {
                "quote": "Wunde zu 'ner Narbe / Chronische Autoaggression",
                "body": """Zwanghafte Manipulation des eigenen Körpers, um Schmerz spürbar zu machen: Die Narbe wird zum trophäenartigen Beweis des Überlebens stilisiert.

Fingernägel bohren sich in die Haut, der Kiefer verspannt sich, und flache Stoßatmung sichert die Herrschaft über den eigenen Schmerz als Ersatz für fehlende Umweltkontrolle.

Trockene, kratzige Percussion-Sounds imitieren das mechanische Reiben auf der Haut."""
            },
            {
                "quote": "Alter Schwamm & Sorgenking / Die Sättigung des Ekels",
                "body": """Ekel vor der eigenen moralischen und körperlichen Kontamination: Die Umwandlung vom Sorgenkind zum „Sorgenking“ zelebriert das Scheitern als königliche Inszenierung.

Schweres Einsinken des Kopfes auf die Brust, bleierne Müdigkeit in den Gliedmaßen und ein matter Blick verkörpern grandiosen Zynismus: Wenn man schon leidet, dann als Monarch des Elends.

Ein schleppender, schwerer Beat mit tiefen analogen Bass-Drones zieht das Tempo nach unten."""
            },
            {
                "quote": "Die Couch schluckt mich / Bipolare Crash-Somatik",
                "body": """Vollständiger Zusammenbruch der dopaminergen Systeme nach dem Höhenflug: Die Couch wird zur Metapher des vegetativen Freeze-Zustands.

Totale Erschlaffung der Skelettmuskulatur, Unfähigkeit zum Aufstehen und Schweregefühl in den Lidern signalisieren absolute Ohnmacht gegenüber der eigenen Biochemie.

Ein breiter, zäher Synth-Teppich füllt den Raum wie dichter Sirup aus und erstickt jede Bewegung."""
            },
            {
                "quote": "Hing nur mit dir rum / Parasitäre Verachtung",
                "body": """Projektive Identifikation: Der eigene Selbsthass wird auf den Partner projiziert und dort verachtet, um ihn nicht am eigenen Körper vollstrecken zu müssen.

Zurückgezogene Mundwinkel, kalte Apathie und das Entgleiten jeglicher Wärme aus den Augen zerstören den Selbstwert des Partners als letzte sadistische Befriedigung.

Eine verstörend intime, nah mikrofonierte Vocal-Spur ohne Raumhall verstärkt die Beklemmung."""
            }
        ],
        "cards_en": [
            {
                "quote": "Scratching every wound into a scar / Auto-aggression",
                "body": """Compulsive tactile somatization to force feeling into a numb organism: the scar is curated as trophy proof of survival.

Nails digging into skin folds, masseter tension, and rapid shallow gasps exert dominance over self-inflicted pain to compensate for zero environmental control.

Scraping, dry percussive clicks sonically emulate tactile skin irritation."""
            },
            {
                "quote": "Old sponge & Problem King / Saturated Repulsion",
                "body": """Visceral disgust with moral and physical toxification: elevating from problem child to 'Problem King' crowns failure with royal grandeur.

A heavy cervical drop onto the sternum, leaden limbs, and a glazed stare embody grandiose cynicism: reigning supreme over one's own wreckage.

A sluggish, heavyweight boom-bap rhythm anchored by analog sub drones drags the tempo down."""
            },
            {
                "quote": "The couch swallows me / Vegetative Collapse",
                "body": """Total dopamine exhaustion following the manic run: the couch symbolizes dorsal vagal shutdown and complete depressive freeze.

Profound musculoskeletal hypotonia, an inability to rise, and drooping eyelids register complete helplessness before neurochemical depletion.

Viscous, suffocating low-end synth pads envelop the frequency field like thick oil."""
            },
            {
                "quote": "Only stayed because I hated you / Parasitic Contempt",
                "body": """Projective identification: internal self-loathing is projected onto the partner and despised externally to spare the core ego.

Retracted lips, flat cold detachment, and drained ocular focus decimate partner self-esteem as final compensatory fuel.

An unsettlingly dry, hyper-proximate vocal capture without spatial room reverberation heightens claustrophobia."""
            }
        ]
    },
    {
        "num": "09",
        "title": "Dopamin Spike",
        "key_triggers": [
            ("Dopamin-Spike und mein Herz rast", 0),
            ("Baller' mich höher als die Schwerkraft", 0),
            ("Jeder Satz hört sich legendär an", 1),
            ("Und muss gar nicht wahr sein", 1),
            ("Muss sich nur so anfühl'n", 1),
            ("Sag, fühlst du das auch?", 2),
            ("Sonnenbrille bei Nacht, denn ich bin in der Matrix", 2),
            ("High auf Moral, doch ich glaub's nicht", 3),
            ("Denn es ist deine Wahrheit / Wegen der du so taub bist", 3)
        ],
        "review_de": """<p><strong>„Dopamin Spike“</strong> ist die Hymne des neurochemischen Größenwahns. Mit dem Einsetzen des Rausches wird die Realität komplett suspendiert: <span class="lyric-quote-highlight">„Jeder Satz hört sich legendär an / Und muss gar nicht wahr sein / Muss sich nur so anfühl'n“</span>.</p>
<p>Die Zeile entlarvt den postfaktischen Charakter des Drogenrauschs: Wahrheit wird durch reine biochemische Intensität ersetzt. Die <span class="lyric-quote-highlight">„Sonnenbrille bei Nacht“</span> fungiert als visueller Filter gegen die Blendung durch das reale Leben – die Matrix wird zur bevorzugten Heimat, in der moralische Urteile als bloße Illusionen belächelt werden.</p>""",
        "review_en": """<p><strong>“Dopamin Spike”</strong> is the anthem of neurochemical megalomania. As the high peaks, empirical reality is entirely suspended: <span class="lyric-quote-highlight">“Every sentence sounds legendary / And doesn't need to be true / Just needs to feel like it”</span>.</p>
<p>This couplet exposes the post-truth nature of chemical intoxication: objective reality is replaced by raw neurotransmitter intensity. Wearing <span class="lyric-quote-highlight">“sunglasses at night”</span> operates as an optical filter against sober exposure—the Matrix becomes the sanctuary where moral constraints are mocked as illusions.</p>""",
        "cards_de": [
            {
                "quote": "Dopamin-Spike & Herzrasen / Chemische Neuro-Emanzipation",
                "body": """Künstliche Erzeugung von Lebendigkeit durch Noradrenalin und Dopamin: Die Tachykardie wird als Beweis des Triumphes über die biologische Schwerkraft gefeiert.

Zittrige Finger, geweitete Pupillen und vibrierende Kiefermuskeln untermauern die chemische Allmachtsfantasie eines unzerstörbaren Körpers.

Pumpende Sidechain-Kompression auf schnellen Synth-Akkorden treibt den Puls gnadenlos an."""
            },
            {
                "quote": "Muss gar nicht wahr sein / Postfaktischer Affekt",
                "body": """Vollständige Abkopplung des Gefühls von der Realität: Wahr ist nur, was Dopamin ausschüttet; empirische Fakten werden irrelevant.

Ausladende Gestik, übersteigertes Sprechtempo (Logorrhoe) und ein euphorisches Grinsen konstruieren eine hermetische Scheinwelt ohne Widerspruch.

Schillernde Höhen und resonante Filter-Sweeps stimulieren künstliche Euphorie."""
            },
            {
                "quote": "Sonnenbrille bei Nacht / Der Matrix-Filter",
                "body": """Visuelle Dissoziation: Die Sonnenbrille schützt die geweiteten Pupillen vor Entlarvung und trennt das Ich hermetisch von der Umwelt.

Starrer Kopf, verdeckter Blickkontakt und kühle Körperhaltung etablieren eine einseitige Überwachung: Ich sehe dich, aber du kannst nicht in mich hineinsehen.

Eine dunkle, pulsierende Bassline mit metallischen Hi-Hats untermalt die künstliche Matrix."""
            },
            {
                "quote": "High auf Moral / Die Entwertung der Tugend",
                "body": """Abwehr moralischer Schuldgefühle durch Entwertung der Tugend des Gegenübers: Wer integer bleibt, wird als scheinheilig und schwach abqualifiziert.

Spöttisches Lächeln, ein leichtes Abwinken mit dem Handgelenk und ein distanzierter Stand setzen radikalen Relativismus gegen berechtigte Kritik.

Ein schneidender Vokal-Chop hallt wie ein hämisches Lachen durch den Stereomix."""
            }
        ],
        "cards_en": [
            {
                "quote": "Dopamine Spike & Racing Pulse / Neurochemical Elevation",
                "body": """Artificial ignition of vitality via noradrenergic flood: tachycardia is celebrated as transcendence over biological gravity.

Fine motor tremor in hands, dilated pupils, and vibrating masseter muscles fuel the chemical omnipotence fantasy of an invulnerable organism.

Pumping sidechain compression on rapid synth chords relentlessly drives the tempo."""
            },
            {
                "quote": "Doesn't need to be true / Post-Factual Affect",
                "body": """Complete decoupling of emotional conviction from empirical truth: truth is defined solely by neurochemical discharge.

Grandiose sweeping gestures, pressured logorrhea, and a manic grin fabricate a solipsistic reality immune to contradiction.

Shimmering high-register arpeggios and resonant filter sweeps stimulate artificial euphoria."""
            },
            {
                "quote": "Sunglasses at night / The Matrix Filter",
                "body": """Visual dissociation: dark lenses shield dilated pupils from inspection while isolating the self from external gaze.

Rigid neck alignment, shielded ocular contact, and a cool demeanor establish asymmetrical surveillance: observing without reciprocity.

A dark undulating bassline driving crisp metallic percussion sustains the synthetic Matrix."""
            },
            {
                "quote": "High on Morals / Devaluation of Virtue",
                "body": """Neutralizing ethical guilt by devaluing the partner's moral compass as hypocritical weakness.

A mocking smirk, dismissive wrist gesture, and aloof stance deploy radical moral relativism against valid critique.

A slicing vocal chop echoes across the stereo field like a taunt."""
            }
        ]
    },
    {
        "num": "10",
        "title": "Amnesia",
        "key_triggers": [
            ("Diese EDM-Mucke hier drinne ist furchtbar, kurz ma'", 0),
            ("Ich hass' diese Nacht und ich hass' ihr'n Geburtstag", 0),
            ("Lächel gezwung'n, renne aufs Klo, um zu koksen und weil ich Durst hab'", 0),
            ("Sage diesem Hurensohn: „Mach mal nicht auf Gangster", 1),
            ("Junge, ich box' dich zurück nach England“", 1),
            ("Du kommst mir grade recht", 2),
            ("Junge, willst du, dass ich dir die Nase brech'?", 2),
            ("Sag' dem Secu: „Tranquilo, I go home“", 3),
            ("Warte auf den Drop und die CO2-Kanon'n", 3),
            ("Und tret' ihm in sein Declan-Rice-Trikot", 3)
        ],
        "review_de": """<p>In <strong>„Amnesia“</strong> explodiert die gestaute toxische Energie im legendären Großraumclub auf Ibiza. Tua dekonstruiert die sensorische Hölle der EDM-Nacht: <span class="lyric-quote-highlight">„Ich hass' diese Nacht und ich hass' ihr'n Geburtstag / Lächel gezwung'n, renne aufs Klo, um zu koksen und weil ich Durst hab'“</span>.</p>
<p>Die Eskalation mit einem britischen Clubgast wird zur ultimativen Katharsis. Mit der schneidenden Hook <span class="lyric-quote-highlight">„Du kommst mir grade recht / Willst du, dass ich dir die Nase brech'?“</span> wird der Schläger zum ersehnten Ventil für den eigenen Selbsthass. Im Moment des CO2-Kanonen-Drops entlädt sich die Gewalt als choreografiertes Finale eines gescheiterten Urlaubs.</p>""",
        "review_en": """<p>In <strong>“Amnesia”</strong>, accumulated toxic kinetic energy detonates inside the legendary Ibiza mega-club. Tua deconstructs the sensory purgatory of commercial EDM: <span class="lyric-quote-highlight">“I hate this night and I hate her birthday / Forced smile, run to the bathroom to do coke and because I'm thirsty”</span>.</p>
<p>The brawl with a British club-goer becomes an ecstatic catharsis. Driven by the unrelenting hook <span class="lyric-quote-highlight">“You're just what I needed / Boy, you want me to break your nose?”</span>, violence provides the long-sought release valve for self-loathing. At the peak of the CO2 cannon blast, physical brutality synchronizes with the festival drop.</p>""",
        "cards_de": [
            {
                "quote": "EDM-Mucke & Toiletten-Flucht / Sensorische Überlastung",
                "body": """Reizüberflutung und akute sensorische Intoleranz unter Club-Bedingungen: Das erzwungene Lächeln bricht zusammen; die Toilette wird zum letzten Schutzraum für chemische Nachjustierung.

Verkniffene Gesichtszüge, Zähneknirschen (Bruxismus) und hastige Atemfrequenz markieren die Flucht vor den sozialen Verpflichtungen des Abends.

Aggressive, dumpf pochende 4-to-the-floor Kicks und schrille EDM-Leads erzeugen eine unerträgliche akustische Enge."""
            },
            {
                "quote": "Box' dich nach England / Projektive Entlastung",
                "body": """Verschiebung innerer Frustration auf ein äußeres Feindbild: Der britische Tourist dient als idealer Blitzableiter für die eigene Ohnmacht.

Geballte Fäuste, Vorstrecken des Kinns und eine plötzliche Adrenalinschwemme stellen die gekränkte Männlichkeit durch physische Dominanzbehauptung wieder her.

Verzerrte, nah komprimierte Vocal-Takes wirken wie ein direkt ins Gesicht gebrüllter Schrei."""
            },
            {
                "quote": "Du kommst mir grade recht / Die Erlösungsfantasie",
                "body": """Gewalt als erlösende somatische Katharsis: Der drohende Kampf wird nicht gefürchtet, sondern herbeigesehnt, um die quälende innere Spannung physisch zu entladen.

Grinsen unter Hochspannung, federnder Kampfgang und rhythmische Atmung transformieren passives Leiden in aktive Destruktion.

Ein stoisch repetitiver Beat-Loop treibt die unausweichliche Kollision gnadenlos voran."""
            },
            {
                "quote": "CO2-Kanonen & Declan-Rice-Trikot / Choreografierte Eskalation",
                "body": """Verschmelzung von Club-Klimax und Schlägerei: Der Tritt erfolgt exakt auf dem musikalischen Drop – physische Gewalt wird zum integralen Bestandteil des Ibiza-Spektakels.

Explosive Kraftentfaltung im Moment des Losreißens vom Sicherheitsdienst setzt das triumphale Aushebeln aller Verhaltensregeln in Szene.

Ein druckvoller Bass-Drop und das berstende weiße Rauschen der CO2-Kanonen lassen den Mix explodieren."""
            }
        ],
        "cards_en": [
            {
                "quote": "EDM Purgatory & Bathroom Retreat / Sensory Overload",
                "body": """Acute sensory intolerance under commercial club stimuli: the forced smile fractures; the bathroom cubicle serves as emergency shelter for chemical re-dosing.

A pinched facial posture, bruxism, and rapid respiration register the desertion of social obligations into isolated chemical privacy.

Aggressive four-on-the-floor kick drums clashing with harsh synth leads construct an unbearable sensory cage."""
            },
            {
                "quote": "Punch you back to England / Displaced Rage",
                "body": """Displacement of internal shame onto a foreign target: the tourist becomes the lightning rod for narcissistic rage.

Clenched fists, a jutting mandible, and explosive adrenaline discharge physically re-assert dominance to repair injured ego structures.

Crushed, hyper-saturated vocal processing projects raw spatial confrontation directly into the foreground."""
            },
            {
                "quote": "You're just what I needed / Cathartic Violence",
                "body": """Physical altercation welcomed as somatic release: violence relieves unbearable internal tension by externalizing conflict.

A high-tension grin, rhythmic boxing bounce, and controlled respiration replace passive emotional paralysis with active mastery.

A relentlessly driving beat loop propels the physical collision forward."""
            },
            {
                "quote": "CO2 Cannons & Football Jersey / Choreographed Climax",
                "body": """Fusion of rave catharsis and physical violence: the kick lands exactly on the musical drop—turning brutality into club performance.

Explosive kinetic release tearing free from security grasp executes the strike, destroying civil boundaries under club cover.

A massive sub-bass impact combined with white noise CO2 blasts explodes across the stereo spectrum."""
            }
        ]
    },
    {
        "num": "11",
        "title": "Kaputt",
        "key_triggers": [
            ("Springmesser-Tattoo auf meiner Brust", 0),
            ("Hand aufs Herz, ich spüre kein'n Puls", 0),
            ("Deine Liebe blieb für immer im August", 0),
            ("Was ich berühr', das geht kaputt", 1),
            ("Ganzes Leben zerleg' ich zu Schutt", 1),
            ("Unerklärlich, als wär ich verflucht", 1),
            ("Ein toter Hund liegt zwischen dem Bauschutt", 2),
            ("Ich war nie viel mehr als 'ne Behauptung", 2),
            ("Lebenslanger Aufbruch", 2),
            ("Und ich kam immer davon, aber niemals an", 3)
        ],
        "review_de": """<p><strong>„Kaputt“</strong> ist das monumentale Finale und die schonungslose Selbstdemontage des Albums. Am verlassenen Hafen zwischen Bauruinen und Schutt blickt der Protagonist auf die Trümmer seiner Existenz: <span class="lyric-quote-highlight">„Ein toter Hund liegt zwischen dem Bauschutt / Ich war nie viel mehr als 'ne Behauptung“</span>.</p>
<p>Die zentrale Formel <span class="lyric-quote-highlight">„Was ich berühr', das geht kaputt“</span> formuliert den Fluch des malignen Narzissmus: Die Unfähigkeit, etwas Schönes zu lieben, ohne es im gleichen Atemzug zu vernichten. Mit dem resignativen Epilog <span class="lyric-quote-highlight">„Und ich kam immer davon, aber niemals an“</span> schließt das Album nicht mit Erlösung, sondern mit der Einsicht in die endlose Schleife der eigenen Entwurzelung.</p>""",
        "review_en": """<p><strong>“Kaputt”</strong> (Broken / Destroyed) serves as the monumental finale and unsparing self-demolition of the album. Standing at an abandoned harbor amid construction ruins, the protagonist surveys his psychological wasteland: <span class="lyric-quote-highlight">“A dead dog lies in the rubble / I was never much more than an assertion”</span>.</p>
<p>The central refrain <span class="lyric-quote-highlight">“Whatever I touch breaks / My whole life I smash into rubble”</span> encapsulates the destructive curse of untreated narcissistic pathology. With the closing epilogue <span class="lyric-quote-highlight">“And I always got away, but never arrived”</span>, the project concludes not in therapeutic redemption, but in full clarity regarding the perpetual loop of self-exile.</p>""",
        "cards_de": [
            {
                "quote": "Springmesser-Tattoo & Kein Puls / Somatische Erstarrung",
                "body": """Das Springmesser-Tattoo auf der Brust als Wappen der permanenten Abwehrbereitschaft: Das Fehlen des Pulses markiert die vollendete emotionale Nekrose.

Hand flach auf der Brust, erstarrte Atmung und das Ausbleiben jeglicher emotionalen Resonanz schaffen die zynische Beruhigung: Wer innerlich tot ist, kann nicht mehr getötet oder verletzt werden.

Schwere Klavierakkorde mit subtilem Tape-Leiern transportieren Trauer und unaufhaltsamen Verfall."""
            },
            {
                "quote": "Was ich berühr', geht kaputt / Der Midas-Fluch",
                "body": """Die Umkehrung des Midas-Mythos: Alles Berührte verwandelt sich nicht in Gold, sondern in Schutt. Destruktivität wird als unkontrollierbarer Schicksalsfluch erlebt.

Kraftloses Öffnen der Hände, Abgleiten der Arme am Körper und ein gesenkter Kopf signalisieren die vollständige Kapitulation vor dem eigenen Zerstörungspotenzial.

Mächtige, verzerrte Synthesizer-Wände schwellen im Refrain wie einstürzende Gebäude an."""
            },
            {
                "quote": "Toter Hund & Nur 'ne Behauptung / Das entlarvte Ego",
                "body": """Radikale Entblößung des falschen Selbst: Die Erkenntnis, dass die gesamte grandiose Persönlichkeit nur eine substanzlose Behauptung ohne inneren Kern war.

Blick auf den Boden, gebeugte Haltung und ein verlangsamter, schwerfälliger Schritt durch den Schutt markieren den totalen Einsturz der Fassade.

Eine brüchige, leise Vokalführung, umgeben von weitem Meeresrauschen und Windgeräuschen, verleiht dem Nullpunkt Stimme."""
            },
            {
                "quote": "Immer davon, niemals an / Die ewige Flucht",
                "body": """Das Kern-Dilemma der Fluchtbiografie: Das Entkommen gelingt stets, doch die Ankunft an einem Ort des Friedens bleibt strukturell unmöglich.

Blick zum fernen Horizont des Meeres, langsames Drehen des Körpers und eine Ausatmung ohne Erlösung spiegeln die Gefangenschaft im eigenen Bewegungsmuster.

Ein endlos ausklingender Synth-Drone löst sich langsam in weißem Rauschen auf und beendet das Werk."""
            }
        ],
        "cards_en": [
            {
                "quote": "Switchblade Tattoo & No Pulse / Somatic Necrosis",
                "body": """The switchblade tattoo over the sternum serves as an emblem of chronic defensive hostility; the absent pulse signifies total affective necrosis.

A hand resting flat on the chest, stopped thoracic rhythm, and absent visceral resonance deploy a cynical solace: he who is already deceased cannot be wounded.

Solemn piano chords drenched in tape flutter convey decay and irreversible loss."""
            },
            {
                "quote": "Whatever I touch breaks / Reverse Midas Curse",
                "body": """Inversion of the Midas myth: everything touched turns not to gold, but to rubble. Destructiveness is experienced as an inescapable curse.

Powerless opening of fingers, arms dropping limp along the torso, and a lowered head signal total surrender to the ego's destructive compulsion.

Monumental, saturated synth walls rise in the chorus like collapsing architecture."""
            },
            {
                "quote": "Dead dog in rubble / The False Self Exposed",
                "body": """Radical exposure of the false persona: the realization that grandiosity was merely an empty assertion without core substance.

A gaze locked onto gravel, hunched posture, and heavy plodding strides through coastal debris mark the total collapse of the facade.

Fragile, intimate vocal delivery cradled by distant ocean surf and wind gives voice to ground zero."""
            },
            {
                "quote": "Always got away, never arrived / The Eternal Exile",
                "body": """The fundamental trauma of the flight narrative: escape is always achieved, but arrival at genuine peace remains psychologically barred.

A gaze fixed onto the distant marine horizon, slow rotation of the body, and unresolved exhalation reflect imprisonment within one's own compulsive velocity.

An infinite decaying drone fades slowly into oceanic white noise, concluding the work."""
            }
        ]
    }
]

# Match lyrics stanzas from full_genius_lyrics.json
for t in tracks_data:
    t_num = t["num"]
    raw_track = raw_lyrics[t_num]
    triggers = t["key_triggers"]
    processed_stanzas = []
    
    global_line_counter = 0
    for stanza in raw_track["stanzas"]:
        st_title = stanza["title"]
        st_lines = []
        for line in stanza["lines"]:
            clean_line = line.strip()
            if not clean_line:
                continue
            
            matched_card = None
            for trig_text, c_idx in triggers:
                if trig_text.lower() in clean_line.lower() or clean_line.lower() in trig_text.lower():
                    matched_card = c_idx
                    break
            
            st_lines.append({
                "line_idx": global_line_counter,
                "text": clean_line,
                "annotated": matched_card is not None,
                "card_idx": matched_card
            })
            global_line_counter += 1
            
        processed_stanzas.append({
            "title": st_title,
            "lines": st_lines
        })
    t["stanzas"] = processed_stanzas

# Generate the EXACT 1:1 HTML matching tomora
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

for t in tracks_data:
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

# Render each track exactly like tomora
for t in tracks_data:
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
    
    # Stanzas
    for stanza in t["stanzas"]:
        html_out.append(f"""          <div class="stanza">
            <div class="stanza-title">{stanza['title']}</div>\n""")
        for line in stanza["lines"]:
            l_idx = line["line_idx"]
            text = line["text"]
            if line["annotated"]:
                c_idx = line["card_idx"]
                html_out.append(f"""            <div class="lyric-line annotated" data-line-idx="{l_idx}"><span class="lyric-trigger" data-track-num="{t_num}" data-target-card="{c_idx}">{text}</span></div>\n""")
            else:
                html_out.append(f"""            <div class="lyric-line plain" data-line-idx="{l_idx}">{text}</div>\n""")
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
      // Close other open decks across the page
      document.querySelectorAll('.track-section').forEach(ts => {
        if (ts !== trackSection) closeCardDeck(ts);
      });

      const activeLang = currentLang;
      const reviewEl = trackSection.querySelector(`.lang-${activeLang} .narrative-review`);
      const deckEl = trackSection.querySelector(`.lang-${activeLang} .card-deck-view`);
      
      if (!deckEl) return;

      // Update trigger active states in this track section
      trackSection.querySelectorAll('.lyric-trigger').forEach(tr => {
        const isMatch = tr.getAttribute('data-target-card') === targetCardIdx;
        tr.classList.toggle('active', isMatch);
      });

      // Calculate vertical alignment with clicked lyric line
      if (triggerEl && window.innerWidth > 992) {
        const gridEl = trackSection.querySelector('.track-grid');
        const triggerRect = triggerEl.getBoundingClientRect();
        const gridRect = gridEl.getBoundingClientRect();
        const relativeTop = triggerRect.top - gridRect.top;
        deckEl.style.marginTop = `${Math.max(0, Math.round(relativeTop))}px`;
      } else {
        deckEl.style.marginTop = '0px';
      }

      // Hide review, show deck
      if (reviewEl) reviewEl.style.display = 'none';
      deckEl.style.display = 'flex';

      // Activate specific card
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

    // Close on outside click
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

    // Toggle Play/Pause on Bottom Player
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

    // Prev / Next Controls
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

    // In-Page Track Song Play Buttons
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

    // In-Page Track Header Audio Play Buttons
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

    // Initialize bottom player with track 1
    updateTrackUI(0);
  </script>
</body>
</html>
""")

final_code = "".join(html_out)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_code)

print(f"Generated Pitchfork/Quietus-grade index.html: {len(final_code)} bytes")
