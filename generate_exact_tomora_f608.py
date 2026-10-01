# -*- coding: utf-8 -*-
import json
import re

# Load complete Genius lyrics
with open('full_genius_lyrics.json', 'r', encoding='utf-8') as f:
    raw_lyrics = json.load(f)

# Load CSS from tomora_index.html and adapt color variables
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
        "ytId": "",
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
<p>Die klangliche Architektur etabliert sofort das Leitmotiv des Projekts: Der Ikarus-Mythos. Der <span class="lyric-quote-highlight">Panoramablick übers Paradies</span> ist kein Ort der Ruhe, sondern die Startrampe für den kontrollierten Absturz. Mit der schneidenden Formel <span class="lyric-quote-highlight">„Wie man sich fesselt, so flieht man“</span> wird Bindung von vornherein als Gefängnis deklariert, das nur durch Flucht und Betäubung im <span class="lyric-quote-highlight">Himmel von Ibiza</span> ertragen werden kann.</p>""",
        "review_en": """<p>The album opens not with nostalgic contemplation, but with the clean slice of a scalpel: <strong>“1996”</strong> operates as both sonic prologue and psychological fault line. Framed by broadcasts from the fictional station <em>Ego FM Ibiza</em>, the protagonist steps onto the synthetic Mediterranean stage where all provincial memories are incinerated through sheer velocity.</p>
<p>The sonic architecture immediately establishes the central motif: the Icarus ascent. The <span class="lyric-quote-highlight">panoramic view over paradise</span> is no sanctuary, but the staging ground for a controlled descent. Through the cutting aphorism <span class="lyric-quote-highlight">“The way you bind yourself is the way you flee”</span>, intimacy is pre-emptively coded as imprisonment, survivable only through evasion into the <span class="lyric-quote-highlight">Ibiza sky</span>.</p>""",
        "cards_de": [
            {
                "quote": "Panoramablick übers Paradies / Die künstliche Idylle",
                "body": """* **Psychodynamische Kausalität:** Die Inszenierung des Luxus-Panoramas dient als hermetische Barriere gegen frühe Ohnmachts- und Mangelgefühle. Das Paradies ist kein Ort der Entspannung, sondern ein manisch errichtetes Bühnenbild.
* **Körpersprache & Somatik:** Erhöhter Muskeltonus im Nackenbereich, fixierter Weitblick über das Meer, flache thorakale Atmung, die das vegetative Nervensystem in dauerhafter Alarmbereitschaft hält.
* **Macht- & Kontroll-Dynamik:** Erhabene Aussichtsposition als Dominanzgestus. Wer von oben herabblickt, kann nicht überrascht, bewertet oder verletzt werden.
* **Akustische & räumliche Wirkung:** Schwebende, warme Synthesizer-Pads, die plötzlich von treibenden 2-Step-Breakbeats durchbrochen werden."""
            },
            {
                "quote": "Das Gegenteil, das Außerhalb / Das Erwachen des Mangels",
                "body": """* **Psychodynamische Kausalität:** Trotz maximaler äußerer Reizüberflutung bricht die innere Leere („das Außerhalb“) durch. Der narzisstische Triumph scheitert an der Unfähigkeit, innere Ruhe zu empfinden.
* **Körpersprache & Somatik:** Plötzliches Erstarren der Gesichtszüge, innerer Kälteschauer trotz warmer Mittelmeerluft, unruhiges Wippen der Füße.
* **Macht- & Kontroll-Dynamik:** Kontrollverlust über die eigenen Affekte. Das Unbewusste meldet sich als unkontrollierbarer Fremdkörper an.
* **Akustische & räumliche Wirkung:** Frequenzbeschnittene Hallräume, die das Gefühl von Kapselung und plötzlich einsetzender Isolation auditiv spürbar machen."""
            },
            {
                "quote": "Wie man sich fesselt, so flieht man / Die Bindungs-Dialektik",
                "body": """* **Psychodynamische Kausalität:** Bindungsphobische Vorwegnahme des Scheiterns. Nähe wird als unerträgliche Fesselung erlebt, sodass der Fluchtreflex bereits vor Beginn der Beziehung aktiviert wird.
* **Körpersprache & Somatik:** Rückzug der Schultern, Ausweichen von direktem Blickkontakt, motorischer Vorwärtsdrang.
* **Macht- & Kontroll-Dynamik:** Autonomie-Behauptung durch Beziehungsabbruch. Wer zuerst geht, behält die Kontrolle über das Narrativ.
* **Akustische & räumliche Wirkung:** Trockene, schneidende Snare-Schläge im Verbund mit staccatoartigen Vocals."""
            },
            {
                "quote": "Himmel von Ibiza / Dissipation & Hedonismus",
                "body": """* **Psychodynamische Kausalität:** Nikotin und Insel-Hedonismus als Desensibilisierungswerkzeuge. Der Rauch fungiert als Schleier zwischen dem Selbst und der Realität.
* **Körpersprache & Somatik:** Tiefes, forciertes Inhalieren, gefolgt von demonstrativ verlangsamtem Ausatmen; Entspannung wird mimisch forciert, nicht organisch erlebt.
* **Macht- & Kontroll-Dynamik:** Zurschaustellung von Gleichgültigkeit gegenüber dem sozialen Umfeld.
* **Akustische & räumliche Wirkung:** Ausfasernde Delay-Fahnen auf den Gesangsspuren, die das Ineinanderfließen von Raum und Bewusstsein zeichnen."""
            }
        ],
        "cards_en": [
            {
                "quote": "Panoramic view over paradise / The Synthetic Sanctuary",
                "body": """* **Psychodynamic Causality:** The staging of the panoramic luxury retreat serves as a hermetic defense against early helplessness. Paradise is not a haven but an adrenaline-fueled set piece.
* **Body Language & Somatics:** Elevated cervical muscle tone, fixated horizon stare, shallow thoracic breathing sustaining chronic sympathetic arousal.
* **Power & Control Dynamics:** Elevated vantage as spatial dominance. Overlooking the scene prevents vulnerability to external judgment.
* **Acoustic & Spatial Impact:** Lush, warm ambient synthesizer pads abruptly intersected by driving garage breakbeats."""
            },
            {
                "quote": "The opposite, the outside / The Void Awakes",
                "body": """* **Psychodynamic Causality:** Despite saturation of external stimuli, chronic internal void breaks through. Narcissistic grandiosity fractures against the inability to sustain peace.
* **Body Language & Somatics:** Sudden facial freeze, micro-shiver despite warm Mediterranean air, restless foot tapping.
* **Power & Control Dynamics:** Loss of affective mastery. The repressed material returns as an uncontrollable intrusion.
* **Acoustic & Spatial Impact:** High-pass filtered reverb decays simulating sudden psychological encapsulation."""
            },
            {
                "quote": "The way you bind yourself is the way you flee / Attachment Dialectics",
                "body": """* **Psychodynamic Causality:** Avoidant attachment schema. Closeness is registered as suffocation; the escape protocol is triggered before intimacy can consolidate.
* **Body Language & Somatics:** Shoulder retraction, gaze evasion, restless kinetic locomotion.
* **Power & Control Dynamics:** Preserving sovereignty via pre-emptive abandonment. He who exits first dictates terms.
* **Acoustic & Spatial Impact:** Dry, cutting snare transients synchronizing with staccato vocal delivery."""
            },
            {
                "quote": "Ibiza Sky / Dissipation and Hedonism",
                "body": """* **Psychodynamic Causality:** Nicotine and island hedonism as chemical insulation. Smoke functions as an optical barrier between the self and emotional reality.
* **Body Language & Somatics:** Forced deep inhalation followed by exaggerated exhalation; composure is performed rather than felt.
* **Power & Control Dynamics:** Performed nonchalance signaling total emotional detachment from surroundings.
* **Acoustic & Spatial Impact:** Wide stereo delay tails diffusing vocal presence into the Mediterranean soundscape."""
            }
        ]
    },
    {
        "num": "02",
        "title": "Wiedersehen",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Spaltung zwischen äußerer Naturromantik und innerer chemischer Zerrüttung. Die Pinien symbolisieren das unerreichbare organische Leben, die Linien den verzweifelten Versuch künstlicher Selbstregulation.
* **Körpersprache & Somatik:** Mydriasis (Pupillenerweiterung), Trockenheit im Mundraum, angespannte Kiefermuskulatur bei krampfhaft ruhiger Außenhaltung.
* **Macht- & Kontroll-Dynamik:** Unterwerfung der Umwelt unter das chemische Regime.
* **Akustische & räumliche Wirkung:** Scharfe, metallische Percussions und trockene Bass-Impulse im Kontrast zu verwehten Gitarren-Samples."""
            },
            {
                "quote": "Vergessen, wie ich dich liebe / Reduktion auf den Trieb",
                "body": """* **Psychodynamische Kausalität:** Abspaltung von Empathie und emotionaler Bindung. Indem Liebe auf reine Triebbefriedigung reduziert wird, entledigt sich das Ich jeglicher moralischer Verantwortung.
* **Körpersprache & Somatik:** Kalter, unbewegter Blick; das Gesicht verliert seine mimische Resonanzfähigkeit (Affektverflachung).
* **Macht- & Kontroll-Dynamik:** Instrumentalisierung des Partners zur reinen narzisstischen Zufuhr.
* **Akustische & räumliche Wirkung:** Trockene, monotone Gesangslinie ohne Vibrato, die emotionale Taubheit klanglich exakt abbildet."""
            },
            {
                "quote": "Die Welt gehört denen, die sie sich nehmen / Das Raubtier-Dogma",
                "body": """* **Psychodynamische Kausalität:** Sozialdarwinistische Rationalisierung. Das Ich rechtfertigt seine Ausbeutungsmuster als universelles Lebensgesetz, um Schuldgefühle im Vorfeld zu neutralisieren.
* **Körpersprache & Somatik:** Fester Stand gegen den Seegang, geschwellte Brust, Zähne zusammengebissen.
* **Macht- & Kontroll-Dynamik:** Omnipotenzfantasie als Schutz vor der existentiellen Belanglosigkeit.
* **Akustische & räumliche Wirkung:** Wuchtiger Subbass, der den Raum okkupiert und keinen Widerspruch zulässt."""
            },
            {
                "quote": "Selig sind die Diebe / Das Transit-Manifest",
                "body": """* **Psychodynamische Kausalität:** Blasphemische Umwertung christlicher Demut. Der Diebstahl von Gefühlen und Ressourcen wird zum heiligen Akt der Selbsterhaltung stilisiert.
* **Körpersprache & Somatik:** Blick nach hinten auf die schäumende Heckwelle, Hände tief in den Jackentaschen vergraben, abgewandter Körper.
* **Macht- & Kontroll-Dynamik:** Absolute Verweigerung von Gegenseitigkeit. Nehmen ohne Geben als Überlebensstrategie.
* **Akustische & räumliche Wirkung:** Anschwellendes Meeresrauschen gemischt mit tiefen, abebbenden Synth-Drones."""
            }
        ],
        "cards_en": [
            {
                "quote": "Pine Trees & Lines / Organic Serenity vs Chemical Velocity",
                "body": """* **Psychodynamic Causality:** Splitting between exterior idyllic nature and internal chemical dysregulation. Pine trees represent unreachable organic peace; cocaine lines represent forced affective control.
* **Body Language & Somatics:** Mydriasis, xerostomia, hypertonic masseter muscles behind a deliberately rigid neutral posture.
* **Power & Control Dynamics:** Subordinating sensory reality to the chemical timetable.
* **Acoustic & Spatial Impact:** Sharp, metallic percussive transients clashing with distant acoustic guitar motifs."""
            },
            {
                "quote": "Forgot how I love you / Drive Reduction",
                "body": """* **Psychodynamic Causality:** Dissociation of empathy. By reducing complex love to animal drive, the ego exempts itself from ethical accountability.
* **Body Language & Somatics:** Flat affect, unblinking ocular focus, absence of prosodic warmth in speech.
* **Power & Control Dynamics:** Complete objectification of the relational partner into narcissistic supply.
* **Acoustic & Spatial Impact:** Monotone, bone-dry vocal staging stripped of natural vibrato."""
            },
            {
                "quote": "The world belongs to those who take it / Predator Ethos",
                "body": """* **Psychodynamic Causality:** Social-darwinist rationalization. The ego reframes relational exploitation as universal law to inoculate against guilt.
* **Body Language & Somatics:** Anchored stance against ferry sway, expanded thoracic cage, clenched jawline.
* **Power & Control Dynamics:** Omnipotence fantasy deployed against underlying insignificance.
* **Acoustic & Spatial Impact:** Heavy sub-bass saturation claiming the acoustic center."""
            },
            {
                "quote": "Blessed are the thieves / Transit Manifesto",
                "body": """* **Psychodynamic Causality:** Blasphemous subversion of spiritual beatitudes. Emotional theft is canonized as sacred self-preservation.
* **Body Language & Somatics:** Gaze locked on the churning white wake, hands buried in coat pockets, posture turned away from land.
* **Power & Control Dynamics:** Absolute rejection of reciprocity. Taking without returning as defensive stance.
* **Acoustic & Spatial Impact:** Churning marine white noise blended into decaying low-frequency drone sweeps."""
            }
        ]
    },
    {
        "num": "03",
        "title": "GluiV",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Luxusgüter und Drogenkonsum als fetischistische Rüstung. Das Subjekt tarnt seine Fragilität durch Symbole unantastbarer Macht und Unberührbarkeit.
* **Körpersprache & Somatik:** Schnelle, ruckartige Kopfbewegungen, Abtasten der eigenen Taschen, ständige Prüfung des Raumes auf potenzielle Bedrohungen.
* **Macht- & Kontroll-Dynamik:** Distanzierung durch Statusbarrieren. Wer das Ensemble trägt, beansprucht die visuelle und soziale Vormachtstellung.
* **Akustische & räumliche Wirkung:** Aggressive 808-Bässe, scharfe Trap-Hi-Hats und zerhackte Vokal-Loops."""
            },
            {
                "quote": "Weißt du, wer ich bin? / Die verbotene Wahrheit",
                "body": """* **Psychodynamische Kausalität:** Angst vor emotionaler Entblößung. Der Protagonist droht mit dem eigenen Abgrund, um das Gegenüber auf Distanz zu halten.
* **Körpersprache & Somatik:** Intensiver, bedrohlicher Blickkontakt, leicht vorgeneigter Oberkörper, gedämpfte, raue Stimme.
* **Macht- & Kontroll-Dynamik:** Einschüchterung durch emotionale Toxizität („Wenn ich's dir sag', kriegst du's nicht mehr aus dem Sinn“).
* **Akustische & räumliche Wirkung:** Gespenstische Pitch-Down-Effekte auf den Backing Vocals, die eine unheimliche Raumtiefe erzeugen."""
            },
            {
                "quote": "Jagd und Beute / Prädatorische Intimität",
                "body": """* **Psychodynamische Kausalität:** Verkehrung von Zuwendung in Jagdverhalten. Intimität wird als Machtkampf inszeniert, bei dem Unterwerfung die einzige Währung ist.
* **Körpersprache & Somatik:** Raubtierhafter Gang, geschärfte Sinne, Vermeidung von Berührungen abseits des sexuellen/machtbezogenen Kontexts.
* **Macht- & Kontroll-Dynamik:** Vollständige Kontrolle über das Nähe-Distanz-Gefälle.
* **Akustische & räumliche Wirkung:** Tief grollende Bassläufe, die das Gefühl eines sich schließenden Netzes klanglich übersetzen."""
            },
            {
                "quote": "Eiskaltes Händchen / Schritt vor, drei zurück",
                "body": """* **Psychodynamische Kausalität:** Intermittierende Verstärkung und Bindungs-Traumata. Das Vor- und Zurückweichen hält das Gegenüber in permanenter emotionaler Abhängigkeit gefangen.
* **Körpersprache & Somatik:** Kalte Peripherie (Hände/Füße) durch chronische Vasokonstriktion unter Stimulanzien; abruptes Abwenden nach kurzer Zuwendung.
* **Macht- & Kontroll-Dynamik:** Sadistische Kontrolle durch Unberechenbarkeit.
* **Akustische & räumliche Wirkung:** Stotternde Arpeggiatoren und Synkopen, die rhythmisch die Unstetigkeit des Protagonisten spiegeln."""
            }
        ],
        "cards_en": [
            {
                "quote": "Louis V, Waist Bag, Cocaine / The Fetish Armor",
                "body": """* **Psychodynamic Causality:** Brand signifiers and narcotics acting as armor. The fragile self shields against collapse by embodying impenetrable invulnerability.
* **Body Language & Somatics:** Rapid saccadic head movements, repetitive checking of body accessories, hyper-vigilant scanning of the room.
* **Power & Control Dynamics:** Social demarcation via luxury signifiers, asserting immediate visual dominance.
* **Acoustic & Spatial Impact:** Aggressive 808 sub-transients, slicing trap hi-hat rolls, and chopped vocal hooks."""
            },
            {
                "quote": "Do you know who I am? / The Poisonous Core",
                "body": """* **Psychodynamic Causality:** Defense against true exposure. The speaker threatens the partner with his destructive core to maintain relational distance.
* **Body Language & Somatics:** Piercing unyielding gaze, torso inclined forward, raspy dropped vocal register.
* **Power & Control Dynamics:** Intimidation via psychological toxicity, warning the partner that proximity is toxic.
* **Acoustic & Spatial Impact:** Pitch-shifted backing doubles creating an ominous, uncanny stereo spread."""
            },
            {
                "quote": "Hunter & Prey / Predatory Intimacy",
                "body": """* **Psychodynamic Causality:** Eroticization of dominance. Attachment is reframed as a predator-prey transaction where submission is demanded.
* **Body Language & Somatics:** Prowling kinetic motion, heightened auditory reflex, calculated physical touch.
* **Power & Control Dynamics:** Complete unilateral steering of relational access.
* **Acoustic & Spatial Impact:** Resonant low-end rumble simulating an enclosing psychological perimeter."""
            },
            {
                "quote": "Ice cold hand / One step forward, three steps back",
                "body": """* **Psychodynamic Causality:** Intermittent reinforcement schedule. Alternating between warm allure and glacial rejection engineers acute trauma bonding.
* **Body Language & Somatics:** Peripheral vasoconstriction (freezing hands) from stimulant load; abrupt physical disengagement.
* **Power & Control Dynamics:** Sadistic control achieved through structural unpredictability.
* **Acoustic & Spatial Impact:** Stuttering arpeggiator figures and syncope breaks echoing relational instability."""
            }
        ]
    },
    {
        "num": "04",
        "title": "Dachterrasse",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Räumliche Überhöhung als Metapher für narzisstische Abkapselung. Die Höhe garantiert Sicherheit vor unkontrollierten zwischenmenschlichen Kontakten.
* **Körpersprache & Somatik:** Schwindelgefühl (Vertigo), Festhalten am Geländer mit weißen Fingerknöcheln, vibrierende Brustmuskulatur.
* **Macht- & Kontroll-Dynamik:** Vermeidung von Augenhöhe. Wer auf der Dachterrasse steht, muss sich niemandem stellen.
* **Akustische & räumliche Wirkung:** Weite Hallräume mit Tiefpassfilter, die den Club-Bass von unten dumpf heraufschallen lassen."""
            },
            {
                "quote": "Ich kann nicht runterkommen / Angst vor der Erdung",
                "body": """* **Psychodynamische Kausalität:** Phobische Angst vor dem Absturz in die depressive Grundstimmung. Die „Einsamkeit da unten“ steht für die reale, ungeschönte Lebenswirklichkeit ohne Rausch.
* **Körpersprache & Somatik:** Schüttelfrost, vegetative Dissonanz zwischen Kälteempfinden und schweißnassen Handflächen.
* **Macht- & Kontroll-Dynamik:** Verweigerung von Hilfsangeboten; das Verharren auf der Kante dient als emotionale Erpressung.
* **Akustische & räumliche Wirkung:** Scharf akzentuierte Synthesizer-Lead-Lines, die wie Alarmsignale durch den Raum schneiden."""
            },
            {
                "quote": "Blick ein Verhör / Paranoide Hypervigilanz",
                "body": """* **Psychodynamische Kausalität:** Projektion eigener Schuld- und Schamgefühle auf die Blicke anderer. Jeder Blick wird als feindlicher Entlarvungsversuch interpretiert.
* **Körpersprache & Somatik:** Flackernder Blick, Anspannung der Trapezmuskeln, ständiges Drehen des Kopfes zur Seite.
* **Macht- & Kontroll-Dynamik:** Vorbeugende Aggression gegen vermeintliche Beobachter.
* **Akustische & räumliche Wirkung:** Komprimierte Bass-Stöße und beklemmende Panorama-Effekte, die eine klaustrophobische Atmosphäre schaffen."""
            }
        ],
        "cards_en": [
            {
                "quote": "Rooftop & Sea of Lights / The Solitary Vantage",
                "body": """* **Psychodynamic Causality:** Spatial elevation as physical correlate of narcissistic detachment. Altitude guarantees immunity from intimate encounters.
* **Body Language & Somatics:** Vertigo, white-knuckled grip on the balcony railing, chest wall vibration from low frequencies below.
* **Power & Control Dynamics:** Evading eye level. Occupying the rooftop exempts one from reciprocal dialogue.
* **Acoustic & Spatial Impact:** Expansive stereo hall with low-pass filtering capturing the muffled club bass thumping from ground level."""
            },
            {
                "quote": "I can't come down / Grounding Phobia",
                "body": """* **Psychodynamic Causality:** Phobic dread of crashing into baseline depressive emptiness. 'Loneliness down there' represents sober, unvarnished existence.
* **Body Language & Somatics:** Shivering, autonomic dissonance between somatic chill and clammy palms.
* **Power & Control Dynamics:** Rejection of rescue; lingering on the precipice functions as emotional leverage.
* **Acoustic & Spatial Impact:** Searing synthesizer leads slicing across the frequency field like siren alarms."""
            },
            {
                "quote": "Every glance an interrogation / Paranoid Hypervigilance",
                "body": """* **Psychodynamic Causality:** Projection of internal shame onto external observers. Every neutral glance is decoded as an investigative intrusion.
* **Body Language & Somatics:** Rapid ocular shifts, hypertonicity of trapezius muscles, constant peripheral scanning.
* **Power & Control Dynamics:** Pre-emptive hostility countering perceived surveillance.
* **Acoustic & Spatial Impact:** Compressed sub transients and panning claustrophobia mimicking acute panic."""
            }
        ]
    },
    {
        "num": "05",
        "title": "Für mich",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Die klassische narzisstische Paradoxie: Autarkie-Behauptung bei gleichzeitiger Abhängigkeit vom Blick des Anderen. Das Nicht-Gesehen-Werden löst schwere Kränkung aus.
* **Körpersprache & Somatik:** Krampfhafte Selbstumarmung, Heben der Stimme bis zum Überschlagen, unruhige Atmung.
* **Macht- & Kontroll-Dynamik:** Vorwurfsvolle Umkehr der Täter-Opfer-Rolle.
* **Akustische & räumliche Wirkung:** Weicher E-Piano-Akkord, der unvermittelt von harten, schneidenden Vocals durchbrochen wird."""
            },
            {
                "quote": "Ich bin perfekt in meiner Welt / Grandiose Abkapselung",
                "body": """* **Psychodynamische Kausalität:** Grandiose Selbstüberhöhung als Schutzwall gegen Kritik. Jede Aufforderung zur Veränderung wird als feindlicher Vernichtungsversuch abgewehrt.
* **Körpersprache & Somatik:** Starre Kopfhaltung, abfälliges Lächeln, hochgezogene Augenbrauen.
* **Macht- & Kontroll-Dynamik:** Entwertung des Partners („du verstehst das nicht“), um die eigene Überlegenheit zu wahren.
* **Akustische & räumliche Wirkung:** Monotone Synthesizer-Flächen, die eine hermetische, künstliche Klangblase bilden."""
            },
            {
                "quote": "Wenn ich falle, dann allein / Niemand ist es wert",
                "body": """* **Psychodynamische Kausalität:** Heroisierung der eigenen Isolation. Der Zusammenbruch wird zum exklusiven Monopol erklärt, um niemandem Dank oder Verletzlichkeit schuldig zu sein.
* **Körpersprache & Somatik:** Schließen der Augen, Abwenden des Oberkörpers vom Gegenüber, Absinken der Schultern.
* **Macht- & Kontroll-Dynamik:** Verachtung als letzter Rettungsanker des Ego.
* **Akustische & räumliche Wirkung:** Vereinzelte, hallüberladene Pianonoten im leeren Frequenzraum."""
            }
        ],
        "cards_en": [
            {
                "quote": "All for myself / Why don't you see me?",
                "body": """* **Psychodynamic Causality:** Classic narcissistic paradox: proclamation of total self-reliance coexisting with frantic dependency on external mirroring. Being unseen triggers acute shame.
* **Body Language & Somatics:** Defensive self-clasping posture, vocal cracking at higher registers, agitated hyperventilation.
* **Power & Control Dynamics:** Blaming inversion: casting the self as the sole victim of unappreciative partners.
* **Acoustic & Spatial Impact:** Intimate electric piano chord interrupted by aggressive dry vocal cuts."""
            },
            {
                "quote": "I am perfect in my world / Grandiose Isolation",
                "body": """* **Psychodynamic Causality:** Grandiose inflation as a fortress against critique. Any request for behavioral change is treated as an existential assault.
* **Body Language & Somatics:** Rigid spinal alignment, contemptuous micro-smirk, elevated brow.
* **Power & Control Dynamics:** Devaluation of the other ('you don't understand') to preserve cognitive supremacy.
* **Acoustic & Spatial Impact:** Monolithic synth drones constructing an acoustic glass enclosure."""
            },
            {
                "quote": "If I fall, I fall alone / No one is worthy",
                "body": """* **Psychodynamic Causality:** Heroization of isolation. Catastrophe is privatized into an elite solo performance to avoid indebted vulnerability.
* **Body Language & Somatics:** Eye closure, torso turned away from interlocutor, sudden gravitational slump in posture.
* **Power & Control Dynamics:** Contempt weaponized as the ego's ultimate defensive bunker.
* **Acoustic & Spatial Impact:** Sparse, isolated piano keystrokes floating inside an empty reverb chamber."""
            }
        ]
    },
    {
        "num": "06",
        "title": "Rette mich nicht",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Das Bild des Kraters markiert eine posttraumatische Verwüstungslandschaft. Nähe wird als Verbrennungsgefahr deklariert, um Verantwortung für spätere Verletzungen im Vorfeld abzuwälzen.
* **Körpersprache & Somatik:** Ausgestreckte abwehrende Hände, Zurückweichen bei gleichzeitiger Fixierung mit den Augen.
* **Macht- & Kontroll-Dynamik:** Toxische Verführung durch Selbststigmatisierung („Ich habe dich gewarnt“).
* **Akustische & räumliche Wirkung:** Verzerrte Basslines und knisternde Noise-Artefakte, die wie glühende Asche klingen."""
            },
            {
                "quote": "Rette mich nicht / Lust am Ertrinken",
                "body": """* **Psychodynamische Kausalität:** Todestrieb (Thanatos) und depressive Selbstaufgabe. Die Weigerung, gerettet zu werden, ist der letzte Versuch, Autonomie durch Selbstzerstörung auszuüben.
* **Körpersprache & Somatik:** Schlaffe Muskulatur, resignatives Senken des Kopfes, dumpfer Stimmklang.
* **Macht- & Kontroll-Dynamik:** Entmachtung des Helfers. Wenn Hilfe verweigert wird, verliert der Partner jeglichen Einfluss.
* **Akustische & räumliche Wirkung:** Tiefpassgefilterte Pads, die wie unter Wasser klingen und das Ertrinken klanglich inszenieren."""
            },
            {
                "quote": "Keine Heilung / Mit in den Abgrund",
                "body": """* **Psychodynamische Kausalität:** Maligner Narzissmus. Die Unfähigkeit zur eigenen Genesung schlägt in den Wunsch um, den gesunden Partner mit in die Zerstörung zu reißen.
* **Körpersprache & Somatik:** Zynisches Grinsen, ruckartiges Heranziehen des Gegenübers gefolgt von partiellem Wegstoßen.
* **Macht- & Kontroll-Dynamik:** Zerstörung der Integrität des Partners als Rache an dessen seelischer Gesundheit.
* **Akustische & räumliche Wirkung:** Ein schneidender Drop mit harten Drums, der den abrupten Sturz in den Abgrund hörbar macht."""
            }
        ],
        "cards_en": [
            {
                "quote": "Don't come too close / Heart is a Crater",
                "body": """* **Psychodynamic Causality:** The crater metaphor signifies a post-traumatic scorched-earth psyche. Intimacy is framed as lethal to pre-emptively disclaim responsibility for inevitable harm.
* **Body Language & Somatics:** Extended defensive palms, step backward paired with piercing magnetic gaze.
* **Power & Control Dynamics:** Seduction via dark mystique: the self-fulfilling prophecy of 'I warned you.'
* **Acoustic & Spatial Impact:** Distorted bass textures layered with crackling vinyl artifacts evoking burning embers."""
            },
            {
                "quote": "Do not save me / Drowning in Poison",
                "body": """* **Psychodynamic Causality:** Thanatos and depressive surrender. Refusing rescue serves as the ultimate assertion of autonomy via self-annihilation.
* **Body Language & Somatics:** Muscular flaccidity, downward head tilt, deadened vocal timbre.
* **Power & Control Dynamics:** Neutralizing the helper's agency; rejecting aid renders the partner utterly powerless.
* **Acoustic & Spatial Impact:** Submerged low-pass pads mimicking underwater sensory deprivation."""
            },
            {
                "quote": "No healing / Dragged into the abyss",
                "body": """* **Psychodynamic Causality:** Malignant envy. Inability to integrate healing turns into the retaliatory drive to pull the healthy partner into the vortex.
* **Body Language & Somatics:** Sardonic grin, abrupt pull toward the partner followed by rejection.
* **Power & Control Dynamics:** Destroying the partner's emotional stability as retribution for their wholeness.
* **Acoustic & Spatial Impact:** Searing sonic drop with abrasive percussion realizing the psychological plummet."""
            }
        ]
    },
    {
        "num": "07",
        "title": "Leicht",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Zwanghafter Hedonismus als Abwehr von Depression. Jedes schwere Gefühl wird als Systemfehler interpretiert, der durch Ablenkung oder Substanzen sofort neutralisiert werden muss.
* **Körpersprache & Somatik:** Rastloses Fußwippen, flaches Lächeln, das die Augenpartie nicht erreicht (Duchenne-Marker fehlen).
* **Macht- & Kontroll-Dynamik:** Forderung an die Umwelt, keine Ansprüche an emotionale Tiefe zu stellen.
* **Akustische & räumliche Wirkung:** Schnelle UK-Garage-Beats und federnde Basslines, die Schwerelosigkeit vorspiegeln."""
            },
            {
                "quote": "Geteiltes Leid / Zynische Empathie",
                "body": """* **Psychodynamische Kausalität:** Verkehrung des Solidaritätsgedankens. Geteiltes Leid bedeutet hier nicht gegenseitige Tröstung, sondern das Abwälzen des eigenen Schmerzes auf das Gegenüber.
* **Körpersprache & Somatik:** Schulterzucken, abfällige Handbewegung, flüchtiger Blick zur Seite.
* **Macht- & Kontroll-Dynamik:** Emotionale Ausbeutung unter dem Deckmantel von Gleichberechtigung.
* **Akustische & räumliche Wirkung:** Schwebende, leicht verstimmt klingende Synthesizer-Akkorde."""
            },
            {
                "quote": "Die Taxitür / Klinische Entsorgung",
                "body": """* **Psychodynamische Kausalität:** Vollständige emotionale Entsorgung nach erfolgtem Konsum. Das Gegenüber wird bezahlt, betäubt und per Taxi aus dem eigenen Orbit entfernt.
* **Körpersprache & Somatik:** Trockenes Zuziehen der Tür mit einer Handbewegung, sofortiges Abwenden des Körpers ohne Blickkontakt.
* **Macht- & Kontroll-Dynamik:** Absolute Souveränität über das Beziehungsende.
* **Akustische & räumliche Wirkung:** Das dumpfe, mechanische Zuschlagen der Autotür hallt isoliert im Stereopanorama nach."""
            }
        ],
        "cards_en": [
            {
                "quote": "Make it easy / Trying to feel alright",
                "body": """* **Psychodynamic Causality:** Compulsive hedonic regulation as defense against baseline depression. Any heavy emotion is flagged as an error requiring chemical override.
* **Body Language & Somatics:** Restless lower-limb bounce, mechanical smile failing to engage periocular muscles.
* **Power & Control Dynamics:** Demanding that the social environment place zero emotional demands on the self.
* **Acoustic & Spatial Impact:** Rapid UK garage syncopation and buoyant basslines fabricating effortless flotation."""
            },
            {
                "quote": "Shared sorrow / Cynical Solidarity",
                "body": """* **Psychodynamic Causality:** Subversion of empathy. Shared suffering is reframed not as mutual holding, but as unloading somatic distress onto the partner.
* **Body Language & Somatics:** Nonchalant shoulder shrug, dismissive wrist flick, transient gaze.
* **Power & Control Dynamics:** Exploitative emotional dumping masked as relational equality.
* **Acoustic & Spatial Impact:** Floating, micro-detuned synth chords creating subtle psychological friction."""
            },
            {
                "quote": "The taxi door / Clinical Disposal",
                "body": """* **Psychodynamic Causality:** Total relational disposal post-transaction. The encounter is subsidized with a gram, extinguished, and transported offsite.
* **Body Language & Somatics:** Single-motion mechanical door latching, instant pivot of the torso away without visual farewell.
* **Power & Control Dynamics:** Unilateral termination of intimacy with zero residual attachment.
* **Acoustic & Spatial Impact:** Isolated transient of a car door thud reverberating across the stereo field."""
            }
        ]
    },
    {
        "num": "08",
        "title": "Höhenflug + Tiefenrausch",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Zwanghafte Manipulation des eigenen Körpers, um Schmerz spürbar zu machen. Die Narbe wird zum trophäenartigen Beweis des Überlebens stilisiert.
* **Körpersprache & Somatik:** Fingernägel bohren sich in die Haut, Verspannung im Kiefer, flache Stoßatmung.
* **Macht- & Kontroll-Dynamik:** Herrschaft über den eigenen Schmerz als Ersatz für fehlende Umweltkontrolle.
* **Akustische & räumliche Wirkung:** Trockene, kratzige Percussion-Sounds, die das Reiben auf der Haut auditiv imitieren."""
            },
            {
                "quote": "Alter Schwamm & Sorgenking / Die Sättigung des Ekels",
                "body": """* **Psychodynamische Kausalität:** Ekel vor der eigenen moralischen und körperlichen Kontamination. Die Umwandlung vom Sorgenkind zum „Sorgenking“ zelebriert das Scheitern als königliche Inszenierung.
* **Körpersprache & Somatik:** Schweres Einsinken des Kopfes auf die Brust, bleierne Müdigkeit in den Gliedmaßen, matter Blick.
* **Macht- & Kontroll-Dynamik:** Grandioser Zynismus: Wenn man schon leidet, dann als Monarch des Elends.
* **Akustische & räumliche Wirkung:** Schleppender, schwerer Beat mit tiefen, analogen Bass-Drones."""
            },
            {
                "quote": "Die Couch schluckt mich / Bipolare Crash-Somatik",
                "body": """* **Psychodynamische Kausalität:** Vollständiger Zusammenbruch der dopaminergen Systeme nach dem Höhenflug. Die Couch wird zur Metapher des vegetativen Freeze-Zustands.
* **Körpersprache & Somatik:** Totale Hypotonie (Erschlaffung) der Skelettmuskulatur, Unfähigkeit zum Aufstehen, Schweregefühl in den Lidern.
* **Macht- & Kontroll-Dynamik:** Vollständige Ohnmacht gegenüber der eigenen Biochemie.
* **Akustische & räumliche Wirkung:** Breiter, zäher Synth-Teppich, der den Raum wie dichter Sirup ausfüllt."""
            },
            {
                "quote": "Hing nur mit dir rum / Parasitäre Verachtung",
                "body": """* **Psychodynamische Kausalität:** Projektive Identifikation. Der eigene Selbsthass wird auf den Partner projiziert und dort verachtet, um ihn nicht am eigenen Körper vollstrecken zu müssen.
* **Körpersprache & Somatik:** Zurückgezogene Mundwinkel, kalte Apathie, Entgleiten jeglicher Wärme aus den Augen.
* **Macht- & Kontroll-Dynamik:** Zerstörung des Selbstwerts des Partners als letzte sadistische Befriedigung.
* **Akustische & räumliche Wirkung:** Verstörend intime, nah mikrofoniere Vocal-Spur ohne Raumhall."""
            }
        ],
        "cards_en": [
            {
                "quote": "Scratching every wound into a scar / Auto-aggression",
                "body": """* **Psychodynamic Causality:** Compulsive tactile somatization to force feeling into a numb organism. The scar is curated as proof of survival.
* **Body Language & Somatics:** Nails digging into skin folds, masseter tension, rapid shallow gasps.
* **Power & Control Dynamics:** Dominance over self-inflicted pain compensating for zero environmental control.
* **Acoustic & Spatial Impact:** Scraping, dry percussive clicks sonically emulating tactile irritation."""
            },
            {
                "quote": "Old sponge & Problem King / Saturated Repulsion",
                "body": """* **Psychodynamic Causality:** Visceral disgust with moral and physical toxification. Elevating from problem child to 'Problem King' crowns failure with royal grandeur.
* **Body Language & Somatics:** Heavy cervical drop onto sternum, leaden limbs, glazed stare.
* **Power & Control Dynamics:** Grandiose cynicism: reigning supreme over one's own wreckage.
* **Acoustic & Spatial Impact:** Sluggish, heavyweight boom-bap rhythm anchored by analog sub drones."""
            },
            {
                "quote": "The couch swallows me / Vegetative Collapse",
                "body": """* **Psychodynamic Causality:** Total dopamine exhaustion following the manic run. The couch symbolizes dorsal vagal shutdown (freeze).
* **Body Language & Somatics:** Profound hypotonia, complete inability to mobilize musculoskeletal drive, drooping eyelids.
* **Power & Control Dynamics:** Absolute helplessness before neurochemical depletion.
* **Acoustic & Spatial Impact:** Viscous, suffocating low-end synth pads enveloping the frequency field."""
            },
            {
                "quote": "Only stayed because I hated you / Parasitic Contempt",
                "body": """* **Psychodynamic Causality:** Projective identification. Internal self-loathing is projected onto the partner and despised externally to spare the core ego.
* **Body Language & Somatics:** Retracted lips, flat cold detachment, drained ocular focus.
* **Power & Control Dynamics:** Decimating partner self-esteem as final compensatory fuel.
* **Acoustic & Spatial Impact:** Unsettlingly dry, hyper-proximate vocal capture without spatial room reverberation."""
            }
        ]
    },
    {
        "num": "09",
        "title": "Dopamin Spike",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Künstliche Erzeugung von Lebendigkeit durch Noradrenalin und Dopamin. Die Tachykardie wird als Beweis des Triumphes über die Schwerkraft gefeiert.
* **Körpersprache & Somatik:** Tachykardie, zittrige Finger, geweitete Pupillen, vibrierende Kiefermuskeln.
* **Macht- & Kontroll-Dynamik:** Chemische Allmachtsfantasie: Der Körper trotzt scheinbar allen biologischen Grenzen.
* **Akustische & räumliche Wirkung:** Pumpende Sidechain-Kompression auf schnellen Synth-Akkorden."""
            },
            {
                "quote": "Muss gar nicht wahr sein / Postfaktischer Affekt",
                "body": """* **Psychodynamische Kausalität:** Vollständige Abkopplung des Gefühls von der Realität. Wahr ist nur, was Dopamin ausschüttet; Fakten werden irrelevant.
* **Körpersprache & Somatik:** Ausladende Gestik, übersteigertes Sprechtempo (Logorrhoe), euphorisches Grinsen.
* **Macht- & Kontroll-Dynamik:** Konstruktion einer eigenen Scheinwelt, in der Widerspruch unmöglich ist.
* **Akustische & räumliche Wirkung:** Schillernde, perlende Höhen und Filter-Sweeps, die Euphorie stimulieren."""
            },
            {
                "quote": "Sonnenbrille bei Nacht / Der Matrix-Filter",
                "body": """* **Psychodynamische Kausalität:** Visuelle Dissoziation. Die Sonnenbrille schützt die geweiteten Pupillen vor Entlarvung und trennt das Ich von der Umwelt.
* **Körpersprache & Somatik:** Starrer Kopf, verdeckter Blickkontakt, kühle und unnahbare Körperhaltung.
* **Macht- & Kontroll-Dynamik:** Einseitige Beobachtung: Ich sehe dich, aber du kannst nicht in mich hineinsehen.
* **Akustische & räumliche Wirkung:** Dunkle, pulsierende Bassline mit metallischen Hi-Hats."""
            },
            {
                "quote": "High auf Moral / Die Entwertung der Tugend",
                "body": """* **Psychodynamische Kausalität:** Abwehr moralischer Schuldgefühle durch Entwertung der Moral des Gegenübers. Wer tugendhaft ist, wird als scheinheilig und schwach abqualifiziert.
* **Körpersprache & Somatik:** Spöttisches Lächeln, leichtes Abwinken mit dem Handgelenk, distanzierter Stand.
* **Macht- & Kontroll-Dynamik:** Moralischer Relativismus als Schutzschild gegen berechtigte Kritik.
* **Akustische & räumliche Wirkung:** Ein schneidender Vokal-Chop, der wie ein hämisches Lachen durch den Mix hallt."""
            }
        ],
        "cards_en": [
            {
                "quote": "Dopamine Spike & Racing Pulse / Neurochemical Elevation",
                "body": """* **Psychodynamic Causality:** Artificial ignition of vitality via noradrenergic flood. Tachycardia is celebrated as transcendence over gravity.
* **Body Language & Somatics:** Tachycardia, fine motor tremor in hands, dilated pupils, vibrating masseter.
* **Power & Control Dynamics:** Chemical omnipotence: the organism appears to conquer biological exhaustion.
* **Acoustic & Spatial Impact:** Pumping sidechain compression driving rapid synth pulses."""
            },
            {
                "quote": "Doesn't need to be true / Post-Factual Affect",
                "body": """* **Psychodynamic Causality:** Complete decoupling of emotional conviction from empirical truth. Truth is defined solely by neurochemical discharge.
* **Body Language & Somatics:** Grandiose sweeping gestures, pressured logorrhea, manic grin.
* **Power & Control Dynamics:** Fabrication of a solipsistic reality immune to contradiction.
* **Acoustic & Spatial Impact:** Shimmering high-register arpeggios and resonant filter sweeps."""
            },
            {
                "quote": "Sunglasses at night / The Matrix Filter",
                "body": """* **Psychodynamic Causality:** Visual dissociation. Dark lenses shield dilated pupils from inspection while isolating the self from external gaze.
* **Body Language & Somatics:** Rigid neck alignment, shielded ocular contact, cool impenetrable demeanor.
* **Power & Control Dynamics:** Asymmetrical surveillance: I observe you while withholding ocular reciprocity.
* **Acoustic & Spatial Impact:** Dark undulating bassline driving crisp metallic percussion."""
            },
            {
                "quote": "High on Morals / Devaluation of Virtue",
                "body": """* **Psychodynamic Causality:** Neutralizing ethical guilt by devaluing the partner's moral compass as hypocritical weakness.
* **Body Language & Somatics:** Mocking smirk, dismissive wrist gesture, aloof posture.
* **Power & Control Dynamics:** Radical moral relativism deployed against valid critique.
* **Acoustic & Spatial Impact:** Slicing vocal chop echoing across the stereo field like a taunt."""
            }
        ]
    },
    {
        "num": "10",
        "title": "Amnesia",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Reizüberflutung und akute sensorische Intoleranz. Das erzwungene Lächeln bricht zusammen; die Toilette wird zum letzten Rückzugsort für chemische Nachjustierung.
* **Körpersprache & Somatik:** Verkniffene Gesichtszüge, Zähneknirschen, hastige Atemfrequenz, klamme Hände.
* **Macht- & Kontroll-Dynamik:** Flucht aus der sozialen Verpflichtung des Geburtstags in die private Isolation der Clubtoilette.
* **Akustische & räumliche Wirkung:** Aggressive, dumpf pochende 4-to-the-floor Kicks mit schrillen, übersteuerten Leads."""
            },
            {
                "quote": "Box' dich nach England / Projektive Entlastung",
                "body": """* **Psychodynamische Kausalität:** Verschiebung innerer Frustration auf ein äußeres Feindbild. Der britische Tourist dient als idealer Blitzableiter für die eigene Ohnmacht.
* **Körpersprache & Somatik:** Geballte Fäuste, Vorstrecken des Kinns, plötzliche Adrenalinschwemme mit Vasokonstriktion.
* **Macht- & Kontroll-Dynamik:** Physische Dominanzbehauptung zur Wiederherstellung gekränkter Männlichkeit.
* **Akustische & räumliche Wirkung:** Harte, verzerrte Vocal-Kompression, die wie ein direkt ins Gesicht gebrüllter Schrei wirkt."""
            },
            {
                "quote": "Du kommst mir grade recht / Die Erlösungsfantasie",
                "body": """* **Psychodynamische Kausalität:** Gewalt als erlösende Katharsis. Der drohende Kampf wird nicht gefürchtet, sondern herbeigesehnt, um die quälende innere Spannung physisch zu entladen.
* **Körpersprache & Somatik:** Grinsen unter Hochspannung, federnder Kampfgang, rhythmische Atmung.
* **Macht- & Kontroll-Dynamik:** Transformation passiven Leidens in aktive Destruktion.
* **Akustische & räumliche Wirkung:** Ein stoisch repetitiver Beat-Loop, der die unausweichliche physische Kollision antreibt."""
            },
            {
                "quote": "CO2-Kanonen & Declan-Rice-Trikot / Choreografierte Eskalation",
                "body": """* **Psychodynamische Kausalität:** Verschmelzung von Club-Klimax und Schlägerei. Der Tritt erfolgt exakt auf dem musikalischen Drop – Gewalt wird zum integralen Teil des Ibiza-Spektakels.
* **Körpersprache & Somatik:** Explosive Kraftentfaltung im Moment des Reißens aus dem Griff des Sicherheitsdienstes; Trittbewegung.
* **Macht- & Kontroll-Dynamik:** Triumphales Aushebeln von Sicherheitsregeln und Verhaltenskodizes.
* **Akustische & räumliche Wirkung:** Druckvoller Bass-Drop, weißes Rauschen der CO2-Kanonen und berstende Synth-Wände."""
            }
        ],
        "cards_en": [
            {
                "quote": "EDM Purgatory & Bathroom Retreat / Sensory Overload",
                "body": """* **Psychodynamic Causality:** Acute sensory intolerance under club stimuli. The forced smile fractures; the bathroom cubicle serves as emergency shelter for chemical re-dosing.
* **Body Language & Somatics:** Pinched facial posture, bruxism, rapid shallow respiration, clammy palms.
* **Power & Control Dynamics:** Desertion of social obligations into isolated chemical privacy.
* **Acoustic & Spatial Impact:** Aggressive, booming four-on-the-floor kick drums clashing with harsh distorted synth leads."""
            },
            {
                "quote": "Punch you back to England / Displaced Rage",
                "body": """* **Psychodynamic Causality:** Displacement of internal shame onto a foreign target. The tourist becomes the lightning rod for narcissistic rage.
* **Body Language & Somatics:** Clenched fists, jutting mandible, explosive adrenaline discharge causing peripheral vasoconstriction.
* **Power & Control Dynamics:** Physical re-assertion of dominance repairing injured masculinity.
* **Acoustic & Spatial Impact:** Crushed, hyper-saturated vocal processing projecting raw spatial confrontation."""
            },
            {
                "quote": "You're just what I needed / Cathartic Violence",
                "body": """* **Psychodynamic Causality:** Physical altercation welcomed as somatic release. Violence relieves unbearable internal tension by externalizing conflict.
* **Body Language & Somatics:** High-tension grin, rhythmic boxing bounce, controlled heavy respiration.
* **Power & Control Dynamics:** Active mastery replacing passive emotional paralysis.
* **Acoustic & Spatial Impact:** Relentlessly driving beat loop propelling the physical impact."""
            },
            {
                "quote": "CO2 Cannons & Football Jersey / Choreographed Climax",
                "body": """* **Psychodynamic Causality:** Fusion of rave catharsis and physical violence. The kick lands exactly on the musical drop—turning brutality into club performance.
* **Body Language & Somatics:** Explosive kinetic release tearing free from security grasp, executing the strike.
* **Power & Control Dynamics:** Triumphant destruction of civil boundaries under club cover.
* **Acoustic & Spatial Impact:** Massive sub-bass impact combined with white noise CO2 blasts and exploding synth sweeps."""
            }
        ]
    },
    {
        "num": "11",
        "title": "Kaputt",
        "ytId": "",
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
                "body": """* **Psychodynamische Kausalität:** Das Springmesser-Tattoo auf der Brust als Wappen der permanenten Abwehrbereitschaft. Das Fehlen des Pulses markiert die vollendete emotionale Nekrose.
* **Körpersprache & Somatik:** Hand flach auf der Brust, erstarrte Atmung, vollständiges Ausbleiben emotionaler Resonanz im Herzbereich.
* **Macht- & Kontroll-Dynamik:** Wer innerlich tot ist, kann nicht mehr getötet oder verletzt werden.
* **Akustische & räumliche Wirkung:** Schwere, getragene Klavierakkorde mit subtilem Tape-Leiern, die Trauer und Verfall transportieren."""
            },
            {
                "quote": "Was ich berühr', geht kaputt / Der Midas-Fluch",
                "body": """* **Psychodynamische Kausalität:** Die Umkehrung des Midas-Mythos: Alles Berührte verwandelt sich nicht in Gold, sondern in Schutt. Destruktivität als unkontrollierbarer Schicksalsfluch.
* **Körpersprache & Somatik:** Kraftloses Öffnen der Hände, Abgleiten der Arme am Körper, gesenkter Kopf.
* **Macht- & Kontroll-Dynamik:** Kapitulation vor dem eigenen Zerstörungspotenzial.
* **Akustische & räumliche Wirkung:** Mächtige, verzerrte Synthesizer-Wände, die im Refrain wie einstürzende Gebäude anschwellen."""
            },
            {
                "quote": "Toter Hund & Nur 'ne Behauptung / Das entlarvte Ego",
                "body": """* **Psychodynamische Kausalität:** Radikale Entblößung des falschen Selbst. Die Erkenntnis, dass die gesamte grandiose Persönlichkeit nur eine substanzlose „Behauptung“ war.
* **Körpersprache & Somatik:** Blick auf den Boden, gebeugte Haltung, verlangsamter, schwerfälliger Schritt durch den Schutt.
* **Macht- & Kontroll-Dynamik:** Vollständiger Kollaps der narzisstischen Fassade.
* **Akustische & räumliche Wirkung:** Brüchige, leise Vokalführung, umgeben von weitem Meeresrauschen und Windgeräuschen."""
            },
            {
                "quote": "Immer davon, niemals an / Die ewige Flucht",
                "body": """* **Psychodynamische Kausalität:** Das Kern-Dilemma der Fluchtbiografie. Das Entkommen gelingt stets, doch die Ankunft an einem Ort des Friedens ist strukturell unmöglich.
* **Körpersprache & Somatik:** Blick zum fernen Horizont des Meeres, langsames Drehen des Körpers, Ausatmung ohne Erlösung.
* **Macht- & Kontroll-Dynamik:** Gefangenschaft im eigenen Bewegungsmuster.
* **Akustische & räumliche Wirkung:** Ein endlos ausklingender Synth-Drone, der sich langsam in weißem Rauschen auflöst."""
            }
        ],
        "cards_en": [
            {
                "quote": "Switchblade Tattoo & No Pulse / Somatic Necrosis",
                "body": """* **Psychodynamic Causality:** The switchblade tattoo over the sternum serves as an emblem of chronic defensive hostility. The absent pulse signifies total affective necrosis.
* **Body Language & Somatics:** Hand resting flat on chest, stopped thoracic rhythm, absence of visceral somatic resonance.
* **Power & Control Dynamics:** He who is already deceased cannot be killed or wounded.
* **Acoustic & Spatial Impact:** Solemn piano chords drenched in tape flutter conveying decay and irreversible loss."""
            },
            {
                "quote": "Whatever I touch breaks / Reverse Midas Curse",
                "body": """* **Psychodynamic Causality:** Inversion of the Midas myth: everything touched turns not to gold, but to rubble. Destructiveness experienced as an inescapable curse.
* **Body Language & Somatics:** Powerless opening of fingers, arms dropping limp along torso, lowered head.
* **Power & Control Dynamics:** Total surrender to the ego's own destructive compulsion.
* **Acoustic & Spatial Impact:** Monumental, saturated synth walls rising in the chorus like collapsing architecture."""
            },
            {
                "quote": "Dead dog in rubble / The False Self Exposed",
                "body": """* **Psychodynamic Causality:** Radical exposure of the false persona. The realization that grandiosity was merely an empty assertion without core foundation.
* **Body Language & Somatics:** Gaze locked onto gravel, hunched posture, heavy plodding strides through coastal debris.
* **Power & Control Dynamics:** Complete structural collapse of the narcissistic facade.
* **Acoustic & Spatial Impact:** Fragile, intimate vocal delivery cradled by distant ocean surf and wind."""
            },
            {
                "quote": "Always got away, never arrived / The Eternal Exil",
                "body": """* **Psychodynamic Causality:** The fundamental trauma of the flight narrative. Escape is always achieved, but arrival at genuine peace remains psychologically barred.
* **Body Language & Somatics:** Gaze fixed onto the distant marine horizon, slow rotation of the body, unresolved exhalation.
* **Power & Control Dynamics:** Imprisoned within one's own compulsive kinetic trajectory.
* **Acoustic & Spatial Impact:** An infinite decaying drone fading slowly into oceanic white noise."""
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
        for line in raw_body.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            line = re.sub(r'^\*\s*\*\*(.*?)\*\*\s*(.*)$', r'<p><strong>\1</strong> \2</p>', line)
            line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
            paragraphs.append(line)
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
        for line in raw_body.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            line = re.sub(r'^\*\s*\*\*(.*?)\*\*\s*(.*)$', r'<p><strong>\1</strong> \2</p>', line)
            line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
            paragraphs.append(line)
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

print(f"Generated 1:1 tomora-replica index.html: {len(final_code)} bytes")
