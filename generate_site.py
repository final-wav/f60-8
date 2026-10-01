import json
import os

# Exact 1:1 data structure matching final-wav/tomora
tracks_data = [
    {
        "num": "01",
        "title": "1996",
        "lyrics_stanzas": [
            {
                "title": "[Intro & Soundscape Exposition]",
                "lines": [
                    {"text": "Ego FM Ibiza — Sesenta punto ocho", "annotated": True, "card_idx": 0},
                    {"text": "1996... Der Beginn des Ikarus-Höhenflugs", "annotated": True, "card_idx": 1},
                    {"text": "Atmosphärisches Anschwellen von Synths & Breakbeats", "annotated": True, "card_idx": 2},
                    {"text": "Kalter Wind über der Bucht, die Motoren starten", "annotated": False}
                ]
            }
        ],
        "review_de": """<p>Das Album eröffnet nicht mit einer versöhnlichen Rückschau, sondern mit dem Schnitt einer Rasierklinge: <strong>„1996“</strong> fungiert als Exposition und biografische Sollbruchstelle. Eingerahmt von den Einspielern des fiktiven Senders <span class="lyric-quote-highlight">Ego FM Ibiza</span> betritt der Protagonist die Bühne einer künstlichen Mittelmeer-Traumwelt, in der jede Erinnerung an die provinzielle Enge durch puren kinetischen Antrieb ausgelöscht werden soll.</p>
<p>Die klangliche Architektur etabliert sofort das Leitmotiv des Projekts: Der Ikarus-Mythos. Der Aufstieg ist kein organisches Wachsen, sondern ein manisches Ausweichen vor der Schwerkraft. Die Breakbeats und ansteigenden Synthesizer simulieren den anflutenden Adrenalinspiegel vor dem Absprung – ein Nervensystem, das Ruhe als akute Lebensgefahr interpretiert.</p>""",
        "review_en": """<p>The album opens not with nostalgic contemplation, but with the clean slice of a scalpel: <strong>“1996”</strong> operates as both sonic prologue and psychological fault line. Framed by broadcasts from the fictional station <span class="lyric-quote-highlight">Ego FM Ibiza</span>, the protagonist steps onto the synthetic Mediterranean stage where all provincial memories are incinerated through sheer velocity.</p>
<p>The sonic architecture immediately establishes the central motif: the Icarus ascent. Elevation is not an organic maturation, but a manic flight from gravity. Skittering breakbeats and rising synth filters simulate the surging adrenaline of takeoff—a nervous system that registers stillness as mortal danger.</p>""",
        "cards_de": [
            {
                "quote": "Ego FM Ibiza / Die geschlossene Frequenz",
                "body": """* **Psychodynamische Kausalität:** Die Inszenierung eines eigenen Radiosenders (*Ego FM*) markiert das hermetisch abgeriegelte Bezugssystem des Narzissten. Die Außenwelt wird nur noch als gefiltertes Mediensignal wahrgenommen, um unkontrollierte emotionale Reize auszublenden.
* **Körpersprache & Somatik:** Fixierter Tunnelblick, leicht erhöhter Muskeltonus im Nackenbereich, motorische Unruhe, die durch das rhythmische Takten der Finger kompensiert wird.
* **Macht- & Kontroll-Dynamik:** Absolute Deutungshoheit über die eigene Realität. Wer den Sender kontrolliert, bestimmt, welche Gefühle überhaupt im Raum existieren dürfen.
* **Akustische & räumliche Wirkung:** Analoger UKW-Radiofilter mit dezentem Rauschen, der unvermittelt in einen voluminösen Stereo-Basskick umschlägt."""
            },
            {
                "quote": "1996 / Der Ikarus-Höhenflug",
                "body": """* **Psychodynamische Kausalität:** Die Jahreszahl 1996 setzt den Fixpunkt der Verdrängung. Hier begann die Umwandlung primärer Beschämung in grandiosen Größenwahn. Der Ikarus-Flug dient als Ersatzidentität.
* **Körpersprache & Somatik:** Aufgerichteter Brustkorb, forciertes Heben des Kinns bei gleichzeitig flacher, rein thorakaler Atmung.
* **Macht- & Kontroll-Dynamik:** Kompensatorischer Narzissmus. Indem man höher fliegt als alle anderen, entzieht man sich jedem Urteil von Gleichen.
* **Akustische & räumliche Wirkung:** Schwebende, ansteigende Pad-Texturen im oberen Frequenzspektrum, die das Gefühl von Höhenrausch und Bodenverlust erzeugen."""
            },
            {
                "quote": "Breakbeats & Synths / Der kinetische Schutzpanzer",
                "body": """* **Psychodynamische Kausalität:** Geschwindigkeit als Abwehrmechanismus. Solange der Beat läuft und der Körper in Bewegung bleibt, kann keine Selbstreflexion einsetzen.
* **Körpersprache & Somatik:** Tachykardie, Vorwärtsdrang der Gliedmaßen, Unterdrückung von Erschöpfungssignalen durch Adrenalinausschüttung.
* **Macht- & Kontroll-Dynamik:** Dominanz über den Zeittakt. Das Verlangsamen wird verweigert, um dem Partner keine Reaktionszeit zu gewähren.
* **Akustische & räumliche Wirkung:** Trockene, präzise 2-Step- und UK-Garage-Drums, die den Hörer ohne Vorwarnung in die Vorwärtsbewegung zwingen."""
            }
        ],
        "cards_en": [
            {
                "quote": "Ego FM Ibiza / The Closed Circuit",
                "body": """* **Psychodynamic Causality:** The radio station construct (*Ego FM*) symbolizes the solipsistic boundary of the narcissistic persona. External reality is reduced to a curated broadcast.
* **Body Language & Somatics:** Tunnel vision, hyper-toned cervical spine, micro-motor restlessness channeled through rhythmic tapping.
* **Power & Control Dynamics:** Total narrative monopoly. Controlling the broadcast dictates which emotional truths are permitted.
* **Acoustic & Spatial Impact:** Lo-fi FM radio filtering suddenly exploding into an uncompressed stereo sub-kick."""
            },
            {
                "quote": "1996 / The Icarus Trajectory",
                "body": """* **Psychodynamic Causality:** 1996 marks the foundational pivot where core shame was converted into compensatory grandiosity. Flight replaces vulnerable attachment.
* **Body Language & Somatics:** Elevated chest, raised chin, shallow thoracic breathing masking somatic dread.
* **Power & Control Dynamics:** Compensatory superiority. Ascending higher than others neutralizes the risk of peer judgment.
* **Acoustic & Spatial Impact:** Ascending high-register synth pads evoking vertigo and detachment from ground level."""
            },
            {
                "quote": "Breakbeats & Synths / Kinetic Insulation",
                "body": """* **Psychodynamic Causality:** Velocity as defense. Continuous acceleration prevents the onset of introspective grief.
* **Body Language & Somatics:** Tachycardia, restless forward motor drive, suppression of fatigue markers.
* **Power & Control Dynamics:** Temporal dominance. Refusing decelerations deprives others of boundary-setting space.
* **Acoustic & Spatial Impact:** Crisp 2-step garage rhythms driving immediate forward momentum."""
            }
        ]
    },
    {
        "num": "02",
        "title": "Wiedersehen",
        "lyrics_stanzas": [
            {
                "title": "[Bridge]",
                "lines": [
                    {"text": "Die Welt gehört denen, die sie sich nehmen", "annotated": True, "card_idx": 0},
                    {"text": "Die Welt gehört denen, die sie sich nehmen", "annotated": True, "card_idx": 0}
                ]
            },
            {
                "title": "[Outro]",
                "lines": [
                    {"text": "Ich steh' auf einer Fähre übers Mittelmeer", "annotated": True, "card_idx": 1},
                    {"text": "Seh' der weißen Spur im Wasser hinterher", "annotated": True, "card_idx": 1},
                    {"text": "Selig sind die Diebe", "annotated": True, "card_idx": 2},
                    {"text": "Ich nehme, was ich kriege", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p>In <strong>„Wiedersehen“</strong> vollzieht der Protagonist den maritimen Transit und formuliert zugleich sein rücksichtsloses Credo. Auf der Fähre übers Mittelmeer stehend, blickt er auf das schäumende Kielwasser – ein kraftvolles Symbol für die Vergänglichkeit und Austauschbarkeit aller hinterlassenen Bindungen.</p>
<p>Mit der schneidenden Formel <span class="lyric-quote-highlight">„Selig sind die Diebe / Ich nehme, was ich kriege“</span> pervertiert Tua die biblische Bergpredigt in ein Manifest räuberischer Autarkie. Das Gegenüber wird nicht mehr als Partner verhandelt, sondern als Ressource, die man abschöpft, bevor man die nächste Insel ansteuert.</p>""",
        "review_en": """<p>In <strong>“Wiedersehen”</strong> (Reunion / Parting), maritime transit crystallizes into an explicit predator manifesto. Standing on the ferry across the Mediterranean, the speaker watches the churning wake—a pristine metaphor for the ephemerality of discarded intimacy.</p>
<p>Through the inversion <span class="lyric-quote-highlight">“Blessed are the thieves / I take what I get”</span>, Tua subverts the Sermon on the Mount into an ethic of unapologetic extraction. The partner is stripped of subjectivity, reduced to fuel consumed prior to departure.</p>""",
        "cards_de": [
            {
                "quote": "Die Welt gehört denen, die sie sich nehmen",
                "body": """* **Psychodynamische Kausalität:** Darwinistische Rationalisierung. Das Ich rechtfertigt seine Ausbeutungsmuster als universelles Lebensgesetz, um Schuldgefühle im Vorfeld zu neutralisieren.
* **Körpersprache & Somatik:** Härte in den Kiefermuskeln, fester Stand gegen den Wellengang, unbewegte Mimik.
* **Macht- & Kontroll-Dynamik:** Aggressives Anspruchsdenken (Entitlement). Das Gegenüber existiert nur als Objekt der Inbesitznahme.
* **Akustische & räumliche Wirkung:** Repetitive Vokalschleife mit schwerem Hallraum, die wie ein unerbittliches Mantra im Stereofeld hämmert."""
            },
            {
                "quote": "Fähre übers Mittelmeer / Weiße Spur im Wasser",
                "body": """* **Psychodynamische Kausalität:** Dissipatives Motiv des Verschwindens. Das Kielwasser löst sich in Sekunden auf – so wie der Narzisst seine Bindungen spurlos aus dem Gedächtnis tilgt.
* **Körpersprache & Somatik:** Rückwärtsgewandter Blick ohne seelische Resonanz; Kältegefühl auf der Haut, das ignoriert wird.
* **Macht- & Kontroll-Dynamik:** Bindungsabbruch durch physische Distanzierung. Wer auf See ist, kann nicht zur Rechenschaft gezogen werden.
* **Akustische & räumliche Wirkung:** Tiefes Rauschen von Meereswellen, überlagert von melancholischen Synth-Arpeggios."""
            },
            {
                "quote": "Selig sind die Diebe / Ich nehme, was ich kriege",
                "body": """* **Psychodynamische Kausalität:** Sakralisierung des Egoismus. Der Diebstahl von Zuneigung und Vertrauen wird zur religiösen Tugend erhoben, um den eigenen moralischen Bankrott zu kaschieren.
* **Körpersprache & Somatik:** Zynisches Lächeln, Entlastung der Schultern durch vollkommene Abgabe moralischer Verantwortung.
* **Macht- & Kontroll-Dynamik:** Grenzverletzung ohne Reue. Dem Bestohlenen wird die Schuld an seiner eigenen Naivität zugeschoben.
* **Akustische & räumliche Wirkung:** Intime, trockene Vocal-Präsenz direkt auf der Center-Achse, die den Hörer mit der Kälte der Aussage konfrontiert."""
            }
        ],
        "cards_en": [
            {
                "quote": "The world belongs to those who take it",
                "body": """* **Psychodynamic Causality:** Darwinian rationalization. Exploitation is framed as natural law to pre-emptively abort guilt.
* **Body Language & Somatics:** Locked jaw, rigid stance against the swell, deadpan facial expression.
* **Power & Control Dynamics:** Entitlement posture. The other exists merely as property to be acquired.
* **Acoustic & Spatial Impact:** Repetitive vocal hook cycling relentlessly through wide stereo reverb."""
            },
            {
                "quote": "Ferry across the sea / White wake in the water",
                "body": """* **Psychodynamic Causality:** Motif of total erasure. The wake dissolves instantly, mirroring the ease with which attachment is forgotten.
* **Body Language & Somatics:** Backward gaze without emotional resonance; thermal blunting against ocean spray.
* **Power & Control Dynamics:** Flight into geographic insulation, eliminating relational accountability.
* **Acoustic & Spatial Impact:** Low-end maritime rumble textured with desolate synthesizer arpeggios."""
            },
            {
                "quote": "Blessed are the thieves / I take what I get",
                "body": """* **Psychodynamic Causality:** Sacralized solipsism. Inverting beatitudes to crown predatory behavior as sovereign virtue.
* **Body Language & Somatics:** Cynical half-smirk, somatic relief through moral detachment.
* **Power & Control Dynamics:** Unapologetic boundary crossing; blaming the victim for their generosity.
* **Acoustic & Spatial Impact:** Bone-dry center-channel vocal delivery confronting the listener with stark detachment."""
            }
        ]
    },
    {
        "num": "03",
        "title": "GluiV",
        "lyrics_stanzas": [
            {
                "title": "[Hook]",
                "lines": [
                    {"text": "Bauchtasche, Kokain, ich fick' alle", "annotated": True, "card_idx": 0},
                    {"text": "G, Louis V, Bauchtasche, Kokain, ich fick' alle", "annotated": True, "card_idx": 0},
                    {"text": "G, Louis V, Bauchtasche, Kokain, ich fick' alle", "annotated": True, "card_idx": 0}
                ]
            },
            {
                "title": "[Part 2]",
                "lines": [
                    {"text": "Marmorfliesen im Airbnb / Ihr Leihparadies", "annotated": True, "card_idx": 1},
                    {"text": "Riecht nach OP Summer Breeze, sie ist im One Piece", "annotated": True, "card_idx": 1},
                    {"text": "Indigoblau, Tropic of C, Alkohol fließt", "annotated": True, "card_idx": 1},
                    {"text": "Ihre mollige Freundin findet mich mies, und ich seh', sie sieht's", "annotated": True, "card_idx": 1}
                ]
            },
            {
                "title": "[Pre-Hook]",
                "lines": [
                    {"text": "Sonne im Zenit, ballert den Kopf weg", "annotated": True, "card_idx": 2},
                    {"text": "Pool türkis wie bei David Hockney", "annotated": True, "card_idx": 2},
                    {"text": "Bluetoothbox spielt Britney – „Toxic“", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p><strong>„GluiV“</strong> (G, Louis V) ist die pulsierende Herzkammer des hedonistischen Größenwahns. Das Arrangement entfaltet ein ultradetailliertes, steriles Stillleben des modernen Jetset-Narzissmus: Gemieteter Marmor im Airbnb, Designer-Bademode von <em>Tropic of C</em>, türkisblaue Pools im Stile von <em>David Hockney</em> und aus der Bluetooth-Box scheppert Britney Spears' <em>Toxic</em>.</p>
<p>Die aggressive Vulgarität der Hook (<span class="lyric-quote-highlight">„Bauchtasche, Kokain, ich fick' alle“</span>) fungiert als hysterischer Abwehrpanzer. Je bedrohlicher die innere Leere wird, desto lauter müssen Statussymbole und chemische Stimulanzien aufgefahren werden, um den drohenden Zusammenbruch zu übertönen.</p>""",
        "review_en": """<p><strong>“GluiV”</strong> (G, Louis V) represents the throbbing core of manic hedonism. The track sketches an immaculate, hyper-sterile tableau of contemporary narcissistic staging: rented Airbnb marble, <em>Tropic of C</em> designer swimwear, turquoise pools evoking <em>David Hockney</em>, and Britney Spears' <em>Toxic</em> blaring from a portable speaker.</p>
<p>The brutal vulgarity of the hook (<span class="lyric-quote-highlight">“Fanny pack, cocaine, I fuck everyone”</span>) operates as a manic firewall. The more acute the inner void becomes, the more frantically luxury signifiers and chemical stimulation are stacked to drown out the collapse.</p>""",
        "cards_de": [
            {
                "quote": "Bauchtasche, Kokain, ich fick' alle / G, Louis V",
                "body": """* **Psychodynamische Kausalität:** Manische Omnipotenz-Phantasie. Drogenrausch und Luxusmarken (*Louis Vuitton*) verschmelzen zu einem Schutzwall gegen Scham und Impotenzgefühle.
* **Körpersprache & Somatik:** Kiefermahlen, geweitete Pupillen, aggressive raumgreifende Gestik, vegetative Hypererregung.
* **Macht- & Kontroll-Dynamik:** Omnipräsente Abwertung aller Anwesenden („fick' alle“), um sich selbst über die Gruppe zu erheben.
* **Akustische & räumliche Wirkung:** Drückende 808-Bässe und stakkatoartige Vocal-Chops, die ein Gefühl von künstlicher Überstimulation erzeugen."""
            },
            {
                "quote": "Marmorfliesen / Ihr Leihparadies / Tropic of C",
                "body": """* **Psychodynamische Kausalität:** Die Tragik der geliehenen Identität. Nichts gehört dem Protagonisten wirklich; das Paradies ist gemietet, die Kulisse austauschbar.
* **Körpersprache & Somatik:** Posing am Poolrand, taxierender Blick auf Körper und Marken, Entkopplung von echter Sinnlichkeit.
* **Macht- & Kontroll-Dynamik:** Soziale Hierarchisierung nach optischen und materiellen Kriterien; feindselige Wahrnehmung von Kritikern („ihre Freundin findet mich mies“).
* **Akustische & räumliche Wirkung:** Cleane, glasige Synths mit sonnigem Hall, die sterile Exklusivität spürbar machen."""
            },
            {
                "quote": "David Hockney Pool / Britney – „Toxic“",
                "body": """* **Psychodynamische Kausalität:** Popkulturelle Spiegelung. Die Hockney-Ästhetik zitiert die vollkommene, leblose Oberfläche; Britneys *Toxic* benennt die Wahrheit des Spiels.
* **Körpersprache & Somatik:** Erstarren in der Pose unter sengender Sonne; Betäubung des Körpers durch Hitze und Alkohol.
* **Macht- & Kontroll-Dynamik:** Selbstinszenierung als Kunstobjekt. Wer zum Bild wird, kann nicht mehr verletzt werden.
* **Akustische & räumliche Wirkung:** Gefilterte Höhen und ein komprimierter Bluetooth-Lautsprecher-Effekt im Song-Intro."""
            }
        ],
        "cards_en": [
            {
                "quote": "Fanny pack, cocaine / G, Louis V",
                "body": """* **Psychodynamic Causality:** Manic omnipotence fantasy. Narcotics and luxury signifiers form an impenetrable barrier against shame.
* **Body Language & Somatics:** Bruxism, dilated pupils, aggressive expansive posturing, autonomic hyper-arousal.
* **Power & Control Dynamics:** Blanket devaluation of surroundings to enforce hierarchical supremacy.
* **Acoustic & Spatial Impact:** Crushing 808 subs and staccato vocal chops creating artificial sensory overload."""
            },
            {
                "quote": "Rented Paradise / Airbnb Marble / Tropic of C",
                "body": """* **Psychodynamic Causality:** Borrowed identity. The persona owns nothing authentic; paradise is leased on credit.
* **Body Language & Somatics:** Poolside posturing, appraising gaze, somatic detachment from organic sensuality.
* **Power & Control Dynamics:** Sorting peers by aesthetic capital; paranoid awareness of dissent.
* **Acoustic & Spatial Impact:** Glassy synthesizers draped in sun-drenched reverb capturing sterile exclusivity."""
            },
            {
                "quote": "David Hockney Pool / Britney's Toxic",
                "body": """* **Psychodynamic Causality:** Pop-cultural mirroring. Hockney evokes pristine, lifeless surfaces; Britney names the toxic reality.
* **Body Language & Somatics:** Freezing into photographic poses under blazing heat, numbed by alcohol.
* **Power & Control Dynamics:** Self-objectification into a sculpture to render oneself invulnerable.
* **Acoustic & Spatial Impact:** Bandpass-filtered highs simulating a portable speaker echoing across sun-baked tiles."""
            }
        ]
    },
    {
        "num": "04",
        "title": "Dachterrasse",
        "lyrics_stanzas": [
            {
                "title": "[Hook]",
                "lines": [
                    {"text": "Man muss aufhör'n, wenn's am besten ist", "annotated": True, "card_idx": 0},
                    {"text": "Aufhör'n, wenn's am besten ist", "annotated": True, "card_idx": 0},
                    {"text": "Man muss aufhör'n, wenn's am besten ist", "annotated": True, "card_idx": 0}
                ]
            },
            {
                "title": "[Outro]",
                "lines": [
                    {"text": "Man muss aufhör'n, wenn's am besten ist", "annotated": True, "card_idx": 1},
                    {"text": "Denn mit der Zeit wird alles lächerlich", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p><strong>„Dachterrasse“</strong> ist das kontemplative Zentrum des Projekts. Hoch über der Stadt stehend, seziert der Protagonist die unausweichliche Entwertung jeder menschlichen Erfahrung: <span class="lyric-quote-highlight">„Man muss aufhör'n, wenn's am besten ist / Denn mit der Zeit wird alles lächerlich“</span>.</p>
<p>Die scheinbare Lebensweisheit entpuppt sich als neurotischer Sabotage-Mechanismus. Weil der Narzisst die Phase der alltäglichen Ernüchterung und des Verfalls nicht ertragen kann, zerstört er Bindungen auf dem Höhepunkt, um die Illusion vollkommener Schönheit einzufrieren.</p>""",
        "review_en": """<p><strong>“Dachterrasse”</strong> (Rooftop Terrace) represents the contemplative eye of the storm. Elevated above the skyline, the speaker dissects the inevitable decay of all experience: <span class="lyric-quote-highlight">“You have to quit when it's at its best / Because with time, everything turns ridiculous”</span>.</p>
<p>What poses as worldly wisdom is in fact a preemptive sabotage reflex. Unable to tolerate the mundane reality of deepening intimacy, the narcissist detonates bonds at their peak to preserve an untarnished fantasy.</p>""",
        "cards_de": [
            {
                "quote": "Aufhör'n, wenn's am besten ist / Der Abbruch-Reflex",
                "body": """* **Psychodynamische Kausalität:** Präventive Selbstsabotage. Aus panischer Angst vor Zurückweisung oder Entzauberung beendet das Ich die Beziehung selbst.
* **Körpersprache & Somatik:** Rückzug der Hände in die Hosentaschen, Vermeidung von direktem Augenkontakt, Abwenden des Körpers zur Brüstung.
* **Macht- & Kontroll-Dynamik:** Kontrolle über das Beziehungsende. Wer als Erster geht, behält die scheinbare emotionale Oberhand.
* **Akustische & räumliche Wirkung:** Reduzierte Gitarrenakkorde und gefilterte Drum-Loops, die eine bittersüße, einsame Weite erzeugen."""
            },
            {
                "quote": "Die Dachterrasse / Die vertikale Isolation",
                "body": """* **Psychodynamische Kausalität:** Räumliche Überhöhung als Schutzraum. Von oben betrachtet werden Menschen zu unbedeutenden Figuren, was Empathie überflüssig macht.
* **Körpersprache & Somatik:** Blick nach unten auf die Lichter der Stadt, Gefühl von kühler Schwerelosigkeit im Brustbereich.
* **Macht- & Kontroll-Dynamik:** Vertikaler Machtanspruch. Distanz wird mit Souveränität verwechselt.
* **Akustische & räumliche Wirkung:** Offene Hallräume mit breiter Stereo-Staffelung, die die Höhe und Kälte des Ortes widerspiegeln."""
            },
            {
                "quote": "Denn mit der Zeit wird alles lächerlich",
                "body": """* **Psychodynamische Kausalität:** Zynische Abwertung von Intimität. Indem Tiefe als „lächerlich“ diffamiert wird, schützt sich die Psyche vor echter Verwundbarkeit.
* **Körpersprache & Somatik:** Abfälliges Schulterzucken, Erkalten des Gesichtsausdrucks, Senkung der Stimmlage.
* **Macht- & Kontroll-Dynamik:** Entwertung des Partners und der gemeinsamen Zeit, um Trauer unmöglich zu machen.
* **Akustische & räumliche Wirkung:** Abrupter Cut der Reverb-Fahne auf dem Wort „lächerlich“, der ein Gefühl von Leere hinterlässt."""
            }
        ],
        "cards_en": [
            {
                "quote": "Quit when it's best / Preemptive Sabotage",
                "body": """* **Psychodynamic Causality:** Preemptive abandonment. Driven by terror of exposure or rejection, the self terminates intimacy prematurely.
* **Body Language & Somatics:** Hands withdrawn into pockets, averted eye contact, torso oriented toward the ledge.
* **Power & Control Dynamics:** Monopolizing the exit. Leaving first secures the illusion of emotional invulnerability.
* **Acoustic & Spatial Impact:** Stripped-back guitar picking and low-passed beats creating desolate spatial breadth."""
            },
            {
                "quote": "The Rooftop / Vertical Insulation",
                "body": """* **Psychodynamic Causality:** Spatial elevation as emotional bunker. Seen from above, human beings are reduced to miniatures.
* **Body Language & Somatics:** Looking down at city lights, somatic chill across the chest.
* **Power & Control Dynamics:** Hierarchical detachment. Distance is conflated with sovereignty.
* **Acoustic & Spatial Impact:** Expansive hall reverb emphasizing cold, lofty isolation."""
            },
            {
                "quote": "Because with time, everything turns ridiculous",
                "body": """* **Psychodynamic Causality:** Cynical devaluation. Labeling depth as 'ridiculous' armors the ego against true vulnerability.
* **Body Language & Somatics:** Dismissive shrug, hardening affect, dropped pitch.
* **Power & Control Dynamics:** Invaliding shared history to render mourning impossible.
* **Acoustic & Spatial Impact:** Sudden gating of reverb tails on the final syllable, exposing the vacuum."""
            }
        ]
    },
    {
        "num": "05",
        "title": "Für mich",
        "lyrics_stanzas": [
            {
                "title": "[Part 2]",
                "lines": [
                    {"text": "Wir beide gehör'n zusamm'n", "annotated": True, "card_idx": 0},
                    {"text": "Wir gehör'n zusamm'n wie Größenwahn und Scheitern", "annotated": True, "card_idx": 0},
                    {"text": "Lass mich das Größte für dich sein", "annotated": True, "card_idx": 1},
                    {"text": "Und wenn es alles für mich bleibt, was ich erreicht hab'", "annotated": True, "card_idx": 1}
                ]
            },
            {
                "title": "[Hook & Bridge]",
                "lines": [
                    {"text": "Gib dich auf, auf für mich / Geb' mich auf für dich", "annotated": True, "card_idx": 2},
                    {"text": "Es mag egoistisch sein, doch ich will dich für mich allein", "annotated": True, "card_idx": 2},
                    {"text": "Was ich brauch', ist Sicherheit — Durch null kann man nicht mehr teil'n", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p>In <strong>„Für mich“</strong> erreicht die toxische Beziehungsdynamik ihre präziseste literarische Zuspitzung: <span class="lyric-quote-highlight">„Wir gehör'n zusamm'n wie Größenwahn und Scheitern“</span>. Die Partnerschaft wird nicht als Begegnung zweier Subjekte verhandelt, sondern als mathematische Unmöglichkeit: <span class="lyric-quote-highlight">„Durch null kann man nicht mehr teil'n“</span>.</p>
<p>Das Einfordern vollständiger Selbstaufgabe des Gegenübers dient der existenziellen Beruhigung des eigenen fragmentierten Ichs. Weil der Protagonist im Inneren eine absolute Nullstelle bewohnt, muss der Partner restlos einverleibt werden, um das Gefühl eigener Existenz zu simulieren.</p>""",
        "review_en": """<p>In <strong>“Für mich”</strong> (For Me), toxic enmeshment achieves its most precise literary phrasing: <span class="lyric-quote-highlight">“We belong together like grandiosity and failure”</span>. Partnership is framed not as mutual communion, but as mathematical impossibility: <span class="lyric-quote-highlight">“Division by zero is impossible”</span>.</p>
<p>Demanding the complete surrender of the partner functions as an emergency stabilizer for a shattered ego. Inhabiting an internal zero-point, the protagonist must consume the other entirely to simulate a cohesive sense of self.</p>""",
        "cards_de": [
            {
                "quote": "Wie Größenwahn und Scheitern / Die Zwangssymbiose",
                "body": """* **Psychodynamische Kausalität:** Dialektische Verstrickung. Manischer Aufstieg und vernichtender Fall bedingen einander wie die Rollen in einer toxischen Beziehung.
* **Körpersprache & Somatik:** Umklammernde Gesten, die Nähe erzwingen, während der Blick ins Leere wandert.
* **Macht- & Kontroll-Dynamik:** Unauflösbare Verknüpfung. Dem Partner wird eingeredet, dass außerhalb der Zerstörung kein Leben existiert.
* **Akustische & räumliche Wirkung:** Schleppender, schwerer Beat mit melancholischer Synth-Fläche, die wie eine zähe Flüssigkeit den Raum füllt."""
            },
            {
                "quote": "Lass mich das Größte für dich sein",
                "body": """* **Psychodynamische Kausalität:** Narzisstische Zufuhr als Überlebensbedingung. Das Selbstwertgefühl hängt vollständig von der Anbetung des Anderen ab.
* **Körpersprache & Somatik:** Flehende Kopfhaltung bei gleichzeitig forderndem Tonfall; Anspannung im Halsbereich.
* **Macht- & Kontroll-Dynamik:** Erpressung von Loyalität. Jede Regung von Eigenständigkeit des Partners wird als Bedrohung empfunden.
* **Akustische & räumliche Wirkung:** Schwebende Vokalharmonie, die das Betteln um Bestätigung akustisch verdoppelt."""
            },
            {
                "quote": "Durch null kann man nicht mehr teil'n",
                "body": """* **Psychodynamische Kausalität:** Die mathematische Metapher des Nichts. Wo kein stabiles Selbst vorhanden ist, ist partnerschaftliches Teilen eine logische Unmöglichkeit.
* **Körpersprache & Somatik:** Erstarrung der Mimik; Hände fallen kraftlos herab.
* **Macht- & Kontroll-Dynamik:** Absoluter Besitzanspruch („für mich allein“). Aus der eigenen Leere wird das Recht auf totale Vereinnahmung abgeleitet.
* **Akustische & räumliche Wirkung:** Ausdünnung des Instrumentals auf eine einzelne Sub-Bass-Linie und nackte Vocals."""
            }
        ],
        "cards_en": [
            {
                "quote": "Like grandiosity and failure / Compulsive Symbiosis",
                "body": """* **Psychodynamic Causality:** Dialectical enmeshment. Manic flight and collapse form an unbreakable circuit mirrored in the relationship.
* **Body Language & Somatics:** Clinging embrace forcing physical proximity while gaze drifts into the void.
* **Power & Control Dynamics:** Enforced codependency; convincing the partner that no reality exists outside the mutual ruin.
* **Acoustic & Spatial Impact:** Sluggish, weighted groove beneath brooding synth textures filling the stereo field."""
            },
            {
                "quote": "Let me be the greatest for you",
                "body": """* **Psychodynamic Causality:** Narcissistic supply as life support. Self-worth is entirely outsourced to the partner's adoration.
* **Body Language & Somatics:** Pleading posture paired with commanding inflection; vocal strain.
* **Power & Control Dynamics:** Emotional extortion; treating any hint of partner autonomy as treason.
* **Acoustic & Spatial Impact:** Layered vocal harmonies reinforcing the desperate demand for validation."""
            },
            {
                "quote": "Division by zero is impossible",
                "body": """* **Psychodynamic Causality:** Mathematical nihilism. Where no cohesive self exists, authentic sharing is structurally impossible.
* **Body Language & Somatics:** Flat affect, limp hands dropping to the side.
* **Power & Control Dynamics:** Total territorial claim ('for me alone'). Inward emptiness fuels absolute possessiveness.
* **Acoustic & Spatial Impact:** Instrumental strips down to a lone sub-bass note and naked center-channel vocals."""
            }
        ]
    },
    {
        "num": "06",
        "title": "Rette mich nicht",
        "lyrics_stanzas": [
            {
                "title": "[Part 2]",
                "lines": [
                    {"text": "Go-go-Girls geh'n private, die Dämmerung glüht", "annotated": True, "card_idx": 0},
                    {"text": "Während du vorm Handy daheim sitzt und überlegst, was du fühlst", "annotated": True, "card_idx": 0},
                    {"text": "Lass mich einfach sein, wer ich sein will", "annotated": True, "card_idx": 1},
                    {"text": "Ich bin das Problem und ich weiß es — nur macht es das nicht kleiner, Gianna", "annotated": True, "card_idx": 1}
                ]
            },
            {
                "title": "[Hook & Bridge]",
                "lines": [
                    {"text": "Rette mich nicht, ich bin nicht wie die andern", "annotated": True, "card_idx": 2},
                    {"text": "Ich hass' dich nicht, du bist mir bloß egal", "annotated": True, "card_idx": 2},
                    {"text": "Wie leichte Versprechen auf weißen Tabletten in Zeitraffer-Nächten", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p>In <strong>„Rette mich nicht“</strong> spricht der Protagonist die unverblümte Wahrheit mit schneidender Kälte aus: <span class="lyric-quote-highlight">„Ich bin das Problem und ich weiß es – nur macht es das nicht kleiner, Gianna“</span>. Die persönliche Adressierung durchbricht für einen Moment die Abstraktion und zeigt das reale Opfer der Verwüstung.</p>
<p>Die schonungslose Demütigung <span class="lyric-quote-highlight">„Ich hass' dich nicht, du bist mir bloß egal“</span> schneidet tiefer als Wut. Indem dem Partner jede emotionale Relevanz aberkannt wird, wehrt das lyrische Ich jeden therapeutischen Rettungsversuch ab und flieht in die Narkose weißer Tabletten.</p>""",
        "review_en": """<p>In <strong>“Rette mich nicht”</strong> (Do Not Save Me), raw clarity surfaces with surgical chill: <span class="lyric-quote-highlight">“I am the problem and I know it—it just doesn't make it smaller, Gianna”</span>. Naming the real partner shatters abstraction, exposing the collateral damage of his path.</p>
<p>The chilling dismissal <span class="lyric-quote-highlight">“I don't hate you, you just don't matter to me”</span> cuts deeper than hostility. Denying the partner even the dignity of being hated, the speaker rejects salvation and retreats into chemical oblivion.</p>""",
        "cards_de": [
            {
                "quote": "Go-go-Girls / Während du vorm Handy sitzt",
                "body": """* **Psychodynamische Kausalität:** Räumliche Spaltung. Das Ausleben flüchtiger Triebe auf Ibiza steht im scharfen Kontrast zur stillen Verzweiflung der zurückgelassenen Partnerin.
* **Körpersprache & Somatik:** Flucht in grelles Clublicht; Verdrängung des schlechten Gewissens durch Sinnesüberreizung.
* **Macht- & Kontroll-Dynamik:** Schamlose Asymmetrie. Der Narzisst fordert Freiheit ein, während er das Leiden des Gegenübers ungerührt hinnimmt.
* **Akustische & räumliche Wirkung:** Druckvoller Club-Beat mit warmen Rhodes-Pianos, die Melancholie und hedonistischen Rausch vereinen."""
            },
            {
                "quote": "Ich bin das Problem und ich weiß es / Gianna",
                "body": """* **Psychodynamische Kausalität:** Luzide Weigerung. Die Selbsterkenntnis führt nicht zur Reue, sondern wird als Ausrede genutzt, um zerstörerisches Verhalten fortzusetzen.
* **Körpersprache & Somatik:** Direkter, fast unbarmherziger Blickkontakt; ruhige, unaufgeregte Stimmführung ohne Schuldausdruck.
* **Macht- & Kontroll-Dynamik:** Entwaffnung des Gegenübers. Wer seine eigenen Fehler vorwegnimmt, entzieht dem anderen jedes Argument.
* **Akustische & räumliche Wirkung:** Die Musik tritt für den Namen „Gianna“ kurz in den Hintergrund, wodurch der Moment maximale Schärfe erhält."""
            },
            {
                "quote": "Du bist mir bloß egal / Weiße Tabletten",
                "body": """* **Psychodynamische Kausalität:** Die ultimative Entwertung. Gleichgültigkeit ist der finale Schutzwall gegen Intimität; Tabletten beschleunigen die Flucht vor Konsequenzen.
* **Körpersprache & Somatik:** Abflachen aller affektiven Reaktionen, verlangsamter Lidschlag, gefühllose Extremitäten.
* **Macht- & Kontroll-Dynamik:** Zerstörung des Selbstwerts des Partners durch absolute Nichtbeachtung.
* **Akustische & räumliche Wirkung:** Schwebende Vocal-Echos mit langem Delay, die das Gefühl von Betäubung und Zeitraffer akustisch greifbar machen."""
            }
        ],
        "cards_en": [
            {
                "quote": "Go-go Girls / Sitting by the phone",
                "body": """* **Psychodynamic Causality:** Spatial split. Transient Ibiza hedonism sharply contrasted against the quiet grief of the abandoned partner.
* **Body Language & Somatics:** Retreat into strobes and noise to suppress somatic guilt.
* **Power & Control Dynamics:** Brazen asymmetry. Demanding total liberty while passively watching the partner suffer.
* **Acoustic & Spatial Impact:** Punchy four-on-the-floor groove balanced against warm Rhodes piano chords."""
            },
            {
                "quote": "I am the problem / Gianna",
                "body": """* **Psychodynamic Causality:** Lucid refusal. Insight without reform; weaponizing self-awareness as an excuse for continued damage.
* **Body Language & Somatics:** Steady, unblinking eye contact; quiet cadence devoid of remorse.
* **Power & Control Dynamics:** Preemptive disarming. Admitting fault strips the other of conversational leverage.
* **Acoustic & Spatial Impact:** Music dips beneath the name 'Gianna', lending the line acute intimacy."""
            },
            {
                "quote": "You just don't matter / White pills",
                "body": """* **Psychodynamic Causality:** Total emotional blunting. Indifference acts as ultimate armor; pharmaceuticals accelerate time-lapse evasion.
* **Body Language & Somatics:** Flat affect, slow blinking, somatic numbness.
* **Power & Control Dynamics:** Obliterating partner self-worth through calculated apathy.
* **Acoustic & Spatial Impact:** Floating vocal delays creating an auditory sensation of pharmacological drifting."""
            }
        ]
    },
    {
        "num": "07",
        "title": "Leicht",
        "lyrics_stanzas": [
            {
                "title": "[Hook & Bridge]",
                "lines": [
                    {"text": "Mach' es mir leicht, mach' es mir leicht", "annotated": True, "card_idx": 0},
                    {"text": "Trying to feel alright all the time", "annotated": True, "card_idx": 0},
                    {"text": "Versuch' die ganze Zeit, mich gut zu fühl'n", "annotated": True, "card_idx": 1},
                    {"text": "Love, love passing by", "annotated": True, "card_idx": 1}
                ]
            },
            {
                "title": "[Outro]",
                "lines": [
                    {"text": "Sie will ballern, ich schenk' ihr ein Gramm", "annotated": True, "card_idx": 2},
                    {"text": "„Meld dich“, sagt sie, ich denke nicht dran", "annotated": True, "card_idx": 2},
                    {"text": "„Danke für den nicen Abend“, sagt sie / „Ja“, sag' ich und schließ' die Tür von ihr'm Taxi", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p>In <strong>„Leicht“</strong> verhandelt Tua das Diktat der permanenten Hochstimmung: <span class="lyric-quote-highlight">„Trying to feel alright all the time“</span>. Eingebettet in fluffigen Balearic House wird die Zwanghaftigkeit spürbar, mit der Schmerz und Schwere verdrängt werden müssen.</p>
<p>Das Outro skizziert die urbane Beiläufigkeit mit fotografischer Präzision: Ein Gramm als Abschiedsgeschenk, ein heuchlerisches „Meld dich“ und das dumpfe Zuschlagen der Taxitür. Menschliche Begegnungen werden wie Konsumgüter abgefertigt.</p>""",
        "review_en": """<p>In <strong>“Leicht”</strong> (Light / Effortless), Tua captures the tyranny of mandatory good vibes: <span class="lyric-quote-highlight">“Trying to feel alright all the time”</span>. Wrapped in breezy Balearic house grooves, compulsory euphoria reveals its defensive core.</p>
<p>The outro captures urban detachment with cinematic brevity: handing over a gram as a parting gift, a fake 'keep in touch', and the definitive thud of a closing taxi door. Human connection processed like fast-food consumption.</p>""",
        "cards_de": [
            {
                "quote": "Trying to feel alright all the time",
                "body": """* **Psychodynamische Kausalität:** Die Manie der Schwerelosigkeit. Der Zwang zur ununterbrochenen Euphorie ist die extremste Form der Traumaleugnung.
* **Körpersprache & Somatik:** Angestrengtes Lächeln, tänzerische Wippbewegungen, die innere Erstarrung überspielen.
* **Macht- & Kontroll-Dynamik:** Verbot von Negativität. Wer Schmerz äußert, wird sofort als toxischer Ballast aussortiert.
* **Akustische & räumliche Wirkung:** Schwebende Vocal-Chops und treibende House-Percussions im sonnigen Panorama."""
            },
            {
                "quote": "Love passing by / Die verpasste Liebe",
                "body": """* **Psychodynamische Kausalität:** Liebe als vorbeiziehendes Phänomen. Der Protagonist kann Intimität nur aus der Distanz beobachten, ohne jemals selbst teilzuhaben.
* **Körpersprache & Somatik:** Sehnsüchtiger Blick ins Leere, gefolgt von sofortiger Abwendung.
* **Macht- & Kontroll-Dynamik:** Passive Isolation. Indem man Liebe als unerreichbares Schicksal darstellt, entzieht man sich der Verantwortung für eigene Bindungsunfähigkeit.
* **Akustische & räumliche Wirkung:** Verträumte Synth-Flächen mit weichem Filter-Sweep."""
            },
            {
                "quote": "Schließ' die Tür von ihr'm Taxi / Das saubere Ende",
                "body": """* **Psychodynamische Kausalität:** Das hermetische Ritual. Das Zuschlagen der Autotür ist der akustische Schlussstrich unter jede flüchtige Bekanntschaft.
* **Körpersprache & Somatik:** Schnelle, routinierte Bewegung der rechten Hand; sofortiges Umdrehen und Zurückgehen in die eigene Welt.
* **Macht- & Kontroll-Dynamik:** Beendigung des Kontakts nach eigenem Fahrplan ohne Raum für Nachfragen.
* **Akustische & räumliche Wirkung:** Trockenes, abruptes Ausklingen der Instrumentierung, das die Kälte des Moments unterstreicht."""
            }
        ],
        "cards_en": [
            {
                "quote": "Trying to feel alright all the time",
                "body": """* **Psychodynamic Causality:** Compulsory euphoria. The manic demand to feel great is the ultimate defense against underlying trauma.
* **Body Language & Somatics:** Strained smile, bouncing motor rhythm masking internal freeze.
* **Power & Control Dynamics:** Outlawing sadness; discarding anyone who exhibits vulnerability as toxic baggage.
* **Acoustic & Spatial Impact:** Shimmering vocal chops and buoyant house percussion across a wide stereo stage."""
            },
            {
                "quote": "Love passing by",
                "body": """* **Psychodynamic Causality:** Love as detached spectator sport. Intimacy is observed from afar without active engagement.
* **Body Language & Somatics:** Wistful gaze followed by abrupt somatic closure.
* **Power & Control Dynamics:** Fatalistic alibi. Framing love as unreachable pardons one's own incapacity for bonding.
* **Acoustic & Spatial Impact:** Dreamy synth pads washing through gentle low-pass filter sweeps."""
            },
            {
                "quote": "Closing her taxi door / The Surgical Exit",
                "body": """* **Psychodynamic Causality:** Hermetic closure. The slam of the car door marks the absolute terminus of transient encounters.
* **Body Language & Somatics:** Practiced flick of the wrist; immediate about-face.
* **Power & Control Dynamics:** Ending contact on private terms with zero room for residual questions.
* **Acoustic & Spatial Impact:** Abrupt muting of background elements emphasizing emotional frost."""
            }
        ]
    },
    {
        "num": "08",
        "title": "Höhenflug + Tiefenrausch",
        "lyrics_stanzas": [
            {
                "title": "[Part 2]",
                "lines": [
                    {"text": "Kann mich nicht bewegen, alles klemmt", "annotated": True, "card_idx": 0},
                    {"text": "Hing nur mit dir rum, weil ich dich so gehasst hab'", "annotated": True, "card_idx": 0},
                    {"text": "Alkohol macht mich zu einer fetten Schnecke", "annotated": True, "card_idx": 1},
                    {"text": "Hundert Meter tief in mein'n Augenhöhl'n, lieg' in der Wanne, versuch' mich aufzulösen", "annotated": True, "card_idx": 1}
                ]
            },
            {
                "title": "[Hook & Bridge]",
                "lines": [
                    {"text": "Die Couch schluckt mich und spuckt mich nie mehr aus", "annotated": True, "card_idx": 2},
                    {"text": "Alle Energie verbraucht, falle durch die Welt, bin im Fiebertraum", "annotated": True, "card_idx": 2},
                    {"text": "Hör' jetzt Stimmen schweigen, der Heldensaal ist leer", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p>In <strong>„Höhenflug + Tiefenrausch“</strong> bricht der physische und psychische Kater mit voller Brutalität herein. Die Zeile <span class="lyric-quote-highlight">„Hing nur mit dir rum, weil ich dich so gehasst hab'“</span> entlarvt den sadomasochistischen Charakter toxischer Bindung: Der Andere wird nicht trotz, sondern wegen des Hasses aufgesucht, um den eigenen Selbstekel zu spiegeln.</p>
<p>Das Bild der Couch, die den Protagonisten verschlingt, und der leere <span class="lyric-quote-highlight">„Heldensaal“</span> markieren den Absturz von Ikarus: Auf dem Boden der Badewanne liegend, bleibt vom einstigen Glanz nur noch die Sehnsucht nach vollständiger molekularer Auflösung.</p>""",
        "review_en": """<p>In <strong>“Höhenflug + Tiefenrausch”</strong> (High Altitude Flight + Deep Intoxication), somatic and psychic collapse strikes with unfiltered brutality. The confession <span class="lyric-quote-highlight">“Only hung around because I hated you so much”</span> exposes the sadomasochistic core: the partner is sought out precisely to mirror externalized self-hatred.</p>
<p>The sofa that swallows the speaker and the empty <span class="lyric-quote-highlight">“hall of heroes”</span> chronicle the crash of Icarus: lying at the bottom of the bathtub, nothing remains of grandiosity save the craving for complete molecular dissolution.</p>""",
        "cards_de": [
            {
                "quote": "Hing mit dir rum, weil ich dich gehasst hab'",
                "body": """* **Psychodynamische Kausalität:** Projektive Identifikation. Der eigene verdrängte Selbsthass wird auf den Partner projiziert und dort obsessiv bekämpft.
* **Körpersprache & Somatik:** Somatischer Freeze-Zustand („alles klemmt“), bleierne Schwere in den Gliedmaßen, Bewegungsunfähigkeit.
* **Macht- & Kontroll-Dynamik:** Destruktive Bindung. Hass bindet stärker als Liebe und verhindert jede echte Loslösung.
* **Akustische & räumliche Wirkung:** Drückende, verlangsamte Drums mit metallisch verzerrten Synth-Bässen."""
            },
            {
                "quote": "Lieg' in der Wanne, versuch' mich aufzulösen",
                "body": """* **Psychodynamische Kausalität:** Somatische Regression. Das warme Wasser der Wanne fungiert als intrauteriner Rückzugsort vor den Anforderungen der Realität.
* **Körpersprache & Somatik:** Eingesunkene Haltung, tiefe Augenhöhlen, vollständiger Tonusverlust der Muskulatur.
* **Macht- & Kontroll-Dynamik:** Kapitulation des Willens. Das Ego gibt alle Kontrollansprüche auf und wünscht sich Nicht-Existenz.
* **Akustische & räumliche Wirkung:** Gedämpfte Unterwasser-Akustik mit sanftem Reverb und tieffrequenten Drones."""
            },
            {
                "quote": "Der Heldensaal ist leer / Couch schluckt mich",
                "body": """* **Psychodynamische Kausalität:** Der Einsturz der narzisstischen Bühne. Wo eben noch Beifall und Rausch herrschten, bleibt nur noch gähnende Öde.
* **Körpersprache & Somatik:** Apathisches Versinken im Sofa, unfähig den Kopf aufrecht zu halten.
* **Macht- & Kontroll-Dynamik:** Vollständiger Machtverlust gegenüber der eigenen Erschöpfung.
* **Akustische & räumliche Wirkung:** Raumgreifender, dunkler Hall, der die Verlassenheit des Raumes fühlbar macht."""
            }
        ],
        "cards_en": [
            {
                "quote": "Hung out because I hated you",
                "body": """* **Psychodynamic Causality:** Projective identification. Repressed self-hatred is projected onto the partner and obsessively engaged.
* **Body Language & Somatics:** Somatic freeze ('everything stuck'), leaden limb heaviness, motor paralysis.
* **Power & Control Dynamics:** Destructive enmeshment. Hatred binds tighter than love, sabotaging authentic release.
* **Acoustic & Spatial Impact:** Heavy, dragging beat distorted through metallic sub-bass frequencies."""
            },
            {
                "quote": "Lying in the tub, trying to dissolve",
                "body": """* **Psychodynamic Causality:** Somatic regression. Warm bathtub water operates as an intra-uterine sanctuary from reality.
* **Body Language & Somatics:** Sunken frame, hollowed eye sockets, total loss of postural muscle tone.
* **Power & Control Dynamics:** Surrender of will. The ego abandons mastery, craving pure non-existence.
* **Acoustic & Spatial Impact:** Muffled underwater acoustics layered with gentle low-end drones."""
            },
            {
                "quote": "The hall of heroes is empty",
                "body": """* **Psychodynamic Causality:** Collapse of the vanity stage. Applause vanishes, leaving behind desolate wasteland.
* **Body Language & Somatics:** Apathetic sink into the upholstery, unable to lift the neck.
* **Power & Control Dynamics:** Complete powerlessness against neurochemical depletion.
* **Acoustic & Spatial Impact:** Cavernous, dark reverb capturing the vacant isolation of the room."""
            }
        ]
    },
    {
        "num": "09",
        "title": "Dopamin Spike",
        "lyrics_stanzas": [
            {
                "title": "[Part 2]",
                "lines": [
                    {"text": "Wartest auf Erlaubnis für all die Dinge, die du nicht mal aussprichst", "annotated": True, "card_idx": 0},
                    {"text": "High auf Moral, doch ich glaub's nicht", "annotated": True, "card_idx": 0},
                    {"text": "Denn es ist deine Wahrheit, wegen der du so taub bist / Solang, bis du drauf bist", "annotated": True, "card_idx": 1}
                ]
            },
            {
                "title": "[Hook & Outro]",
                "lines": [
                    {"text": "Dann fühlst du es auch — die Schmetterlinge im Bauch", "annotated": True, "card_idx": 2},
                    {"text": "Und dir ist alles egal, die könn'n lang auf dich warten", "annotated": True, "card_idx": 2},
                    {"text": "Ego FM Ibiza, Yours truly — Trayéndote el fuego", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p>In <strong>„Dopamin Spike“</strong> dekonstruiert Tua den Zynismus moderner Reizüberflutung. Moralische Bedenken werden als feige Lebensverweigerung verhöhnt (<span class="lyric-quote-highlight">„High auf Moral, doch ich glaub's nicht“</span>). Gefühle existieren nicht mehr als organische Zwischenmenschlichkeit, sondern als neurochemischer Impuls auf Knopfdruck.</p>
<p>Die „Schmetterlinge im Bauch“ sind hier kein Liebesbeweis, sondern das Resultat eines künstlichen Dopamin-Peaks. Eingerahmt von spanischen Radio-Jingles feiert der Track die Kapitulation vor dem schnellen Kick.</p>""",
        "review_en": """<p>In <strong>“Dopamin Spike”</strong>, Tua deconstructs modern sensory cynicism. Moral hesitation is mocked as cowardice (<span class="lyric-quote-highlight">“High on morality, but I don't buy it”</span>). Emotion ceases to exist as organic reciprocity, reduced to on-demand neurochemical surges.</p>
<p>Butterflies in the stomach no longer signify romance, but the physiological spike of synthetic dopamine. Framed by Latin radio drops, the song toasts to sensory capitulation.</p>""",
        "cards_de": [
            {
                "quote": "High auf Moral / Wartest auf Erlaubnis",
                "body": """* **Psychodynamische Kausalität:** Verachtung ethischer Grenzen. Der Narzisst stilisiert seine Hemmungslosigkeit zur einzig wahren Freiheit hoch.
* **Körpersprache & Somatik:** Herausfordernder Blick, herablassendes Schmunzeln, aufrechter Oberkörper.
* **Macht- & Kontroll-Dynamik:** Beschämung des Gegenübers. Wer zögert, wird als spießig und schwach abgestempelt.
* **Akustische & räumliche Wirkung:** Glasklare Hi-Hats und trockene Trap-Snares im rhythmischen Vorwärtsdrang."""
            },
            {
                "quote": "Taub bist, solang bis du drauf bist",
                "body": """* **Psychodynamische Kausalität:** Die chemische Erweckung. Die natürliche Gefühlswelt ist so abgestumpft, dass nur noch extreme Dosen Resonanz erzeugen.
* **Körpersprache & Somatik:** Zittern der Fingerkuppen vor dem nächsten Peak, gefolgt von plötzlicher Entspannung.
* **Macht- & Kontroll-Dynamik:** Verführung des Partners in dieselbe Suchtdynamik, um nicht allein im Abgrund zu stehen.
* **Akustische & räumliche Wirkung:** Schwebende Flanger-Effekte auf den Vocals, die das Anfluten der Substanz abbilden."""
            },
            {
                "quote": "Schmetterlinge im Bauch / Trayéndote el fuego",
                "body": """* **Psychodynamische Kausalität:** Die Simulation von Verliebtheit. Synthetische Euphorie ersetzt die Fähigkeit zu echter Herzenswärme.
* **Körpersprache & Somatik:** Weite Pupillen, leicht geöffneter Mund, ekstatische Bewegung im Takt der Musik.
* **Macht- & Kontroll-Dynamik:** Gleichgültigkeit gegenüber der Außenwelt („die könn'n lang auf dich warten“).
* **Akustische & räumliche Wirkung:** Warme, pumpende House-Bässe und sonnige Vocal-Samples."""
            }
        ],
        "cards_en": [
            {
                "quote": "High on morality / Waiting for permission",
                "body": """* **Psychodynamic Causality:** Ethical cynicism. The narcissist crowns impulsivity as the only genuine liberty.
* **Body Language & Somatics:** Defiant gaze, condescending smirk, upright chest.
* **Power & Control Dynamics:** Shaming restraint. Caution is branded as boring weakness.
* **Acoustic & Spatial Impact:** Laser-sharp hi-hats and crisp snares driving forward urgency."""
            },
            {
                "quote": "Numb until you're high",
                "body": """* **Psychodynamic Causality:** Chemical awakening. Organic affect is so blunted that only pharmacological surges produce sensation.
* **Body Language & Somatics:** Tremor in fingertips anticipating the peak, followed by sudden relaxation.
* **Power & Control Dynamics:** Luring the partner into shared addiction to avoid solitary ruin.
* **Acoustic & Spatial Impact:** Sweeping flanger sweeps across the vocals simulating the onset."""
            },
            {
                "quote": "Synthetic Butterflies / Bringing the fire",
                "body": """* **Psychodynamic Causality:** Simulated romance. Neurochemical surges substitute for authentic emotional warmth.
* **Body Language & Somatics:** Dilated pupils, slightly parted lips, ecstatic physical syncing with the beat.
* **Power & Control Dynamics:** Complete disregard for outside obligations ('they can wait forever').
* **Acoustic & Spatial Impact:** Pumping house basslines textured with sun-kissed vocal cuts."""
            }
        ]
    },
    {
        "num": "10",
        "title": "Amnesia",
        "lyrics_stanzas": [
            {
                "title": "[Part 2]",
                "lines": [
                    {"text": "Der Secu ist so breit wie hoch / Hält mich, hält mich fest, währ'nd der mir weiter droht", "annotated": True, "card_idx": 0},
                    {"text": "Sonn'nbrand-Fresse hinter sein'n beiden Bros / Unter weiß-roten Pyramiden und Kaleidoskop", "annotated": True, "card_idx": 0},
                    {"text": "Sag' dem Secu: „Tranquilo, I go home“ — Warte auf den Drop und die CO2-Kanon'n", "annotated": True, "card_idx": 1},
                    {"text": "Kalter Rauch, reiß' mich los und tret' ihm in sein Declan-Rice-Trikot", "annotated": True, "card_idx": 1}
                ]
            },
            {
                "title": "[Hook]",
                "lines": [
                    {"text": "Du kommst mir grade recht, Junge, willst du, dass ich dir die Nase brech'?", "annotated": True, "card_idx": 2},
                    {"text": "Du kommst mir grade recht...", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p>In <strong>„Amnesia“</strong> schlägt die verdrängte Agonie in rohe physische Gewalt um. Der legendäre Ibiza-Club wird zum Schauplatz narzisstischer Wut (*Narcissistic Rage*): Zwischen CO2-Kanonen, Laser-Pyramiden und Türstehern eskaliert der Konflikt.</p>
<p>Der Tritt in das <em>Declan-Rice-Trikot</em> des Sicherheitsmannes ist kein herkömmlicher Club-Streit, sondern der verzweifelte Ausbruch eines Ertrinkenden, der durch Schmerz und Adrenalin seine eigene Existenz im Raum erzwingen will.</p>""",
        "review_en": """<p>In <strong>“Amnesia”</strong>, suppressed psychic agony erupts into physical violence. The legendary Ibiza club transforms into the arena of *Narcissistic Rage*: under CO2 cannons and kaleidoscopic lasers, conflict explodes.</p>
<p>Kicking the bouncer's <em>Declan Rice football jersey</em> is not a standard brawl, but the violent convulsion of a drowning psyche using pain and adrenaline to force proof of existence.</p>""",
        "cards_de": [
            {
                "quote": "Der Secu / Weiß-rote Pyramiden",
                "body": """* **Psychodynamische Kausalität:** Sensorische Reizüberflutung. Der Clubraum fragmentiert die Wahrnehmung; die Bedrohung von außen triggert den archaischen Kampftest.
* **Körpersprache & Somatik:** Adrenalinschub, verengte Pupillen, Anspannung der Nacken- und Armmuskulatur.
* **Macht- & Kontroll-Dynamik:** Weigerung vor Unterordnung. Der Türsteher verkörpert die verhasste Autorität, die Grenzen setzt.
* **Akustische & räumliche Wirkung:** Aggressive Basslines und markerschütternde Club-Reverbs."""
            },
            {
                "quote": "CO2-Kanonen / Declan-Rice-Trikot",
                "body": """* **Psychodynamische Kausalität:** Der Moment des Ausbruchs. Kälte (CO2) und Wut verschmelzen zum befreienden Gewaltexzess.
* **Körpersprache & Somatik:** Explosiver Tritt, Reißen an der Kleidung, Schmerzunempfindlichkeit.
* **Macht- & Kontroll-Dynamik:** Physische Grenzverletzung als ultimative Machtdemonstration gegen Übermacht.
* **Akustische & räumliche Wirkung:** Zischender CO2-Effekt im Panorama, gefolgt von einem brutalen Beat-Drop."""
            },
            {
                "quote": "Nase brech' / Narzisstische Wut",
                "body": """* **Psychodynamische Kausalität:** Narcissistic Rage. Wird das Ego in die Enge getrieben, antwortet es mit blinder Vernichtungswut.
* **Körpersprache & Somatik:** Zähnefletschen, geballte Fäuste, vorgebeugter Oberkörper im Angriffsmodus.
* **Macht- & Kontroll-Dynamik:** Einschüchterung durch unberechenbare Gewaltbereitschaft.
* **Akustische & räumliche Wirkung:** Verzerrte, ins Mikrofon gebrüllte Vocals ohne Dynamikbegrenzung."""
            }
        ],
        "cards_en": [
            {
                "quote": "The Bouncer / Red-white Pyramids",
                "body": """* **Psychodynamic Causality:** Sensory fragmentation. Club lights shatter perception; external boundaries trigger primal combat reflexes.
* **Body Language & Somatics:** Adrenaline rush, narrowed pupils, taut neck and bicep tension.
* **Power & Control Dynamics:** Refusing subordination. The bouncer personifies boundary-enforcing authority.
* **Acoustic & Spatial Impact:** Aggressive synth basslines rattling cavernous club acoustics."""
            },
            {
                "quote": "CO2 Canons / Declan Rice Jersey",
                "body": """* **Psychodynamic Causality:** Explosive catharsis. Cold gas and fury merge into kinetic retaliation.
* **Body Language & Somatics:** Explosive kick, tearing free, somatic anesthesia to physical pain.
* **Power & Control Dynamics:** Physical boundary breach as final protest against containment.
* **Acoustic & Spatial Impact:** Searing CO2 white-noise sweeps slamming into an unhinged beat drop."""
            },
            {
                "quote": "Break your nose / Narcissistic Rage",
                "body": """* **Psychodynamic Causality:** Narcissistic Rage. Cornered grandiosity lashes out with destructive fury.
* **Body Language & Somatics:** Clenched jaw, balled fists, forward attack posture.
* **Power & Control Dynamics:** Intimidation via unhinged volatile aggression.
* **Acoustic & Spatial Impact:** Distorted, red-lined vocal scream cutting through the mix."""
            }
        ]
    },
    {
        "num": "11",
        "title": "Kaputt",
        "lyrics_stanzas": [
            {
                "title": "[Hook]",
                "lines": [
                    {"text": "Was ich berühr', das geht kaputt", "annotated": True, "card_idx": 0},
                    {"text": "Ganzes Leben zerleg' ich zu Schutt", "annotated": True, "card_idx": 0},
                    {"text": "Umso schwerer, je mehr ich's versuch'", "annotated": True, "card_idx": 1},
                    {"text": "Und du bist weit, weit weg, währ'nd ich ein Fehltritt bleib'", "annotated": True, "card_idx": 1},
                    {"text": "Ich steck' für eine Ewigkeit in 'nem Loop", "annotated": True, "card_idx": 1}
                ]
            },
            {
                "title": "[Bridge & Outro]",
                "lines": [
                    {"text": "Und ich kam immer davon, aber niemals an", "annotated": True, "card_idx": 2},
                    {"text": "Springmesser-Tattoo auf meiner Brust / Tu nicht so, als hast du nichts gewusst", "annotated": True, "card_idx": 2},
                    {"text": "Hand aufs Herz, ich spüre kein'n Puls — Deine Liebe blieb für immer im August", "annotated": True, "card_idx": 2}
                ]
            }
        ],
        "review_de": """<p>Mit <strong>„Kaputt“</strong> findet das Werk seinen niederschmetternden Schlusspunkt. Hier fällt die Maske des unbesiegbaren Hedonisten vollkommen ab: <span class="lyric-quote-highlight">„Was ich berühr', das geht kaputt / Ganzes Leben zerleg' ich zu Schutt“</span>. Der Narzissmus entpuppt sich als Fluch der Isolation.</p>
<p>Die Schicksalszeile <span class="lyric-quote-highlight">„Und ich kam immer davon, aber niemals an“</span> fasst das menschliche Dilemma der gesamten F60.8-Diagnose zusammen: Ewige Flucht, ewiges Entkommen vor Verantwortung, aber vollkommene Unfähigkeit zu Heimat und wahrer Bindung. <em>„Deine Liebe blieb für immer im August.“</em></p>""",
        "review_en": """<p>With <strong>“Kaputt”</strong> (Broken), the project reaches its devastating terminus. Here the invincible hedonist mask shatters completely: <span class="lyric-quote-highlight">“Whatever I touch turns to ruin / My whole life I dismantle into rubble”</span>. Narcissism stands revealed as a curse of total isolation.</p>
<p>The definitive epitaph <span class="lyric-quote-highlight">“I always got away, but never arrived”</span> encapsulates the existential tragedy of the F60.8 diagnosis: perpetual evasion of accountability, paired with total incapacity for sanctuary and love. <em>“Your love remained forever locked in August.”</em></p>""",
        "cards_de": [
            {
                "quote": "Was ich berühr', das geht kaputt",
                "body": """* **Psychodynamische Kausalität:** Der Midas-Fluch der Zerstörung. Die Unfähigkeit zur echten Empathie vergiftet unweigerlich jede zwischenmenschliche Beziehung.
* **Körpersprache & Somatik:** Zusammensinken der Gestalt, hängende Schultern, matter Blick auf die eigenen Hände.
* **Macht- & Kontroll-Dynamik:** Eingeständnis totaler Ohnmacht gegenüber den eigenen Zerstörungsimpulsen.
* **Akustische & räumliche Wirkung:** Warme, traurige Klavierakkorde und ein schleppender Beat mit tiefem, melancholischem Bassfundament."""
            },
            {
                "quote": "Für eine Ewigkeit in 'nem Loop",
                "body": """* **Psychodynamische Kausalität:** Der psychoanalytische Wiederholungszwang. Die Figur ist dazu verdammt, den Zyklus aus Idealisierung, Entwertung und Absturz endlos zu wiederholen.
* **Körpersprache & Somatik:** Monotones Kopfwiegen im Takt, Gefühl von Zeitlosigkeit und Gefangenschaft.
* **Macht- & Kontroll-Dynamik:** Der Protagonist ist nicht Täter, sondern Gefangener seiner eigenen Charakterstruktur.
* **Akustische & räumliche Wirkung:** Repetitive Synth-Schleifen, die das kreisende Gefangensein akustisch spürbar machen."""
            },
            {
                "quote": "Immer davon, niemals an / Liebe im August",
                "body": """* **Psychodynamische Kausalität:** Das finale Epitaph der Bindungslosigkeit. Ewige Flucht ohne Ankunft; die Liebe wird als vergangene Epoche im Sommer konserviert.
* **Körpersprache & Somatik:** Hand auf der Brust („kein Puls“), somatische Taubheit als Schutz vor dem Schmerz.
* **Macht- & Kontroll-Dynamik:** Resignierte Akzeptanz der eigenen Einsamkeit.
* **Akustische & räumliche Wirkung:** Ausklingende Klaviernoten und sanftes Rauschen, das im Nichts verhallt."""
            }
        ],
        "cards_en": [
            {
                "quote": "What I touch turns to ruin",
                "body": """* **Psychodynamic Causality:** Inverted Midas curse. The structural incapacity for empathy inevitably poisons every bond.
* **Body Language & Somatics:** Collapsed posture, slumped shoulders, vacant stare at open palms.
* **Power & Control Dynamics:** Conceding total helplessness against one's own destructive reflexes.
* **Acoustic & Spatial Impact:** Intimate piano voicings anchored by a weighted, sorrowful sub-bass."""
            },
            {
                "quote": "Trapped in an eternal loop",
                "body": """* **Psychodynamic Causality:** Repetition compulsion. Doomed to endlessly replay the cycle of idealization, devaluation, and collapse.
* **Body Language & Somatics:** Monotone rhythmic nodding, somatic sensation of temporal entrapment.
* **Power & Control Dynamics:** The protagonist is no longer the predator, but the prisoner of his character structure.
* **Acoustic & Spatial Impact:** Circular synthesizer patterns evoking an inescapable sonic loop."""
            },
            {
                "quote": "Always got away, never arrived / August",
                "body": """* **Psychodynamic Causality:** The final epitaph of unattachment. Eternal escape without sanctuary; love sealed away in a dead summer.
* **Body Language & Somatics:** Palm over chest ('no pulse'), somatic numbness guarding against grief.
* **Power & Control Dynamics:** Resigned acceptance of terminal isolation.
* **Acoustic & Spatial Impact:** Fading piano notes dissolving into soft analog tape hiss."""
            }
        ]
    }
]

# Generate index.html exactly 1:1 matching final-wav/tomora
html = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TUA — F60.8 | Album Review & Interpretation</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0c0c0f;
      --bg-surface: #141418;
      --text: #ffffff;
      --text-muted: #8e8e93;
      --magenta: #ff007a;
      --magenta-dim: rgba(255, 0, 122, 0.12);
      --magenta-glow: rgba(255, 0, 122, 0.35);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    html {
      scroll-behavior: smooth;
      background-color: var(--bg);
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.65;
      overflow-x: hidden;
      position: relative;
    }

    /* Dynamic Language Visibility */
    body[data-lang="de"] .lang-en { display: none !important; }
    body[data-lang="en"] .lang-de { display: none !important; }

    /* Animierter 35mm Analog-Film-Grain Canvas */
    #grainCanvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 9999;
      opacity: 0.11;
      mix-blend-mode: screen;
    }

    ::selection {
      background-color: var(--magenta);
      color: #ffffff;
    }

    /* Minimalistische Navbar */
    .navbar {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 65px;
      background: rgba(12, 12, 15, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      padding: 0 32px;
      z-index: 1000;
    }

    .nav-left {
      display: flex;
      align-items: center;
    }

    .burger-btn {
      background: none;
      border: none;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      width: 24px;
      height: 16px;
      padding: 0;
      position: relative;
    }

    .burger-btn span {
      display: block;
      width: 100%;
      height: 2px;
      background-color: #ffffff;
      transition: background-color 0.2s;
    }

    .burger-btn:hover span {
      background-color: var(--magenta);
    }

    .nav-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }

    .brand-title {
      font-size: 1.1rem;
      font-weight: 900;
      letter-spacing: 0.25em;
      color: #ffffff;
      text-transform: uppercase;
      line-height: 1;
    }

    .nav-right {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      gap: 16px;
    }

    .lang-toggle-btn {
      background: rgba(255, 255, 255, 0.06);
      color: var(--text-muted);
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 6px 14px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.15em;
      cursor: pointer;
      text-transform: uppercase;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .lang-toggle-btn:hover {
      color: #ffffff;
      border-color: var(--magenta);
      background: var(--magenta-dim);
    }

    /* Burger Drawer */
    .drawer-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      z-index: 1100;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s;
    }
    .drawer-overlay.active {
      opacity: 1;
      pointer-events: auto;
    }

    .drawer {
      position: fixed;
      top: 0;
      left: -340px;
      width: min(320px, 85vw);
      height: 100vh;
      background-color: #111115;
      z-index: 1200;
      padding: 20px 32px 36px 32px;
      display: flex;
      flex-direction: column;
      transition: left 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      overflow-y: auto;
    }
    .drawer.active { left: 0; }

    .drawer-header {
      height: 25px;
      display: flex;
      align-items: center;
      gap: 20px;
      margin-bottom: 36px;
    }

    .drawer-close-btn {
      background: none;
      border: none;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: center;
      width: 24px;
      height: 24px;
      padding: 0;
      position: relative;
    }

    .drawer-close-btn span {
      display: block;
      width: 24px;
      height: 2px;
      background-color: var(--magenta);
      position: absolute;
      top: 11px;
      left: 0;
      transition: background-color 0.2s;
    }

    .drawer-close-btn span:nth-child(1) { transform: rotate(45deg); }
    .drawer-close-btn span:nth-child(2) { transform: rotate(-45deg); }
    .drawer-close-btn:hover span { background-color: #ffffff; }

    .drawer-title {
      font-size: 0.85rem;
      font-weight: 800;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--magenta);
      line-height: 1;
    }

    .drawer-nav {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .drawer-nav a {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 1rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      display: block;
      padding: 4px 0;
      transition: all 0.2s;
    }

    .drawer-nav a:hover {
      color: #ffffff;
      padding-left: 6px;
    }

    /* FULL BLEED HERO */
    .hero-fullbleed {
      margin-top: 65px;
      width: 100%;
      max-height: 75vh;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #000000;
      position: relative;
    }

    .hero-image {
      width: 100%;
      height: 75vh;
      object-fit: cover;
      display: block;
      filter: brightness(0.65) saturate(1.2);
    }

    .hero-overlay-tag {
      position: absolute;
      bottom: 40px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(12, 12, 15, 0.8);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 0, 122, 0.4);
      padding: 8px 24px;
      border-radius: 30px;
      font-size: 0.8rem;
      font-weight: 800;
      letter-spacing: 0.2em;
      color: #ffffff;
      text-transform: uppercase;
    }

    /* Layout Wrapper */
    .main-wrapper {
      max-width: 1400px;
      margin: 0 auto;
      padding: 60px 32px 120px 32px;
    }

    .album-header {
      margin-bottom: 80px;
      text-align: center;
    }

    .album-meta-tag {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.25em;
      color: var(--magenta);
      text-transform: uppercase;
      margin-bottom: 12px;
    }

    .album-main-title {
      font-size: clamp(2.5rem, 5vw, 4rem);
      font-weight: 900;
      letter-spacing: -0.02em;
      line-height: 1.1;
      margin-bottom: 16px;
    }

    .album-subtitle {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 760px;
      margin: 0 auto;
      font-weight: 400;
      line-height: 1.6;
    }

    /* Track Container */
    .track-section {
      margin-bottom: 140px;
      scroll-margin-top: 100px;
    }

    .track-header-bar {
      margin-bottom: 40px;
      padding-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    .track-title-wrap {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }

    .song-round-play-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--magenta);
      color: #ffffff;
      border: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 0 12px var(--magenta-glow);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      flex-shrink: 0;
      padding: 0;
    }

    .song-round-play-btn:hover {
      background: #ff2b92;
      transform: scale(1.1);
      box-shadow: 0 0 18px rgba(255, 0, 122, 0.65);
    }

    .audio-play-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #cfcfd4;
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
      user-select: none;
    }

    .audio-play-btn:hover {
      color: #ffffff;
      border-color: var(--magenta);
      background: var(--magenta-dim);
    }

    .track-num-badge {
      font-size: 1.2rem;
      font-weight: 900;
      color: var(--magenta);
      letter-spacing: 0.1em;
    }

    .track-heading {
      font-size: clamp(1.8rem, 3.5vw, 2.5rem);
      font-weight: 900;
      letter-spacing: -0.01em;
      color: #ffffff;
      text-transform: uppercase;
    }

    /* Two-Column Genius Layout */
    .track-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: start;
    }

    @media (max-width: 992px) {
      .track-grid {
        grid-template-columns: 1fr;
        gap: 40px;
      }
    }

    /* Left Column: Lyrics */
    .lyrics-col {
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    .stanza {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .stanza-title {
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--magenta);
      margin-bottom: 4px;
    }

    .lyric-line {
      font-size: 1.08rem;
      font-weight: 500;
      color: rgba(255, 255, 255, 0.75);
      line-height: 1.65;
      margin-bottom: 4px;
    }

    .lyric-line.plain {
      cursor: default;
    }

    .lyric-line.annotated {
      cursor: pointer;
    }

    .lyric-trigger {
      display: inline-block;
      color: #ffffff;
      border-bottom: 2px solid rgba(255, 0, 122, 0.45);
      padding: 1px 4px;
      margin: 0 -4px;
      border-radius: 4px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .lyric-trigger:hover {
      background: rgba(255, 0, 122, 0.18);
      border-bottom-color: var(--magenta);
      color: #ffffff;
      box-shadow: 0 0 12px var(--magenta-glow);
    }

    .lyric-trigger.active {
      background: var(--magenta);
      border-bottom-color: #ffffff;
      color: #ffffff;
      font-weight: 700;
      box-shadow: 0 0 16px var(--magenta-glow);
    }

    /* Right Column: Analysis */
    .analysis-col {
      display: flex;
      flex-direction: column;
      gap: 32px;
    }

    .lang-block {
      display: flex;
      flex-direction: column;
      gap: 32px;
    }

    .analysis-view-wrapper {
      position: relative;
      width: 100%;
    }

    .narrative-review {
      background: transparent;
      font-size: 1.05rem;
      color: #cfcfd4;
      line-height: 1.8;
      font-weight: 400;
      transition: opacity 0.3s ease;
    }

    .narrative-review p {
      margin-bottom: 16px;
    }

    .narrative-review p:last-child {
      margin-bottom: 0;
    }

    .lyric-quote-highlight {
      color: var(--magenta);
      background: rgba(255, 0, 122, 0.12);
      padding: 1px 7px;
      border-radius: 4px;
      font-weight: 600;
      font-style: normal;
      display: inline;
      border: 1px solid rgba(255, 0, 122, 0.25);
    }

    .narrative-review strong,
    .card-body strong {
      color: #ffffff;
      font-weight: 700;
    }

    .card-deck-view {
      display: flex;
      flex-direction: column;
      gap: 20px;
      transition: margin-top 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      animation: fadeInCard 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes fadeInCard {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .card-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .card-back-btn {
      background: none;
      border: none;
      color: rgba(255, 255, 255, 0.6);
      padding: 4px;
      margin: 0;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .card-back-btn:hover {
      color: var(--magenta);
      transform: translateX(-4px);
    }

    .card-badge-counter {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .analysis-card {
      background: var(--bg-surface);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      padding: 24px 28px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
      display: none;
    }

    .analysis-card.active {
      display: block;
    }

    .card-quote {
      font-size: 0.88rem;
      font-weight: 800;
      color: var(--magenta);
      background: rgba(255, 0, 122, 0.10);
      border-left: 3px solid var(--magenta);
      padding: 6px 12px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 14px;
      display: block;
    }

    .card-body {
      font-size: 0.98rem;
      color: #d0d0d5;
      line-height: 1.7;
    }

    .card-body p {
      margin-bottom: 12px;
    }
    .card-body p:last-child {
      margin-bottom: 0;
    }

    /* Footer */
    footer {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 60px 32px 120px 32px;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
      letter-spacing: 0.05em;
    }

    footer p {
      margin-bottom: 8px;
    }

    /* FLOATING BOTTOM MINI PLAYER (Glass Dock) */
    .bottom-player {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      width: min(840px, calc(100vw - 32px));
      height: 68px;
      background: rgba(12, 12, 15, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65), 0 0 1px rgba(255, 255, 255, 0.15);
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      padding: 0 24px;
      z-index: 1000;
    }

    .player-left {
      display: flex;
      flex-direction: column;
      gap: 2px;
      overflow: hidden;
      justify-content: center;
    }

    .player-track-info {
      display: flex;
      align-items: baseline;
      gap: 8px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .player-track-num {
      font-size: 0.75rem;
      font-weight: 900;
      color: var(--magenta);
      letter-spacing: 0.08em;
    }

    .player-track-title {
      font-size: 0.88rem;
      font-weight: 800;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .player-subtitle {
      font-size: 0.65rem;
      color: var(--text-muted);
      letter-spacing: 0.05em;
    }

    .player-center {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
    }

    .play-pause-circle {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: #ffffff;
      color: #0c0c0f;
      display: flex;
      align-items: center;
      justify-content: center;
      border: none;
      cursor: pointer;
      transition: all 0.2s;
    }

    .play-pause-circle:hover {
      background: var(--magenta);
      color: #ffffff;
      box-shadow: 0 0 15px var(--magenta-glow);
    }

    .player-right {
      display: flex;
      justify-content: flex-end;
      align-items: center;
    }

    .player-lang-badge {
      font-size: 0.65rem;
      font-weight: 800;
      color: var(--text-muted);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 2px 6px;
      border-radius: 4px;
      letter-spacing: 0.08em;
    }

    @media (max-width: 768px) {
      .bottom-player {
        bottom: 16px;
        width: calc(100vw - 24px);
        grid-template-columns: 1fr auto;
        height: auto;
        padding: 10px 14px;
        gap: 6px;
      }
      .player-right { display: none; }
    }
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
      <div class="brand-title">TUA</div>
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
        <span class="lang-de">Titelauswahl (F60.8)</span>
        <span class="lang-en">Track Selection (F60.8)</span>
      </div>
    </div>
    <ul class="drawer-nav">
"""

for t in tracks_data:
    html += f'      <li><a href="#track-{t["num"]}">{t["num"]} — {t["title"]}</a></li>\n'

html += """    </ul>
  </div>

  <!-- Hero Cover Art -->
  <div class="hero-fullbleed">
    <img src="cover.png" alt="Tua F60.8 Cover" class="hero-image">
    <div class="hero-overlay-tag">ICD-10 F60.8 — MULTIMODALE WERKANALYSE</div>
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
        <span class="lang-de">Eine detaillierte literarische und psychoanalytische Untersuchung über Narzissmus, Rausch, emotionale Staffage und den unausweichlichen Ikarus-Absturz.</span>
        <span class="lang-en">An in-depth literary and psychoanalytic examination of narcissism, intoxication, emotional stage-setting, and the inevitable Icarus descent.</span>
      </p>
    </header>

    <div class="tracks-list">
"""

for t in tracks_data:
    num = t["num"]
    title = t["title"]
    
    html += f"""
    <section class="track-section" id="track-{num}">
      <div class="track-header-bar">
        <div class="track-title-wrap">
          <span class="track-num-badge">{num}</span>
          <h2 class="track-heading">{title}</h2>
          <button class="song-round-play-btn" data-track-num="{num}" data-track-title="{num} — {title}" aria-label="Play Track">
            <svg class="play-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><polygon points="7 4 19 12 7 20 7 4"></polygon></svg>
            <svg class="pause-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><rect x="6" y="4" width="3.5" height="16"></rect><rect x="14.5" y="4" width="3.5" height="16"></rect></svg>
          </button>
        </div>
        <button class="audio-play-btn" data-track-num="{num}" aria-label="Listen to Essay">
          <svg class="play-icon" viewBox="0 0 24 24" width="13" height="13"><polygon points="6 4 20 12 6 20 6 4" fill="currentColor"></polygon></svg>
          <span class="btn-text">
            <span class="lang-de">Analyse-Fokus</span>
            <span class="lang-en">Analysis Focus</span>
          </span>
        </button>
      </div>
      <div class="track-grid">
        <div class="lyrics-col">
"""
    for stanza in t["lyrics_stanzas"]:
        html += f'          <div class="stanza">\n'
        html += f'            <div class="stanza-title">{stanza["title"]}</div>\n'
        for line in stanza["lines"]:
            if line.get("annotated"):
                c_idx = line["card_idx"]
                html += f'            <div class="lyric-line annotated"><span class="lyric-trigger" data-track-num="{num}" data-target-card="{c_idx}">{line["text"]}</span></div>\n'
            else:
                html += f'            <div class="lyric-line plain">{line["text"]}</div>\n'
        html += f'          </div>\n'

    html += f"""        </div>
        <div class="analysis-col">
          <!-- German Block -->
          <div class="lang-block lang-de">
            <div class="analysis-view-wrapper">
              <div class="narrative-review" id="review-{num}-de">
                {t["review_de"]}
              </div>
              <div class="card-deck-view" id="card-deck-{num}-de" style="display: none;">
"""
    total_cards = len(t["cards_de"])
    for idx, c in enumerate(t["cards_de"]):
        # Parse markdown formatting inside card body
        body_html = ""
        for p in c["body"].split("\n"):
            p_strip = p.strip()
            if not p_strip:
                continue
            if p_strip.startswith("* **"):
                # Dimension bullet
                formatted = p_strip.replace("* **", "<strong>").replace(":**", ":</strong>")
                body_html += f"<p>{formatted}</p>\n"
            else:
                body_html += f"<p>{p_strip}</p>\n"

        html += f"""                <div class="analysis-card" id="card-{num}-de-{idx}" data-card-idx="{idx}">
                  <div class="card-header-bar">
                    <button class="card-back-btn" data-track-num="{num}" data-lang="de" aria-label="Zurück zur Review">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    </button>
                    <span class="card-badge-counter">Tiefen-Analyse {idx + 1} / {total_cards}</span>
                  </div>
                  <span class="card-quote">{c["quote"]}</span>
                  <div class="card-body">
                    {body_html}
                  </div>
                </div>
"""

    html += f"""              </div>
            </div>
          </div>

          <!-- English Block -->
          <div class="lang-block lang-en">
            <div class="analysis-view-wrapper">
              <div class="narrative-review" id="review-{num}-en">
                {t["review_en"]}
              </div>
              <div class="card-deck-view" id="card-deck-{num}-en" style="display: none;">
"""
    for idx, c in enumerate(t["cards_en"]):
        body_html = ""
        for p in c["body"].split("\n"):
            p_strip = p.strip()
            if not p_strip:
                continue
            if p_strip.startswith("* **"):
                formatted = p_strip.replace("* **", "<strong>").replace(":**", ":</strong>")
                body_html += f"<p>{formatted}</p>\n"
            else:
                body_html += f"<p>{p_strip}</p>\n"

        html += f"""                <div class="analysis-card" id="card-{num}-en-{idx}" data-card-idx="{idx}">
                  <div class="card-header-bar">
                    <button class="card-back-btn" data-track-num="{num}" data-lang="en" aria-label="Back to Review">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    </button>
                    <span class="card-badge-counter">Deep Analysis {idx + 1} / {total_cards}</span>
                  </div>
                  <span class="card-quote">{c["quote"]}</span>
                  <div class="card-body">
                    {body_html}
                  </div>
                </div>
"""

    html += f"""              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

html += """    </div>
  </main>

  <!-- Footer -->
  <footer>
    <p><strong>TUA — F60.8 (2025)</strong></p>
    <p>ICD-10 F60.8: Sonstige spezifische Persönlichkeitsstörungen (Narzissmus & Dissoziation)</p>
    <p>Architektur & Design-System: Pitchfork / Genius Standard | 35mm Analogfilm-Korn</p>
  </footer>

  <!-- Floating Mini Player (Glass Dock) -->
  <div class="bottom-player">
    <div class="player-left">
      <div class="player-track-info">
        <span class="player-track-num" id="playerTrackNum">01</span>
        <span class="player-track-title" id="playerTrackTitle">1996</span>
      </div>
      <div class="player-subtitle">Tua — F60.8 (2025)</div>
    </div>
    <div class="player-center">
      <button class="play-pause-circle" id="masterPlayBtn" aria-label="Play / Pause">
        <svg id="playIconSvg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
          <polygon points="7 4 19 12 7 20 7 4"></polygon>
        </svg>
      </button>
    </div>
    <div class="player-right">
      <span class="player-lang-badge">EGO FM IBIZA</span>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // 1. Animierter 35mm Film-Grain Canvas
      const canvas = document.getElementById('grainCanvas');
      if (canvas) {
        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = window.innerHeight;

        window.addEventListener('resize', () => {
          width = canvas.width = window.innerWidth;
          height = canvas.height = window.innerHeight;
        });

        function renderGrain() {
          const imgData = ctx.createImageData(width, height);
          const buffer = new Uint32Array(imgData.data.buffer);
          const len = buffer.length;
          for (let i = 0; i < len; i++) {
            if (Math.random() < 0.11) {
              const gray = (Math.random() * 255) | 0;
              buffer[i] = (255 << 24) | (gray << 16) | (gray << 8) | gray;
            }
          }
          ctx.putImageData(imgData, 0, 0);
          requestAnimationFrame(renderGrain);
        }
        renderGrain();
      }

      // 2. Language Switcher (DE / EN)
      const langBtn = document.getElementById('langToggleBtn');
      langBtn.addEventListener('click', () => {
        const currentLang = document.body.getAttribute('data-lang') || 'de';
        const newLang = currentLang === 'de' ? 'en' : 'de';
        document.body.setAttribute('data-lang', newLang);
      });

      // 3. Burger Drawer Navigation
      const burgerToggle = document.getElementById('burgerToggle');
      const drawerClose = document.getElementById('drawerClose');
      const drawerNav = document.getElementById('drawerNav');
      const drawerOverlay = document.getElementById('drawerOverlay');

      function openDrawer() {
        drawerNav.classList.add('active');
        drawerOverlay.classList.add('active');
      }

      function closeDrawer() {
        drawerNav.classList.remove('active');
        drawerOverlay.classList.remove('active');
      }

      burgerToggle.addEventListener('click', openDrawer);
      drawerClose.addEventListener('click', closeDrawer);
      drawerOverlay.addEventListener('click', closeDrawer);

      drawerNav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', closeDrawer);
      });

      // 4. Interaktive Zeilen-Trigger & Dynamische Tiefen-Analyse Karten
      const lyricTriggers = document.querySelectorAll('.lyric-trigger');
      
      lyricTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
          const trackNum = trigger.getAttribute('data-track-num');
          const targetCardIdx = trigger.getAttribute('data-target-card');

          document.querySelectorAll(`.lyric-trigger[data-track-num="${trackNum}"]`).forEach(el => {
            el.classList.remove('active');
          });
          trigger.classList.add('active');

          ['de', 'en'].forEach(lang => {
            const reviewEl = document.getElementById(`review-${trackNum}-${lang}`);
            const deckEl = document.getElementById(`card-deck-${trackNum}-${lang}`);
            if (!reviewEl || !deckEl) return;

            reviewEl.style.display = 'none';
            deckEl.style.display = 'flex';

            const cards = deckEl.querySelectorAll('.analysis-card');
            cards.forEach(card => card.classList.remove('active'));

            const targetCard = document.getElementById(`card-${trackNum}-${lang}-${targetCardIdx}`);
            if (targetCard) {
              targetCard.classList.add('active');
            }

            if (window.innerWidth > 992) {
              const trackGrid = trigger.closest('.track-grid');
              if (trackGrid) {
                const gridRect = trackGrid.getBoundingClientRect();
                const triggerRect = trigger.getBoundingClientRect();
                const relativeTop = Math.max(0, triggerRect.top - gridRect.top);
                deckEl.style.marginTop = `${relativeTop}px`;
              }
            } else {
              deckEl.style.marginTop = '0px';
            }
          });
        });
      });

      // 5. Zurück-Button auf den Analysekarten
      const backButtons = document.querySelectorAll('.card-back-btn');
      backButtons.forEach(btn => {
        btn.addEventListener('click', () => {
          const trackNum = btn.getAttribute('data-track-num');

          ['de', 'en'].forEach(lang => {
            const reviewEl = document.getElementById(`review-${trackNum}-${lang}`);
            const deckEl = document.getElementById(`card-deck-${trackNum}-${lang}`);
            if (deckEl) deckEl.style.display = 'none';
            if (reviewEl) reviewEl.style.display = 'block';
          });

          document.querySelectorAll(`.lyric-trigger[data-track-num="${trackNum}"]`).forEach(el => {
            el.classList.remove('active');
          });
        });
      });

      // 6. Audio Player Interaktion
      const playerTrackNum = document.getElementById('playerTrackNum');
      const playerTrackTitle = document.getElementById('playerTrackTitle');
      const masterPlayBtn = document.getElementById('masterPlayBtn');
      const songPlayBtns = document.querySelectorAll('.song-round-play-btn');

      let isPlaying = false;

      function updatePlayerState(title, trackNumber) {
        playerTrackTitle.textContent = title;
        playerTrackNum.textContent = trackNumber;
        isPlaying = true;
        masterPlayBtn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>`;
      }

      songPlayBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          const fullTitle = btn.getAttribute('data-track-title');
          const [num, title] = fullTitle.split(' — ');
          
          songPlayBtns.forEach(b => {
            b.querySelector('.play-icon').style.display = 'block';
            b.querySelector('.pause-icon').style.display = 'none';
          });
          btn.querySelector('.play-icon').style.display = 'none';
          btn.querySelector('.pause-icon').style.display = 'block';

          updatePlayerState(title || fullTitle, num || '01');
        });
      });

      masterPlayBtn.addEventListener('click', () => {
        isPlaying = !isPlaying;
        if (isPlaying) {
          masterPlayBtn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>`;
        } else {
          masterPlayBtn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="7 4 19 12 7 20 7 4"></polygon></svg>`;
        }
      });
    });
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generated 1:1 matching tomora architecture.")
