import json
import re
import os

# Load Genius lyrics
raw_lyrics = json.load(open("full_genius_lyrics.json", "r", encoding="utf-8"))

# Load tomora template
with open("tomora_index.html", "r", encoding="utf-8") as f:
    tomora_raw = f.read()

# Extract CSS and change theme to cover orange
css_start = tomora_raw.find("<style>")
css_end = tomora_raw.find("</style>") + len("</style>")
tomora_css = tomora_raw[css_start:css_end]

orange_css = tomora_css.replace('--magenta: #ff007a;', '--magenta: #fa5b00;') \
                       .replace('255, 0, 122', '250, 91, 0') \
                       .replace('#ff2b92', '#ff6a1a') \
                       .replace('object-fit: cover;', 'object-fit: cover; object-position: center 78%;')




# Extract JS
js_start = tomora_raw.rfind("<script>")
js_end = tomora_raw.rfind("</script>") + len("</script>")
tomora_js = tomora_raw[js_start:js_end]

# 11 Tracks Dataset with real Pitchfork reviews and genuine prose cards (Tomora standard)
tracks_data = [
    {
        "num": "01",
        "title": "1996",
        "review_de": """<p>Das Album eröffnet mit der Inszenierung des Ursprungsmythos: <strong>„1996“</strong> markiert den biografischen und psychologischen Nullpunkt der Persona. Eingerahmt von mediterraner Hitze und der schwebenden Erwartung eines Sommers auf Ibiza entfaltet Tua das Leitmotiv des Werks: Der <span class="lyric-quote-highlight">„Panoramablick übers Paradies / Während warme Luft auf dem Garten liegt“</span> ist kein Ort inneren Friedens, sondern die erhabene Bastion eines Ichs, das die Welt nur aus sicherer Distanz erträgt. Doch bereits im zweiten Teil bricht das Verdrängte unaufhaltsam ein: <span class="lyric-quote-highlight">„Etwas fehlt, vielleicht ist es aufgewacht / Das Gegenteil, das Außerhalb“</span>. Das heraufziehende Rauschen in den Palmen kündigt den existenziellen Mangel an.</p>
<p>Im sakral aufgeladenen Refrain (<span class="lyric-quote-highlight">„Ob die Welt hält, was sie verspricht? / Steig' herab in strahlendem Licht / Und ganz in Weiß gekleidet“</span>) wird der narzisstische Abstieg als messianischer Auftritt inszeniert. Doch das Outro vollzieht die schonungslose Demaskierung: Als <span class="lyric-quote-highlight">„Ikarus, Fantasieprodukt / Entfliehst dem Druck hoch in die Fieberluft“</span> flieht die Kunstfigur vor der Realität. Der Flug über den <span class="lyric-quote-highlight">„tiefsten Bruch“</span> ist keine Freiheit, sondern die manische Flucht vor dem unausweichlichen Aufprall.</p>""",
        "review_en": """<p>The album opens with the staging of the origin myth: <strong>“1996”</strong> marks the biographical and psychological baseline of the persona. Framed by Mediterranean heat and the suspended anticipation of an Ibiza summer, Tua unveils the central motif: <span class="lyric-quote-highlight">“Panoramic view over paradise / While warm air lies on the garden”</span> is no sanctuary of peace, but the elevated fortress of an ego that tolerates reality only from a detached distance. Yet in the second part, the repressed core erupts: <span class="lyric-quote-highlight">“Something is missing, maybe it woke up / The opposite, the outside”</span>. The rising rustle in the palms announces foundational lack.</p>
<p>In the sacral chorus (<span class="lyric-quote-highlight">“Will the world deliver what it promised? / Step down in radiant light / Dressed in white”</span>), narcissistic descent is choreographed as a messianic arrival. Yet the outro executes an unsparing demystification: as <span class="lyric-quote-highlight">“Icarus, fantasy product / Fleeing the pressure into the fever air”</span>, the persona retreats from reality. The flight over the <span class="lyric-quote-highlight">“deepest fracture”</span> is no sovereign emancipation, but a manic escape preceding the inevitable impact.</p>""",
        "cards_de": [
            {
                "quote": "Panoramablick übers Paradies / Die erhabene Isolation",
                "body": """Die Inszenierung des Luxus-Panoramas über das „Paradies“ dient als hermetische Barriere: Wer ganz oben steht und auf die Szenerie herabblickt, entzieht sich jeder unkontrollierten Nähe. Die Erwartung, die „unter die Palmen kriecht“, anthropomorphisiert die quälende innere Unruhe zu einem schleichenden Eindringling, der die scheinbare Idylle bedroht.

Es entsteht das Bild eines Ichs, das seinen Schmerz in luxuriöser Ferne betäubt. Die Hitze und die Weite des Gartens spenden keinen Trost, sondern bilden das sterile Bühnenbild für eine chronische Alarmbereitschaft."""
            },
            {
                "quote": "Etwas fehlt, vielleicht ist es aufgewacht / Der Einbruch des Mangels",
                "body": """Trotz maximaler äußerer Reizsättigung bricht das verdrängte Reale ein: „Das Gegenteil, das Außerhalb“ ist der unausweichliche Mangel, der sich nicht länger wegerklären lässt. Das anschwellende Rauschen in den Palmen markiert den Moment, in dem die Fassade der Sorglosigkeit Risse bekommt.

Das Subjekt spürt die Kälte des eigenen Vakuums mitten im Hochsommer. Der Versuch, sich im Paradies zu verbarrikadieren, scheitert an der Unfähigkeit, inneren Frieden zu finden."""
            },
            {
                "quote": "Ob die Welt hält, was sie verspricht? / Der messianische Abstieg",
                "body": """Die Frage an die Welt formuliert einen infantilen Allmachtsanspruch: Das Ich verlangt die bedingungslose Erfüllung seiner Grandiositätsfantasien. Der Auftritt „ganz in Weiß gekleidet“ auf Stufen, die einen scheinbar von selbst tragen, inszeniert den Eintritt in die Welt als sakrale Apotheose.

Hinter der strahlenden Geste verbirgt sich die panische Angst vor der Realitätsprüfung. Das weiße Gewand ist keine Reinheit, sondern die Rüstung eines Narzissten, der jede Berührung mit dem Boden scheut."""
            },
            {
                "quote": "Ikarus, Fantasieprodukt / Der manische Höhenflug",
                "body": """Die schonungslose Demaskierung im Outro: Das Ich erkennt sich selbst als rein artifizielles „Fantasieprodukt“. Der mythologische Flug des Ikarus in die „Fieberluft“ ist kein heroischer Akt der Freiheit, sondern die verzweifelte Flucht vor dem unerträglichen inneren Druck.

Das Überfliegen des „tiefsten Bruchs“ schiebt den fatalen Aufprall lediglich auf. Die Konstruktion der Persona kollabiert in der Erkenntnis ihrer eigenen Hohlheit."""
            }
        ],
        "cards_en": [
            {
                "quote": "Panoramic view over paradise / Sublime isolation",
                "body": """The luxury panorama over "paradise" serves as a hermetic barrier: surveying reality from above precludes unmediated vulnerability. Anticipation "creeping under the palms" anthropomorphizes chronic anxiety into an encroaching intruder threatening serenity.

A portrait of a self sedating pain through elevated detachment. The garden's warmth offers no comfort, but provides the sterile set piece for chronic vigilance."""
            },
            {
                "quote": "Something is missing, maybe it woke up / Incursion of lack",
                "body": """Despite maximum sensory saturation, the repressed real erupts: "the opposite, the outside" is the unavoidable void that resists rationalization. The swelling rustle in the palms signals the collapse of the carefree facade.

The subject encounters internal cold in high summer. Barricading inside paradise fails against the inability to sustain inner peace."""
            },
            {
                "quote": "Will the world deliver what it promised? / Messianic descent",
                "body": """The query directed at the world articulates infantile entitlement: demanding total validation of omnipotent fantasies. Descending "dressed in white" on stairs that seemingly carry the body stages entry into reality as sacral apotheosis.

Behind the radiant posture lurks acute terror of reality testing. The white attire is no emblem of purity, but armor warding off ground friction."""
            },
            {
                "quote": "Icarus, fantasy product / Manic flight",
                "body": """Unsparing demystification in the outro: the persona confronts its constructed identity as an artificial "fantasy product". The flight of Icarus into "fever air" is not heroism, but frantic flight from internal pressure.

Soaring over the "deepest fracture" merely defers impact. The persona fractures under the weight of its own hollowness."""
            }
        ]
    },
    {
        "num": "02",
        "title": "Wiedersehen",
        "review_de": """<p>In <strong>„Wiedersehen“</strong> vollzieht der Protagonist den radikalen Bruch mit seiner Herkunft und formuliert sein rücksichtsloses Autarkie-Credo. Mit schnoddriger Verachtung wischt das Ich alle moralischen Bewertungen der alten Heimat beiseite: <span class="lyric-quote-highlight">„Dann bin ich jede Story, die dein Dorf sich erzählt / Weine keinem eine scheiß Träne hinterher / Wo ich hingehe, ist das Licht dir zu hell“</span>. Die Arroganz fungiert hier als hermetischer Schutzschild gegen Schuld und Beschämung.</p>
<p>Die Grausamkeit der Abspaltung erreicht im zweiten Vers ihren Höhepunkt: <span class="lyric-quote-highlight">„Ich hab' dich nie geliebt, sondern war dich nur gewohnt / Ich wein' dir nicht mal eine scheiß Träne hinterher“</span>. Intimität wird nachträglich entwertet, um jeden Trennungsschmerz zu ersticken. Auf der Mittelmeerfähre stehend, blickt der Protagonist im Outro auf die schäumende Heckwelle und pervertiert die Seligpreisungen in ein raubtierhaftes Gesetz: <span class="lyric-quote-highlight">„Ich steh' auf einer Fähre übers Mittelmeer / Seh' der weißen Spur im Wasser hinterher / Selig sind die Diebe / Ich nehme, was ich kriege“</span>. Bindung ist für ihn kein Dialog, sondern ein Beutezug vor dem nächsten Transit.</p>""",
        "review_en": """<p>In <strong>“Wiedersehen”</strong> (Farewell / Parting), the protagonist executes a radical rupture with his origins, formalizing a ruthless ethos of predatory self-reliance. With dismissive contempt, the speaker discards provincial judgments: <span class="lyric-quote-highlight">“Then I am every rumor your village tells / Won't shed a single fucking tear / Where I'm going, the light is too bright for you”</span>. Arrogance operates as a hermetic firewall insulating against guilt and shame.</p>
<p>The cruelty of detachment culminates in the second verse: <span class="lyric-quote-highlight">“I never loved you, I was only used to you / Won't even shed a fucking tear for you”</span>. Past intimacy is retroactively incinerated to pre-empt any experience of mourning. Standing on the Mediterranean ferry in the outro, Tua subverts the Beatitudes into a pirate manifesto: <span class="lyric-quote-highlight">“Standing on a ferry across the Mediterranean / Watching the white wake in the water / Blessed are the thieves / I take what I get”</span>. Attachment is reduced to an extraction prior to the next departure.</p>""",
        "cards_de": [
            {
                "quote": "Dann bin ich jede Story, die dein Dorf sich erzählt / Der arrogante Schutzwall",
                "body": """Mit schnoddriger Verachtung wischt das Ich alle Gerüchte der alten Heimat beiseite. Die trotzige Behauptung, das eigene Licht sei für die Zurückgebliebenen „zu hell“, projiziert Minderwertigkeit auf das Umfeld, um die eigene fundamentale Scham abzuwehren.

Arroganz fungiert hier als Exoskelett: Wer die anderen zuerst entwertet und auslacht, kann von ihren Urteilen nicht mehr getroffen werden."""
            },
            {
                "quote": "Sorry für die Wahrheit / Der zynische Beziehungsabbruch",
                "body": """Die Hook zelebriert die Trennung als befreiende Selbstermächtigung. Indem das Leiden des Gegenübers als fremdes „Drama“ abqualifiziert wird, entzieht sich das Ich jeder emotionalen Verantwortung. Das dreifache „Auf Nimmerwiederseh'n“ schlägt die Tür mit administrativer Kälte zu.

Die vorgetäuschte Reue („Sorry für die Wahrheit“) ist eine rhetorische Waffe, die Grausamkeit als angebliche Ehrlichkeit tarnt."""
            },
            {
                "quote": "Ich hab' dich nie geliebt, sondern war dich nur gewohnt / Die Tilgung der Intimität",
                "body": """Das radikale Eingeständnis beraubt den Partner nachträglich jeglicher Bedeutung. Um keinen Trennungsschmerz empfinden zu müssen, wird die gesamte gemeinsame Vergangenheit als bloße „Gewohnheit“ entwertet.

Das somatische Bild des „Rotwerdens“ hinter geschlossenen Augen verrät jedoch die krampfhafte Anstrengung dieser Abspaltung: Die Wut dient als Betäubungsmittel gegen das unausweichliche Schuldbewusstsein."""
            },
            {
                "quote": "Die Welt gehört denen, die sie sich nehmen / Das Raubtier-Dogma",
                "body": """Das sozialdarwinistische Bekenntnis als moralische Rechtfertigung: Das Ich erklärt Ausbeutung und Rücksichtslosigkeit zum universellen Naturgesetz. Wer Skrupel zeigt, geht unter; wer nimmt, behält die Kontrolle.

Diese Ideologie fungiert als letzte Bastion gegen die eigene Verletzlichkeit. Die Wiederholung wirkt wie eine Autosuggestion, um das nagende Gewissen mundtot zu machen."""
            },
            {
                "quote": "Selig sind die Diebe / Die Pervertierung der Gnade",
                "body": """Auf der Mittelmeerfähre stehend, blickt der Protagonist auf die schäumende Heckwelle und pervertiert die biblischen Seligpreisungen in ein Gesetz des Diebstahls. Die weiße Spur im Wasser wird zum Sinnbild für die Vergänglichkeit und Entsorgung aller vergangenen Bindungen.

Das Nehmen ohne Wiederkehr wird zum heiligen Überlebensprinzip erhoben. Das Subjekt flieht auf dem Wasser vor jeder Bindung in das selbstgewählte Exil."""
            }
        ],
        "cards_en": [
            {
                "quote": "Then I am every rumor your village tells / Arrogant firewall",
                "body": """Dismissing provincial gossip with nonchalant contempt. Proclaiming personal radiance "too bright" projects inadequacy outward, defending against deep-seated shame.

Arrogance serves as exoskeleton: devaluing and mocking others pre-empts vulnerability to their judgment."""
            },
            {
                "quote": "Sorry for the truth / Cynical rupture",
                "body": """The chorus celebrates relational termination as triumphant emancipation. Labelling partner anguish as external "drama" absolves the ego of accountability.

Feigned remorse ("sorry for the truth") weaponizes cruelty as alleged authenticity."""
            },
            {
                "quote": "Never loved you, was only used to you / Erasure of intimacy",
                "body": """Confessing past intimacy was merely "habit" retroactively strips the bond of value to extinguish mourning.

Internal "redness" behind closed eyelids betrays the immense strain of repression: rage numbs guilt."""
            },
            {
                "quote": "The world belongs to those who take it / Predator dogma",
                "body": """Social-Darwinist doctrine rationalizing extraction: ruthlessness framed as natural law. Reluctance invites destruction; taking asserts control.

Ideology serves as defense against vulnerability. Repetition operates as autosuggestion to silence conscience."""
            },
            {
                "quote": "Blessed are the thieves / Inversion of grace",
                "body": """Aboard the Mediterranean ferry, surveying the churning wake, the Beatitudes are inverted into a pirate code. The fading wake symbolizes the disposal of past attachment.

Unilateral extraction becomes sovereign survival law. The subject flees across water into self-imposed exile."""
            }
        ]
    },
    {
        "num": "03",
        "title": "GluiV",
        "review_de": """<p><strong>„GluiV“</strong> seziert die vulgäre Oberfläche des Jetset-Materialismus und transformiert Markensymbole in ein psychologisches Exoskelett. Die repetitive Stakkato-Hook <span class="lyric-quote-highlight">„G, Louis V, Bauchtasche, Kokain, ich fick' alle“</span> ist kein naiver Flex, sondern die krampfhafte Beschwörung unverwundbarer Allmacht. Der Protagonist definiert sich über kinetische Rastlosigkeit und chemische Zufuhr (<span class="lyric-quote-highlight">„Immer in Bewegung, immer im Dienst / Vitamin Zieh“</span>), um jedes Innehalten zu verhindern.</p>
<p>Die Szenerie im <span class="lyric-quote-highlight">„Marmorfliesen im Airbnb / Ihr Leihparadies“</span> entlarvt die Austauschbarkeit der Akteure. Hinter der Prahlerei bricht im Pre-Hook die nackte Kränkung durch: <span class="lyric-quote-highlight">„Und trotzdem, denn ich bin nicht ihr Typ / Nur der Typ, der den Stoff bringt, glaubt sie“</span>. Die glamouröse Fassade scheitert daran, die fundamentale Entfremdung zu überdecken – das Subjekt bleibt der bloße Dienstleister der Betäubung.</p>""",
        "review_en": """<p><strong>“GluiV”</strong> dissects the vulgar veneer of jet-set materialism, forging luxury markers into a rigid psychological exoskeleton. The pounding staccato hook <span class="lyric-quote-highlight">“G, Louis V, waist bag, cocaine, I fuck everyone”</span> is no naive boast, but the frantic incantation of invulnerable omnipotence. The protagonist defines himself through perpetual motion and chemical fuel (<span class="lyric-quote-highlight">“Always moving, always on duty / Vitamin Zieh”</span>) to ward off introspective stillness.</p>
<p>The Airbnb tableau (<span class="lyric-quote-highlight">“Marble tiles in the Airbnb / Your rented paradise”</span>) exposes the total interchangeability of the actors. Yet beneath the aggressive grandiosity, the pre-hook reveals core vulnerability: <span class="lyric-quote-highlight">“And nevertheless, I'm not her type / Just the guy who brings the gear, she thinks”</span>. The luxury facade fractures against reality: the speaker is reduced to a disposable purveyor of chemical fuel.</p>""",
        "cards_de": [
            {
                "quote": "Ego FM Ibiza / Die synthetische Kulisse",
                "body": """Der Radio-Jingle rahmt den Track in die künstliche Welt kommerzieller Party-Euphorie ein. Die mediale Inszenierung großer Geschichten („big stories, big tunes“) etabliert die Insel als Hyperrealität, in der authentische Gefühle durch standardisierte Lifestyle-Formeln ersetzt werden.

Die Fassade der Daueranimation übertönt die innere Zerrüttung und zwingt das Subjekt in die Rolle des funktionierenden Rausch-Darstellers."""
            },
            {
                "quote": "G, Louis V, Bauchtasche, Kokain, ich fick' alle / Das materielle Exoskelett",
                "body": """Die repetitive Stakkato-Hook reiht Statussymbole und Drogen aneinander, um mit der Allmachtsformel „ich fick' alle“ ein unverwundbares Schutzschild zu errichten. Die Vulgarität ist kein naiver Protz, sondern der krampfhafte Versuch, Ohnmachtsgefühle durch demonstrierte Härte zu ersticken.

Jedes Markenemblem wird zur Rüstung gegen die eigene Bedeutungslosigkeit. Das Ich definiert seinen Wert ausschließlich über Konsum und Einschüchterung."""
            },
            {
                "quote": "Immer in Bewegung, immer im Dienst / Die Flucht vor dem Stillstand",
                "body": """Kinetische Rastlosigkeit als seelischer Überlebensreflex: Das Subjekt muss ununterbrochen „in Bewegung“ und „im Dienst“ bleiben, weil jeder Moment der Ruhe das unerträgliche Grundgefühl von Leere freisetzen würde. Kokain wird als „Vitamin Zieh“ verharmlost, um die Abhängigkeit als reine Leistungssteigerung zu verbuchen.

Die Reduktion der Frauen auf austauschbare Klischees („Ibiza Hadid“) entlarvt die vollständige Unfähigkeit zu echter zwischenmenschlicher Resonanz."""
            },
            {
                "quote": "Pool türkis wie bei David Hockney / Die gekränkte Eitelkeit",
                "body": """Mitten in der sonnendurchfluteten Hockney-Kulisse bricht die soziale Realität ein: Das Ich erkennt, dass es für die glamouröse Clique lediglich der funktionale Drogenlieferant ist („nur der Typ, der den Stoff bringt“). Das narzisstische Begehren scheitert an der Gleichgültigkeit des Gegenübers.

Die glamouröse Illusion zerschellt an der harten Tatsache, dass Reichtum und Rausch die fundamentale Einsamkeit des Dienstleisters nicht aufheben können."""
            },
            {
                "quote": "Marmorfliesen im Airbnb / Das geliehene Paradies",
                "body": """Das Setting im „Leihparadies“ entlarvt den parasitären Charakter der Szene: Nichts gehört einem selbst, alles ist gemietet, geborgt oder auf Zeit gekauft. Der misstrauische Blick der Freundin („findet mich mies / Und ich seh', sie sieht's“) droht die Maske zu lüften und erzeugt sofortige Paranoia.

Die Kälte der Marmorfliesen spiegelt die emotionale Temperatur der Beziehungen wider: Austauschbare Körper in einer gemieteten Kulisse auf Abruf."""
            }
        ],
        "cards_en": [
            {
                "quote": "Ego FM Ibiza / Synthetic backdrop",
                "body": """The radio drop frames the track inside commercial vacation euphoria. Framing events as "big stories, big tunes" establishes hyperreality where authentic feelings are replaced by lifestyle templates.

Perpetual broadcast cheer drowns internal distress, locking the subject into performative euphoria."""
            },
            {
                "quote": "G, Louis V, waist bag, cocaine, I fuck everyone / Material exoskeleton",
                "body": """Concatenating luxury markers and chemical fuel under the battle cry "I fuck everyone" fabricates an impenetrable armor. Vulgarity masks vulnerability with theatrical dominance.

Brand emblems function as shields against insignificance. Worth is asserted strictly through consumption and intimidation."""
            },
            {
                "quote": "Always moving, always on duty / Flight from stillness",
                "body": """Kinetic restlessness as survival reflex: remaining "always on duty" prevents introspective stillness from unearthing core emptiness. Cocaine trivialized as "Vitamin Zieh" recasts addiction as performance enhancement.

Reducing companions to Instagram tropes ("Ibiza Hadid") underscores affective impoverishment."""
            },
            {
                "quote": "Pool turquoise like David Hockney / Wounded vanity",
                "body": """Amid sun-drenched Hockney aesthetics, social reality pierces the fantasy: the speaker is reduced to a disposable drug runner ("just the guy who brings the gear"). Desire fractures against indifference.

Luxury veneers cannot obscure the isolation of the service provider."""
            },
            {
                "quote": "Marble tiles in the Airbnb / Rented paradise",
                "body": """The "rented paradise" tableau exposes the parasitic core: everything is leased, borrowed, or temporary. The companion's suspicious glare ("finds me awful / and I see she sees it") triggers hyper-vigilance.

Cold marble reflects relational climate: interchangeable bodies staged within temporary sets."""
            }
        ]
    },
    {
        "num": "04",
        "title": "Dachterrasse",
        "review_de": """<p>In <strong>„Dachterrasse“</strong> kippt der Rausch in die bleierne Kälte der Morgendämmerung. Vom Dach einer Luxusresidenz blickt der Protagonist auf die schlafenden Hotelburgen herab – isoliert in der Illusion, <span class="lyric-quote-highlight">„Auf der Dachterrasse weit oben, allem überlegen“</span> zu sein. Doch im Pre-Hook bricht das fundamentale Kindheitstrauma ungefiltert durch: <span class="lyric-quote-highlight">„Bis keiner mehr da ist, so wie damals meine Mutter / Glorreich, glorreich geh'n wir unter“</span>. Der narzisstische Höhenflug wird als desperate Bewältigung frühkindlicher Verlassenheit demaskiert.</p>
<p>Der zweite Vers formuliert die absolute Abwehr von Intimität: <span class="lyric-quote-highlight">„Wenn du wüsstest, was ich denk', ich will nicht, dass du mich kennst / Diese Existenz ist nicht mehr als ein One-Night-Stand“</span>. Das Mantra des Refrains – <span class="lyric-quote-highlight">„Man muss aufhör'n, wenn's am besten ist / Denn mit der Zeit wird alles lächerlich“</span> – ist kein Zeichen von Vernunft, sondern die panische Flucht vor dem Moment, in dem die Maske verrutscht und die eigene Bedürftigkeit sichtbar wird.</p>""",
        "review_en": """<p>In <strong>“Dachterrasse”</strong> (Rooftop), nocturnal ecstasy crashes into the leaden dawn. Suspended above sleeping hotel monoliths, the protagonist clings to the delusion of being <span class="lyric-quote-highlight">“On the rooftop terrace high above, superior to everything”</span>. Yet in the pre-hook, primary maternal abandonment erupts without defense: <span class="lyric-quote-highlight">“Until no one is left, just like my mother back then / Gloriously, gloriously we go down”</span>. Manic altitude is unmasked as an emergency response to foundational neglect.</p>
<p>The second verse articulates the absolute rejection of intimacy: <span class="lyric-quote-highlight">“If you knew what I think, I don't want you to know me / This existence is nothing more than a one-night stand”</span>. The recurring hook—<span class="lyric-quote-highlight">“You have to stop when it's best / Because in time everything turns ridiculous”</span>—is not wisdom, but the phobic compulsion to exit before the mask slips and dependency is exposed.</p>""",
        "cards_de": [
            {
                "quote": "Das erste Licht über den Bergen / Das bleierne Erwachen",
                "body": """Die Morgendämmerung entzieht dem nächtlichen Exzess seinen Schutzraum. Die Hotelburgen und die träumende Superjacht wirken wie leblose Monumente einer erstarrten Welt. Das Ich blickt von oben herab auf eine Szenerie, die jede Magie verloren hat.

Mit dem Verblassen der Nacht weicht die Euphorie einer körperlichen und seelischen Erschöpfung. Das Licht spendet keine Wärme, sondern beleuchtet die Trümmer der Nacht."""
            },
            {
                "quote": "Bis keiner mehr da ist, so wie damals meine Mutter / Das Urtrauma",
                "body": """Der Höhepunkt des Tracks reißt die tiefste Wunde auf: Das Gefühl, hoch über allem „überlegen“ zu sein, kippt unvermittelt in das unverarbeitete Trauma frühkindlicher Verlassenheit. Die Erinnerung an die Mutter entlarvt den gesamten Höhenflug als verzweifelten Versuch, den Schmerz des Verlassenwerdens durch aktive Distanzierung zu kontrollieren.

Der herannahende Absturz wird zynisch als „glorreich“ verbrämt, um der eigenen Ohnmacht einen heroischen Anstrich zu verleihen."""
            },
            {
                "quote": "Man muss aufhör'n, wenn's am besten ist / Der Fluchtreflex",
                "body": """Die Hook formuliert die phobische Angst vor dem Moment, in dem die Illusion kollabiert. Was wie rationale Lebensklugheit klingt, ist in Wahrheit die panische Flucht vor dem unausweichlichen Verfall und der Demaskierung.

Das Subjekt bricht Beziehungen und Momente ab, bevor das Gegenüber die Schwäche hinter der Fassade entdecken kann. Flucht wird zur einzigen verbleibenden Kontrollstrategie."""
            },
            {
                "quote": "Wenn du wüsstest, was ich denk', ich will nicht, dass du mich kennst / Die Barriere",
                "body": """Das radikale Verbot von Nähe: Der Satz „ich will nicht, dass du mich kennst“ zieht eine unüberwindbare Grenze. Die Sehnsucht nach einer „Sonne, die mich blendet“ und einem „Sommer, der nie endet“ verlangt nach permanenter Betäubung durch Reize.

Indem das gesamte Dasein zum flüchtigen „One-Night-Stand“ erklärt wird, schützt sich das Ich vor jeder verbindlichen Verantwortung und Bindung."""
            },
            {
                "quote": "Denn mit der Zeit wird alles lächerlich / Die Angst vor der Entblößung",
                "body": """Die bittere Schlusspointe: Die Furcht vor der Lächerlichkeit entlarvt die Fragilität des narzisstischen Selbstbildes. Dauer und Gewöhnung bedrohen das Image der Souveränität.

Wer rechtzeitig geht, hinterlässt das Bild eines Unnahbaren. Zurück bleibt die selbstgewählte Isolation als Preis für den Erhalt der Maske."""
            }
        ],
        "cards_en": [
            {
                "quote": "First light over mountains / Leaden dawn",
                "body": """Dawn strips nocturnal intoxication of its sanctuary. Sleeping monoliths and superyachts resemble petrified relics. Surveying the landscape from above reveals exhausted stillness.

Euphoria gives way to physical depletion. Daylight offers no warmth, illuminating wreckage."""
            },
            {
                "quote": "Until no one is left, like my mother / Primal wound",
                "body": """The track's emotional core: claimed supremacy fractures into maternal abandonment. Grandiosity is unmasked as an emergency attempt to master abandonment through pre-emptive isolation.

Impending ruin is romanticized as "glorious" to salvage heroic agency."""
            },
            {
                "quote": "You have to stop when it's best / Exit reflex",
                "body": """The chorus articulates phobic terror of disillusionment. Mimicking life advice, it masks compulsive departure before vulnerability is exposed.

Severing intimacy first preserves control over the narrative."""
            },
            {
                "quote": "I don't want you to know me / Fortress wall",
                "body": """Absolute intimacy taboo: "I don't want you to know me" bars genuine contact. Craving perpetual sunlight demands sensory blinding.

Reducing existence to a "one-night stand" inoculates against emotional permanence."""
            },
            {
                "quote": "In time everything turns ridiculous / Terror of exposure",
                "body": """Cynical conclusion: dread of humiliation reveals narcissistic fragility. Familiarity threatens the illusion of supremacy.

Exiting pre-emptively preserves the aloof persona at the cost of total isolation."""
            }
        ]
    },
    {
        "num": "05",
        "title": "Für mich",
        "review_de": """<p><strong>„Für mich“</strong> legt das erotisch verbrämte Machtgefüge narzisstischer Bindung offen. Hinter der intimen Kulisse (<span class="lyric-quote-highlight">„Hinter einer blauen Tür / Unter einem Baldachin aus Seide / Will das Mondlicht Haut berühr'n / Auf der Innenseite deiner Beine“</span>) inszeniert das Ich die sexuelle Begegnung als totalen Unterwerfungsakt: <span class="lyric-quote-highlight">„Unter dir bin ich außer mir / Bis du klingst, als würdest du verzweifeln / Lass mich das Größte für dich sein / Lass es das Größte für mich sein, das ich erreiche“</span>. Intimität ist hier kein Raum für Augenhöhe, sondern der exklusive Maßstab des eigenen narzisstischen Geltungsdrangs.</p>
<p>Die Hook fordert die vollständige Selbstaufgabe des Partners (<span class="lyric-quote-highlight">„Gib dich auf, auf für mich / Geb' mich, geb' mich auf, auf für dich“</span>), während das Ich eine scheinbare Gegenseitigkeit nur vorspiegelt. Im zweiten Vers formuliert Tua die unheilvolle Symbiose in einem der prägnantesten Vergleiche des Albums: <span class="lyric-quote-highlight">„Wir gehör'n zusamm'n wie Größenwahn und Scheitern“</span>. In der Bridge begründet das Ich seinen Kontrollzwang mit mathematischer Unerbittlichkeit: <span class="lyric-quote-highlight">„Was ich brauch', ist Sicherheit / Durch null kann man nicht mehr teil'n“</span>.</p>""",
        "review_en": """<p><strong>“Für mich”</strong> (For Myself) exposes the eroticized machinery of narcissistic attachment. Behind the intimate staging (<span class="lyric-quote-highlight">“Behind a blue door / Under a canopy of silk / Moonlight wants to touch skin / On the inside of your legs”</span>), the speaker frames sexual encounter as an act of absolute subjugation: <span class="lyric-quote-highlight">“Under you I am beside myself / Until you sound like you're despairing / Let me be the greatest for you / Let it be the greatest thing for me to achieve”</span>. Intimacy is reduced to fuel for the speaker's supremacy.</p>
<p>The hook demands the partner's total self-surrender (<span class="lyric-quote-highlight">“Give yourself up, up for me / Giving myself up, up for you”</span>), while mutuality is merely simulated. In the second verse, Tua formulates this fatal symbiosis: <span class="lyric-quote-highlight">“We belong together like megalomania and failure”</span>. In the bridge, the speaker justifies his need for control with mathematical finality: <span class="lyric-quote-highlight">“What I need is security / You cannot divide by zero”</span>.</p>""",
        "cards_de": [
            {
                "quote": "Hinter einer blauen Tür / Das erotische Machtspiel",
                "body": """Hinter der ästhetisierten Kulisse aus Seide und Mondlicht inszeniert das Ich die sexuelle Vereinigung als totalen Unterwerfungsakt. Die Zeile „Bis du klingst, als würdest du verzweifeln“ entlarvt die fatale Verwechslung von Schmerz und Intimität: Dominanz wird als Beweis eigener Lebendigkeit konsumiert.

Die Bitte „Lass mich das Größte für dich sein“ offenbart die absolute Abhängigkeit des Egos: Es existiert nur im Spiegel der vollständigen Hingabe des gequälten Anderen."""
            },
            {
                "quote": "Gib dich auf, auf für mich / Die geforderte Selbstaufgabe",
                "body": """Die Hook verlangt die bedingungslose Kapitulation des Partners. Das scheinbare Zugeständnis „Geb' mich auf für dich“ ist eine mimische Farce; echte Reziprozität findet nicht statt.

Die Beziehung wird zum parasitären Konstrukt, in dem die Identität des Partners ausgelöscht wird, um das schwankende Selbstwertgefühl des Protagonisten zu stabilisieren."""
            },
            {
                "quote": "Wir gehör'n zusamm'n wie Größenwahn und Scheitern / Das toxische Band",
                "body": """Die treffende Selbsterkenntnis der eigenen Zerstörungskraft: Die Paarung von Größenwahn und Scheitern beschreibt die unausweichliche Dynamik pathologischer Beziehungen. Das Geständnis, dass diese destruktive Macht vielleicht „alles ist, was ich erreicht hab'“, legt die innere Verwüstung schonungslos offen.

Das Ich begreift seine eigene Toxizität, nutzt dieses Wissen jedoch nicht zur Umkehr, sondern als melancholische Rechtfertigung für das Weitermachen."""
            },
            {
                "quote": "Was ich brauch', ist Sicherheit / Durch null kann man nicht mehr teil'n / Die mathematische Kälte",
                "body": """Der Kontrollzwang wird mit mathematischer Unerbittlichkeit begründet. Indem der Partner auf den Wert Null reduziert (entmachtet und isoliert) wird, wird jedes weitere Teilen mit der Außenwelt unmöglich.

Sicherheit entsteht hier nicht aus Vertrauen, sondern aus der totalen Ausschaltung jeder Autonomie des Gegenübers."""
            }
        ],
        "cards_en": [
            {
                "quote": "Behind a blue door / Erotic power dynamics",
                "body": """Beneath silk canopies and moonlight, intimacy is weaponized as subjugation. "Until you sound like you're despairing" conflates agony and ecstasy: dominance serves as proof of aliveness.

"Let me be the greatest for you" exposes total reliance on being mirrored through the other's surrender."""
            },
            {
                "quote": "Give yourself up for me / Compulsory surrender",
                "body": """The chorus demands unconditional capitulation. Reciprocity ("giving myself up for you") is pure mimicry.

The bond mutates into a parasitic dynamic where partner identity is erased to stabilize the fragile ego."""
            },
            {
                "quote": "Megalomania and failure / Toxic symbiosis",
                "body": """Self-diagnosis of destructive capacity: megalomania and failure define the trajectory of malignant attachment. Admitting dominance may be "all I have achieved" unmasks spiritual ruin.

Awareness brings no repentance, functioning instead as a melancholic rationale to persist."""
            },
            {
                "quote": "Security / Cannot divide by zero / Mathematical finality",
                "body": """Compulsive control expressed with mathematical rigor: reducing the partner to zero (isolated and disempowered) makes sharing with the world impossible.

Security is engineered through total suppression of partner autonomy."""
            }
        ]
    },
    {
        "num": "06",
        "title": "Rette mich nicht",
        "review_de": """<p>In <strong>„Rette mich nicht“</strong> verweigert das Ich jede Form partnerschaftlicher Rettung und zelebriert seine autodestruktive Autonomie. In rastloser Manie rast der Protagonist durch die Nacht (<span class="lyric-quote-highlight">„Immer unterwegs mit den Feinden / Adern voller Gift / Kickdown, rauchende Reifen / Mercadona, Parkplatz-Drift“</span>), um die Grenze des Erträglichen zu testen. Das Hilfsangebot des Gegenübers wird mit zynischem Stolz abgewehrt: <span class="lyric-quote-highlight">„Um mich zu ruinier'n, brauch' ich keinen / Das schaff' ich auch alleine“</span>.</p>
<p>Die Hook deklariert die totale emotionale Verflachung: <span class="lyric-quote-highlight">„Rette mich nicht / Ich hass' dich nicht, du bist mir bloß egal / Ich laufe durch das Niemandsland in überlebensgroß / Tauche in die Zwielichter und hoff', ich geh' verlor'n“</span>. Im zweiten Vers wendet sich das Ich direkt an die verlassene Partnerin (<span class="lyric-quote-highlight">„Ich bin das Problem und ich weiß es / Nur macht es das nicht kleiner, Gianna“</span>), ehe die Bridge jede romantisierte Bindung zerschlägt: <span class="lyric-quote-highlight">„Wir leben nicht in derselben Realität / Du liebst mich nicht, du kriegst nur nicht, was dir fehlt / Du solltest mich einfach vergessen / Wie leichte Versprechen auf weißen Tabletten in Zeitraffer-Nächten“</span>.</p>""",
        "review_en": """<p>In <strong>“Rette mich nicht”</strong> (Do Not Save Me), the speaker rejects every relational rescue attempt, celebrating his autodestructive autonomy. In restless mania, the protagonist races through the night (<span class="lyric-quote-highlight">“Always on the move with the enemies / Veins full of poison / Kickdown, smoking tires / Mercadona parking lot drift”</span>) testing the limits of endurance. All offers of help are met with cynical defiance: <span class="lyric-quote-highlight">“To ruin myself, I don't need anyone / I can do that on my own”</span>.</p>
<p>The chorus declares complete affective flattening: <span class="lyric-quote-highlight">“Do not save me / I don't hate you, you just don't matter to me / I run through no man's land larger than life / Dive into twilight and hope I get lost”</span>. In the second verse, the speaker addresses the abandoned partner directly (<span class="lyric-quote-highlight">“I am the problem and I know it / But that doesn't make it smaller, Gianna”</span>), before the bridge dismantles all romanticized illusion: <span class="lyric-quote-highlight">“We don't live in the same reality / You don't love me, you just don't get what you lack / You should just forget me / Like light promises on white tablets in time-lapse nights”</span>.</p>""",
        "cards_de": [
            {
                "quote": "Um mich zu ruinier'n, brauch' ich keinen / Das schaff' ich auch alleine / Die beanspruchte Selbstzerstörung",
                "body": """Das Ich rast mit Feinden durch die Nacht und beansprucht den eigenen Ruin als exklusives Hoheitsgebiet. Das Hilfsangebot des Partners wird mit zynischem Stolz abgewehrt: Wer sich selbst zerstört, behält die letzte Kontrolle und verweigert dem anderen die Retterrolle.

Die Raserei auf dem Parkplatz und das Gift in den Adern dramatisieren den Drang, sich über das Ausreizen der Schmerzgrenze überhaupt noch zu spüren."""
            },
            {
                "quote": "Ich hass' dich nicht, du bist mir bloß egal / Die vollkommene Entwertung",
                "body": """Die Hook trifft mit eisiger Kälte: Gleichgültigkeit ist grausamer als Hass, da sie dem Gegenüber jede Existenzberechtigung abspricht. Das Wandern als „überlebensgroße“ Gestalt im Niemandsland überhöht das seelische Verschwinden zu einem heroischen Mythos.

Der Wunsch, verloren zu gehen („hoff', ich geh' verlor'n“), artikuliert den unausgesprochenen Todes- und Auflösungstrieb (Thanatos) hinter der manischen Fassade."""
            },
            {
                "quote": "Ich bin das Problem und ich weiß es / Nur macht es das nicht kleiner, Gianna / Die entwaffnende Schulddeklaration",
                "body": """Der direkte Appell an die verlassene Partnerin: Indem das Ich seine eigene Schuld proaktiv deklariert („Ich bin das Problem“), schlägt es dem Gegenüber jede therapeutische Argumentation aus der Hand. Selbsterkenntnis wird zur Waffe, die jede Veränderung blockiert.

Der Kontrast zwischen den Go-go-Girls im Club und der wartenden Frau am Smartphone zeichnet das zynische Gefälle der Bindung."""
            },
            {
                "quote": "Wie leichte Versprechen auf weißen Tabletten / Die chemische Vergänglichkeit",
                "body": """Die Bridge demontiert alle verbliebenen Bindungsillusionen: „Du liebst mich nicht, du kriegst nur nicht, was dir fehlt“ dekonstruiert das Helfersyndrom als eigene Bedürftigkeit. Worte und Schwüre werden mit weißen Tabletten verglichen – flüchtig, chemisch erzeugt und bei Tagesanbruch wertlos.

Das Subjekt fordert das Vergessenwerden ein, um sich endgültig aus dem moralischen Koordinatensystem zu verabschieden."""
            }
        ],
        "cards_en": [
            {
                "quote": "To ruin myself, I don't need anyone / Autodestructive sovereignty",
                "body": """Racing through the night with enemies, reclaiming ruin as sovereign property. Rejecting assistance preserves absolute control and frustrates the partner's savior complex.

Parking lot drifts and poisoned veins dramatize the impulse to breach pain thresholds to feel alive."""
            },
            {
                "quote": "Don't hate you, you just don't matter / Radical apathy",
                "body": """Indifference cuts deeper than hatred, stripping the other of meaning. Roaming "larger than life" romanticizes psychic disintegration into heroic myth.

Craving disappearance ("hope I get lost") expresses latent Thanatos beneath mania."""
            },
            {
                "quote": "I am the problem and I know it, Gianna / Pre-emptive culpability",
                "body": """Direct address to the partner: proactively admitting fault disarms therapeutic confrontation. Self-awareness is weaponized to stall transformation.

Contrasting dancers with the woman waiting by her phone underscores relational asymmetry."""
            },
            {
                "quote": "Light promises on white tablets / Chemical transience",
                "body": """Dismantling romantic projection: "you don't love me, you just lack what you need" unmasks codependency. Vows are equated to pills—ephemeral, synthetic, dissolving by dawn.

Demanding to be forgotten completes exit from moral accountability."""
            }
        ]
    },
    {
        "num": "07",
        "title": "Leicht",
        "review_de": """<p><strong>„Leicht“</strong> ist die Chronik einer abgestumpften Affektabflachung im hedonistischen Nachtleben. Aus purer Trägheit gerät der Protagonist in eine Villa-Party und beginnt eine flüchtige Begegnung ohne jede emotionale Beteiligung: <span class="lyric-quote-highlight">„Fang' zu flirten an, nur aus Routine / Finde sie nicht mal besonders heiß / Doch geteiltes Leid ist halbes Leid“</span>. Das unterlegte englische Sample (<span class="lyric-quote-highlight">„Trying to feel alright all the time“</span>) fungiert als resignatives Mantra.</p>
<p>Im zweiten Vers tritt die Dissoziation offen zutage: <span class="lyric-quote-highlight">„Blauer als die Scheinwerfer im Pool / Schaue mir von weit weg dabei zu / Alles fühlt sich als, als wär es geschäftlich / Echt ist nur die Leere, seit du weg bist“</span>. Die finale Entsorgung der Intimität vollzieht sich im Outro mit administrativer Gleichgültigkeit an der Taxitür: <span class="lyric-quote-highlight">„Sie will ballern, ich schenk' ihr ein Gramm / „Meld dich“, sagt sie, ich denke nicht dran / „Danke für den nicen Abend“, sagt sie / „Ja“, sag' ich und schließ' die Tür von ihr'm Taxi“</span>.</p>""",
        "review_en": """<p><strong>“Leicht”</strong> (Light / Easy) stands as a chronicle of emotional blunting within hedonistic nightlife. Wandering into a villa party out of sheer inertia, the protagonist initiates a hollow encounter: <span class="lyric-quote-highlight">“Start flirting just out of routine / Don't even find her particularly hot / But shared pain is half the pain”</span>. The underlying vocal loop (<span class="lyric-quote-highlight">“Trying to feel alright all the time”</span>) acts as a resigned mantra.</p>
<p>In the second verse, dissociation takes over: <span class="lyric-quote-highlight">“Bluer than the spotlights in the pool / Watching myself from far away / Everything feels commercial / Real is only the void since you left”</span>. Disposal of intimacy occurs at the taxi door with administrative coldness: <span class="lyric-quote-highlight">“She wants to party, I give her a gram / 'Call me,' she says, I don't think about it / 'Thanks for the nice evening,' she says / 'Yeah,' I say and close the door of her taxi”</span>.</p>""",
        "cards_de": [
            {
                "quote": "Fang' zu flirten an, nur aus Routine / Das mechanische Begehren",
                "body": """Die Begegnung auf der Party ist frei von echter Leidenschaft: Flirten läuft als automatisierte „Routine“ ab. Das Ich findet das Gegenüber nicht einmal attraktiv, nutzt die Situation aber als Betäubungsmittel gegen die eigene Einsamkeit („geteiltes Leid ist halbes Leid“).

Intimität verkommt zur seelenlosen Transaktion zweier Menschen, die sich gegenseitig als Rauschmittel konsumieren."""
            },
            {
                "quote": "Trying to feel alright all the time / Der Zwang zum Wohlbefinden",
                "body": """Das geloopte englische Sample bringt den Kernkonflikt der hedonistischen Kultur auf den Punkt: Der Zwang, sich permanent gut zu fühlen, erstickt jede authentische Regung und mündet in chronischer Taubheit.

Die Bitte „Mach' es mir leicht“ ist die Kapitulation vor der emotionalen Komplexität des realen Lebens."""
            },
            {
                "quote": "Schaue mir von weit weg dabei zu / Die Dissoziation",
                "body": """Mitten im Geschehen spaltet sich das Bewusstsein ab: Das Ich beobachtet den eigenen Körper wie einen fremden Darsteller im Scheinwerferlicht des Pools. Alles wirkt steril und „geschäftlich“; als einzige reale Empfindung bleibt die Leere nach dem Verlust.

Die emotionale Resonanzachse zur Umwelt ist vollständig gekappt; die Party wird zum Stummfilm."""
            },
            {
                "quote": "„Ja“, sag' ich und schließ' die Tür von ihr'm Taxi / Die finale Entsorgung",
                "body": """Die Begegnung endet an der Taxitür mit bürokratischer Gleichgültigkeit. Das Verschenken von Kokain begleicht die Schuld; das geheuchelte Einverständnis („Ja“) dient nur dazu, die Tür zuzuschlagen und die Person loszuwerden.

Das Geräusch der zufallenden Autotür besiegelt die sofortige Auslöschung der Begegnung aus dem Gedächtnis."""
            }
        ],
        "cards_en": [
            {
                "quote": "Flirting out of routine / Mechanical desire",
                "body": """Flirting without attraction, enacted as routine. Shared numbness serves as anesthetic ("shared pain is half the pain").

Intimacy degenerates into transactional consumption between isolated individuals."""
            },
            {
                "quote": "Trying to feel alright all the time / Compulsive euphoria",
                "body": """The vocal loop distills hedonistic pathology: compulsory optimization smothers authentic feeling into chronic numbness.

Pleading for lightness capitulates before emotional reality."""
            },
            {
                "quote": "Watching myself from far away / Dissociation",
                "body": """Consciousness detaches during intimacy: observing oneself as an alien actor under pool lights. Sensation feels commercial; void is the only remaining authenticity.

Emotional resonance severed; party reduced to silent cinema."""
            },
            {
                "quote": "Yeah, I say, closing the taxi door / Disposal",
                "body": """Meeting concluded with bureaucratic finality. Cocaine settles obligation; feigned consent ("yeah") expedites departure.

Slamming the taxi door executes immediate erasure from consciousness."""
            }
        ]
    },
    {
        "num": "08",
        "title": "Höhenflug + Tiefenrausch",
        "review_de": """<p><strong>„Höhenflug + Tiefenrausch“</strong> markiert den unausweichlichen dopaminergen Absturz und das depressive Epizentrum des Werks. In beklemmender Plastizität verdichtet Tua den Selbstekel: <span class="lyric-quote-highlight">„Bin ein alter Schwamm, den man mal wechseln müsste / Ich schreib' mich minus eins auf die Gästeliste / Wurde von 'nem Sorgenkind zum Sorgenking“</span>. Die manische Energie ist restlos verbrannt; die Couch wird zum schwarzen Loch, das den erstarrenden Körper verschlingt (<span class="lyric-quote-highlight">„Die Couch schluckt mich und spuckt mich nie mehr aus / Alle Energie verbraucht / Falle durch die Welt, bin im Fiebertraum / Zwischen Höhenflug und Tiefenrausch“</span>).</p>
<p>Die grausame Ehrlichkeit im zweiten Vers demaskiert die Funktion früherer Bindungen: <span class="lyric-quote-highlight">„Sorry, dass ich dir so lang was vorgemacht hab' / Hing nur mit dir rum, weil ich dich so gehasst hab'“</span>. In der Badewanne liegend, versucht das Ich seine somatische Existenz aufzulösen (<span class="lyric-quote-highlight">„Hundert Meter tief in mein'n Augenhöhl'n / Lieg' in der Wanne, versuch' mich aufzulösen“</span>), während die Wände im leeren Heldensaal unerbittlich näher rücken (<span class="lyric-quote-highlight">„Hör' jetzt Stimmen schweigen, der Heldensaal ist leer / Unendlich Langeweile, die Wände kommen näher“</span>).</p>""",
        "review_en": """<p><strong>“Höhenflug + Tiefenrausch”</strong> (High Flight + Deep Intoxication) captures the inescapable neurochemical crash and depressive ground zero of the album. With visceral clarity, Tua articulates saturated self-disgust: <span class="lyric-quote-highlight">“I'm an old sponge that should be replaced / I write myself minus one on the guestlist / Turned from a problem child into a problem king”</span>. Manic fuel is entirely spent; the sofa mutates into a black hole (<span class="lyric-quote-highlight">“The couch swallows me and never spits me out / All energy depleted / Falling through the world, in a fever dream / Between high flight and deep intoxication”</span>).</p>
<p>The brutal confession in the second verse exposes past intimacy: <span class="lyric-quote-highlight">“Sorry that I pretended for so long / Only hung out with you because I hated you so much”</span>. Submerged in the bathtub, the self attempts somatic dissolution (<span class="lyric-quote-highlight">“A hundred meters deep in my eye sockets / Lying in the tub, trying to dissolve”</span>) while the walls of the empty hall of heroes close in (<span class="lyric-quote-highlight">“Hearing voices fall silent now, the hall of heroes is empty / Infinite boredom, the walls coming closer”</span>).</p>""",
        "cards_de": [
            {
                "quote": "Kratze jede Wunde zu 'ner Narbe / Bin ein alter Schwamm / Der somatisierte Selbstekel",
                "body": """Das Ich erlebt den eigenen Körper und Geist als kontaminiertes Terrain: Wunden werden zwanghaft zu Narben aufgekratzt, und die eigenen Ambitionen liegen wie nutzloser Müll im Weg der verwahrlosten Wohnung herum.

Das Bild vom „alten Schwamm, den man mal wechseln müsste“ verdichtet die seelische Verunreinigung; die Selbstkrönung zum „Sorgenking“ verwandelt die biografische Misere in einen zynischen, abwertenden Adelstitel."""
            },
            {
                "quote": "Seit wie viel'n Tagen steht die Zeit still? / Sorry, dass mein Leben dein'n Vibe killt / Das Tabu der Depression",
                "body": """Im Pre-Hook erstarrt die innere Zeitrechnung: Das Subjekt ist maximal weit von jedem erstrebenswerten Lebensentwurf entfernt und erträgt die eigene Einsamkeit nicht mehr.

Die schuldhafte Entschuldigung „Sorry, dass mein Leben dein'n Vibe killt“ demaskiert die gnadenlose Realität der Party-Kultur: In einer Welt der verordneten Hochstimmung ist authentische Depression das ultimative gesellschaftliche Tabu."""
            },
            {
                "quote": "Die Couch schluckt mich und spuckt mich nie mehr aus / Das schwarze Loch der Katatonie",
                "body": """Die Couch mutiert zum schwarzen Loch der motorischen und seelischen Lähmung: Alle manische Energie ist restlos verbraucht, der Körper sinkt tonuslos in die Polster ein.

Das bipolare Pendeln „Zwischen Höhenflug und Tiefenrausch“ beschreibt den fatalen Kreislauf des Werks: Die erzwungene Ekstase der vorangegangenen Nächte fordert ihren unausweichlichen Preis im katatonischen Fiebertraum."""
            },
            {
                "quote": "Hing nur mit dir rum, weil ich dich so gehasst hab' / Die Projektionsfläche & Auflösung in der Wanne",
                "body": """Der zweite Vers eröffnet mit dem Bekenntnis toxischer Ausbeutung: Der Partner wurde nicht geliebt, sondern als Projektionsfläche für den eigenen unerträglichen Selbsthass instrumentalisiert.

Alkohol degradiert den Organismus zu einer lichtscheuen „fetten Schnecke“. In der Badewanne liegend, mit hundert Meter tiefen Augenhöhlen, fantasiert das Ich über die vollständige molekulare Auflösung der eigenen Existenz im Wasser."""
            },
            {
                "quote": "Hör' jetzt Stimmen schweigen, der Heldensaal ist leer / Das Ende des Theaters",
                "body": """In der Bridge verstummt der eingebildete Jubel des Publikums: Der erhabene „Heldensaal“ ist leer gefegt, und die Zimmerwände rücken klaustrophobisch näher.

Der nervös auf der Stelle springende Uhrzeiger visualisiert die Gefangenschaft im neurotischen Wiederholungszwang: Ohne Rausch und Theater blickt das Ich in die gähnende Leere der eigenen Existenz."""
            }
        ],
        "cards_en": [
            {
                "quote": "Scratching every wound into a scar / Old sponge / Somatized self-disgust",
                "body": """The subject experiences body and mind as contaminated territory: wounds are compulsively picked into scars, while ambitions lie scattered like discarded trash across the apartment floor.

The metaphor of an "old sponge that needs replacement" captures toxic saturation; crowning himself "problem king" converts personal misery into a cynical, self-mocking badge."""
            },
            {
                "quote": "How many days has time stood still? / Sorry my life kills your vibe / Taboo of depression",
                "body": """Internal temporality freezes in the pre-hook: the speaker stands infinitely removed from any authentic self, unable to endure isolation.

The defensive apology "sorry that my life kills your vibe" exposes hedonistic brutality: inside compulsory party culture, authentic depression is the unforgivable offense."""
            },
            {
                "quote": "The couch swallows me and never spits me out / Black hole of catatonia",
                "body": """The sofa mutates into a black hole of somatic paralysis: manic fuel is entirely spent, muscle tone evaporates into total stillness.

Oscillating "between high flight and deep intoxication" charts the fatal manic-depressive loop: artificial euphoria demands its inescapable toll in catatonic fever."""
            },
            {
                "quote": "Only hung out because I hated you / Projection screen & dissolution in the tub",
                "body": """The second verse unmasks relational exploitation: the partner was weaponized to absorb and reflect disowned self-hatred.

Alcohol reduces the physical organism to a sluggish snail fleeing daylight. Submerged in the tub with sunken eye sockets, the speaker craves complete molecular dissolution in water."""
            },
            {
                "quote": "Hearing voices fall silent, hall of heroes is empty / Collapse of theater",
                "body": """In the bridge, phantom applause abruptly dies: the grandiose "hall of heroes" stands completely deserted as walls contract claustrophobically.

The erratic clock hand depicts entrapment within compulsory repetition: stripped of intoxication and applause, the speaker confronts pure existential void."""
            }
        ]
    },
    {
        "num": "09",
        "title": "Dopamin Spike",
        "review_de": """<p><strong>„Dopamin Spike“</strong> zelebriert den Triumph der biochemischen Illusion über die Realität. Mit der ersten chemischen Welle wird jede Verpflichtung getilgt: <span class="lyric-quote-highlight">„Dopamin-Spike und mein Herz rast / Seit ich es dir nicht mehr hinterhertrag' / Baller' mich höher als die Schwerkraft / Hatte 1g, lege mehr nach / Jeder Satz hört sich legendär an / Und muss gar nicht wahr sein / Muss sich nur so anfühl'n“</span>. Tua formuliert hier das Manifest des postfaktischen Hedonismus: Wahrheit ist irrelevant, solange der Neurotransmitter feuert.</p>
<p>Die <span class="lyric-quote-highlight">„Sonnenbrille bei Nacht, denn ich bin in der Matrix“</span> schützt nicht nur die Mydriasis der Pupillen, sondern schirmt das Ich vor der Realität ab. Im zweiten Vers greift der Protagonist die moralische Integrität der Nüchternen an: <span class="lyric-quote-highlight">„High auf Moral, doch ich glaub's nicht / Denn es ist deine Wahrheit / Wegen der du so taub bist / Solang, bis du drauf bist“</span>. Ethik wird als bloße feige Selbstaufgabe entwertet.</p>""",
        "review_en": """<p><strong>“Dopamin Spike”</strong> celebrates the triumph of biochemical simulation over empirical reality. As the chemical surge hits, all relational obligation evaporates: <span class="lyric-quote-highlight">“Dopamine spike and my heart races / Since I stopped carrying it after you / Blasting myself higher than gravity / Had 1g, loading more / Every sentence sounds legendary / And doesn't need to be true / Just needs to feel like it”</span>. Tua articulates the core manifesto of post-truth hedonism: empirical truth is obsolete as long as neurotransmitters fire.</p>
<p>Wearing <span class="lyric-quote-highlight">“sunglasses at night, because I'm in the Matrix”</span> not only conceals dilated pupils, but seals the speaker inside a private bunker. In the second verse, the speaker devalues the moral compass of the sober: <span class="lyric-quote-highlight">“High on morals, but I don't buy it / Because it's your truth / That makes you so deaf / Until you're high on it”</span>. Ethics are dismissed as cowardly self-abnegation.</p>""",
        "cards_de": [
            {
                "quote": "Jeder Satz hört sich legendär an / Und muss gar nicht wahr sein / Das postfaktische Hochgefühl",
                "body": """Die Feier der chemischen Simulation: Wahrheit und Realität werden bedeutungslos, solange der „Dopamin-Spike“ das Belohnungszentrum flutet. Das Gefühl von Größe („baller' mich höher als die Schwerkraft“) ersetzt jede reale Substanz.

Lügen und Täuschungen stören nicht mehr, solange sie sich im Rausch „legendär“ anfühlen."""
            },
            {
                "quote": "Sonnenbrille bei Nacht, denn ich bin in der Matrix / Die hermetische Kapsel",
                "body": """Die Sonnenbrille schützt nicht nur die geweiteten Pupillen, sondern schirmt das Ich wie in einer geschlossenen „Matrix“ gegen die Realität ab. Die Schmetterlinge im Bauch sind kein Zeichen von Liebe, sondern die körperliche Vibration des Rausches.

Das Subjekt lebt in seiner privaten Simulation, in der niemand mehr an es heranreicht."""
            },
            {
                "quote": "High auf Moral, doch ich glaub's nicht / Der Angriff auf die Nüchternheit",
                "body": """Zynische Entwertung bürgerlicher Tugenden: Nüchterne Moral wird als bloße feige Ersatzsucht verspottet. Das Ich behauptet, die Moralisten seien taub für das wirkliche Leben, „solang, bis du drauf bist“.

Hier vollzieht die Persona die vollständige Pervertierung aller ethischen Maßstäbe."""
            }
        ],
        "cards_en": [
            {
                "quote": "Every sentence sounds legendary / Doesn't need to be true / Post-truth high",
                "body": """Chemical simulation celebrated: objective reality vanishes while dopamine inundates receptors. Artificial grandiosity replaces substance.

Deception causes no friction so long as it feels legendary in intoxication."""
            },
            {
                "quote": "Sunglasses at night in the Matrix / Hermetic firewall",
                "body": """Sunglasses conceal pupil dilation while sealing consciousness inside a Matrix firewall. Butterflies represent somatic drug vibration rather than romance.

The persona resides inside private simulation where contact is impossible."""
            },
            {
                "quote": "High on morals / Assault on sobriety",
                "body": """Moral integrity mocked as cowardly substitution. Claiming sober observers are blind until chemically altered inverts ethical norms.

Complete transvaluation of values through hedonistic cynicism."""
            }
        ]
    },
    {
        "num": "10",
        "title": "Amnesia",
        "review_de": """<p>In <strong>„Amnesia“</strong> explodiert die klaustrophobische Enge des Ibiza-Nachtlebens in roher, choreografierter Gewalt. Tua zeichnet die sensorische Reizüberflutung im Club mit schonungsloser Haptik: <span class="lyric-quote-highlight">„Diese EDM-Mucke hier drinne ist furchtbar / Ich hass' diese Nacht und ich hass' ihr'n Geburtstag / Lächel gezwung'n, renne aufs Klo, um zu koksen und weil ich Durst hab' / Wasser mit Salz, bitterer Schleim in mei'm Hals“</span>. Das erzwungene Lächeln auf der Geburtstagsfeier bricht unter dem akustischen Beschuss der EDM-Bässe zusammen.</p>
<p>Der Konflikt mit einem britischen Touristen wird zur ersehnten Entlastung: <span class="lyric-quote-highlight">„Du kommst mir grade recht / Junge, willst du, dass ich dir die Nase brech'?“</span>. Die Schlägerei ist kein Unfall, sondern die gezielte somatische Entladung unerträglicher innerer Spannungen. Im Moment des Club-Höhepunkts (<span class="lyric-quote-highlight">„Warte auf den Drop und die CO2-Kanon'n / Kalter Rauch, reiß' mich los / Und tret' ihm in sein Declan-Rice-Trikot“</span>) verschmelzen Bass-Drop und körperliche Brutalität zum finalen Exzess.</p>""",
        "review_en": """<p>In <strong>“Amnesia”</strong>, the sensory claustrophobia of mega-club nightlife detonates into raw, choreographed violence. Tua renders sensory overload with visceral tactility: <span class="lyric-quote-highlight">“This EDM music in here is terrible / I hate this night and I hate her birthday / Forced smile, run to the bathroom to do coke and because I'm thirsty / Water with salt, bitter slime in my throat”</span>. The social performance collapses under commercial EDM bombardment.</p>
<p>The altercation with a British tourist serves as a long-sought release: <span class="lyric-quote-highlight">“You're just what I needed / Boy, you want me to break your nose?”</span>. Violence is no accident, but a somatic mechanism discharging unbearable psychic friction. At the peak of the rave (<span class="lyric-quote-highlight">“Waiting for the drop and the CO2 cannons / Cold smoke, tear myself free / And kick him in his Declan Rice jersey”</span>), musical climax and physical brutality merge into ecstasy.</p>""",
        "cards_de": [
            {
                "quote": "Wasser mit Salz, bitterer Schleim in mei'm Hals / Die sensorische Hölle",
                "body": """Die Reizüberflutung im Megaclub Amnesia wird zur physischen Qual: Bitterer Schleim, rasender Puls und lärmende EDM-Bässe. Das Koksen auf der Toilette ist längst kein Vergnügen mehr, sondern der verzweifelte Versuch, das erzwungene Lächeln nicht kollabieren zu lassen.

Die aufgestaute Wut sucht nach einem Ventil und entlädt sich am Aussehen eines fremden Touristen."""
            },
            {
                "quote": "Du kommst mir grade recht / Die ersehnte Gewaltkatharsis",
                "body": """Die Schlägerei ist kein Unfall, sondern die gezielt herbeigeführte Explosion. Die Drohung, dem Gegenüber die Nase zu brechen, formuliert den Drang nach physischem Aufprall, um die eigene emotionale Taubheit mit Schmerz zu durchbrechen.

Gewalt wird zum letzten Mittel, sich im dissoziativen Taumel wieder als handelndes Subjekt zu spüren."""
            },
            {
                "quote": "Warte auf den Drop und die CO2-Kanon'n / Der choreografierte Schlag",
                "body": """Perfekte Synchronisation von Musikeffekt und Gewaltausbruch: Das Ich täuscht Beruhigung vor („Tranquilo“), um exakt im Moment des Bass-Drops und des kalten CO2-Rauchs zuzutreten („in sein Declan-Rice-Trikot“).

Körperliche Brutalität und elektronischer Club-Höhepunkt verschmelzen zu einem Moment roher Ekstase."""
            }
        ],
        "cards_en": [
            {
                "quote": "Saltwater, bitter slime in throat / Sensory torment",
                "body": """Mega-club overload experienced as physical agony: bitter drip, racing pulse, abrasive EDM. Snorting coke maintains the strained smile.

Repressed rage seeks a valve, targeting a foreign tourist."""
            },
            {
                "quote": "Just what I needed / Cathartic violence",
                "body": """Violence engineered as catharsis. Threatening broken bones seeks blunt somatic impact to shatter internal numbness.

Physical collision becomes the final tool to reclaim sensory aliveness."""
            },
            {
                "quote": "Waiting for drop and CO2 cannons / Choreographed strike",
                "body": """Synthesizing musical climax with physical assault: figning calmness ("Tranquilo") before striking inside the CO2 blast ("Declan Rice kit").

Brutality and rave peak fuse into unified ecstasy."""
            }
        ]
    },
    {
        "num": "11",
        "title": "Kaputt",
        "review_de": """<p><strong>„Kaputt“</strong> bildet das monumentale Finale und die radikale Selbstdemontage des Albums. Eingerahmt von der Totenstarre des Intros (<span class="lyric-quote-highlight">„Springmesser-Tattoo auf meiner Brust / Tu nicht so, als hast du nichts gewusst / Hand aufs Herz, ich spüre kein'n Puls / Deine Liebe blieb für immer im August“</span>) steht der Protagonist am Hafen zwischen Bauruinen und Schutt. Das Bild des verendeten Tieres spiegelt den Ruin des eigenen Charakters: <span class="lyric-quote-highlight">„Ein toter Hund liegt zwischen dem Bauschutt / Ich war nie viel mehr als 'ne Behauptung“</span>.</p>
<p>Die namensgebende Formel <span class="lyric-quote-highlight">„Was ich berühr', das geht kaputt / Ganzes Leben zerleg' ich zu Schutt“</span> artikuliert den Fluch des malignen Narzissmus: Die Unfähigkeit, Verbindung einzugehen, ohne sie zu vernichten. Der Schlusssatz des Albums – <span class="lyric-quote-highlight">„Und ich kam immer davon, aber niemals an“</span> – verweigert jede billige Erlösung. Das Werk endet in der glasklaren, unerbittlichen Erkenntnis der eigenen ewigen Entwurzelung.</p>""",
        "review_en": """<p><strong>“Kaputt”</strong> (Broken / Destroyed) stands as the monumental finale and radical self-demolition of the album. Framed by somatic rigor mortis in the intro (<span class="lyric-quote-highlight">“Switchblade tattoo on my chest / Don't act like you didn't know anything / Hand on my heart, I feel no pulse / Your love remained forever in August”</span>), the protagonist surveys coastal ruins. The carcass in the debris reflects the ruin of the false self: <span class="lyric-quote-highlight">“A dead dog lies in the rubble / I was never much more than an assertion”</span>.</p>
<p>The titular refrain <span class="lyric-quote-highlight">“Whatever I touch breaks / My whole life I smash into rubble”</span> articulates the tragedy of pathological narcissism: the inability to touch beauty without reducing it to ash. The closing realization—<span class="lyric-quote-highlight">“And I always got away, but never arrived”</span>—denies therapeutic resolution, terminating in the unsparing clarity of eternal self-exile.</p>""",
        "cards_de": [
            {
                "quote": "Hand aufs Herz, ich spüre kein'n Puls / Die seelische Nekrose",
                "body": """Das Springmesser-Tattoo auf der Brust als Waffe und Schutzschild: Das Ich stellt nüchtern fest, dass sein Herz nicht mehr schlägt. Die Liebe blieb unwiderruflich im „August“ zurück; übrig bleibt die Kälte des Hyperloops, in dem kein Gefühl mehr Fuß fassen kann.

Die Persona diagnostiziert ihren eigenen emotionalen Tod ohne Selbstmitleid."""
            },
            {
                "quote": "Was ich berühr', das geht kaputt / Der Fluch des Midas",
                "body": """Die zentrale Erkenntnis des Werks: Die namensgebende Formel artikuliert die Unfähigkeit, Schönes zu berühren, ohne es in Schutt zu verwandeln. Das Ich begreift sich als Gefangener einer ewigen Wiederholungsschleife („steck' für eine Ewigkeit in 'nem Loop“).

Die Einsicht, dass der Partner gehen muss („weil du musst“), ist der einzige Moment uneigennütziger Klarheit."""
            },
            {
                "quote": "Ein toter Hund liegt zwischen dem Bauschutt / Ich war nie viel mehr als 'ne Behauptung / Die Demontage des Falschen Selbst",
                "body": """Die Trostlosigkeit des Industriehafens zwischen Bauruinen und Schutt spiegelt den Zustand des Protagonisten. Der Schlüsselsatz „Ich war nie viel mehr als 'ne Behauptung“ zertrümmert das gesamte narzisstische Gebäude: Hinter der Maske lag keine wahre Identität, sondern nur die leere Behauptung von Größe.

Das Leben erweist sich als permanenter, zielloser „Aufbruch“ ohne Fundament."""
            },
            {
                "quote": "Und ich kam immer davon, aber niemals an / Das ewige Exil",
                "body": """Das Schlusswort des Albums: Das Ich entging jeder Strafe, jeder Bindung und jeder Rechenschaft („kam immer davon“), fand aber nirgendwo Heimat oder Frieden („niemals an“).

Das Werk schließt in der unbarmherzigen Erkenntnis der eigenen ewigen Heimatlosigkeit."""
            }
        ],
        "cards_en": [
            {
                "quote": "Hand on heart, no pulse / Emotional necrosis",
                "body": """Switchblade tattoo as armor: calculating cold diagnosis that no pulse remains. Love vanished in August; only synthetic hyperloop momentum remains.

The persona records internal death without self-pity."""
            },
            {
                "quote": "Whatever I touch breaks / Compulsive ruin",
                "body": """The central revelation: touching beauty reduces it to rubble. The speaker recognizes entrapment within chronic repetition loops.

Acknowledging the partner must leave represents rare authentic maturity."""
            },
            {
                "quote": "Dead dog in rubble / I was only an assertion / Shattering the False Self",
                "body": """Harbor rubble mirrors psychic wreckage. "I was never much more than an assertion" annihilates the false self: behind grandiosity lay no authentic identity.

Existence revealed as perpetual, homeless departure."""
            },
            {
                "quote": "Always got away, never arrived / Eternal exile",
                "body": """Final album testament: escaping accountability ("got away") without ever discovering peace ("never arrived").

The record terminates in unsparing ontological exile."""
            }
        ]
    }
]

# Official YouTube Playlist IDs
yt_ids = {
    "01": "B57Cfur5gmo",
    "02": "8aRKRKHTEu0",
    "03": "U4oCu0Ddsmw",
    "04": "0spWTbvgpUA",
    "05": "Kf3nIF8r05Y",
    "06": "1OjuBWxIV9I",
    "07": "aqKJA8C3qnw",
    "08": "qpVAoWbGV1g",
    "09": "lyOFF32dEao",
    "10": "spCXhlxPLBk",
    "11": "bKS0-KAdPNw"
}

# TrackList in JS
track_list_js = "const trackList = [\n"
for t in tracks_data:
    t_num = t["num"]
    t_title = t["title"]
    slug = f"{t_num}_{t_title.replace(' ', '_').replace('+', 'und')}"
    yt_id = yt_ids.get(t_num, "")
    track_list_js += f'  {{ num: "{t_num}", title: "{t_title}", audioDe: "audio/de/{slug}.mp3", audioEn: "audio/en/{slug}.mp3", ytId: "{yt_id}" }},\n'
track_list_js += "];"

adapted_js = re.sub(r'const trackList = \[.*?\];', track_list_js, tomora_js, flags=re.DOTALL)
adapted_js = adapted_js.replace('TOMORA', 'TUA — F60.8')
adapted_js = adapted_js.replace('const audioSrc = `audio/track_${track.num}_${currentLang}.mp3`;', 'const audioSrc = currentLang === "de" ? track.audioDe : track.audioEn;')


# Explicit semantic card mapping for every track and stanza
stanza_mappings = {
    "01": [0, 1, 2, 3], # [Part 1]->0, [Part 2]->1, [Hook]->2, [Outro]->3
    "02": [0, 1, 2, 1, 3, 4], # [Part 1]->0, [Hook]->1, [Part 2]->2, [Hook]->1, [Bridge]->3, [Outro]->4
    "03": [0, 1, 2, 3, 1, 4, 3, 1], # [Intro]->0, [Hook]->1, [Part 1]->2, [Pre-Hook]->3, [Hook]->1, [Part 2]->4, [Pre-Hook]->3, [Hook]->1
    "04": [0, 1, 2, 3, 1, 2, 4], # [Part 1]->0, [Pre-Hook]->1, [Hook]->2, [Part 2]->3, [Pre-Hook]->1, [Hook]->2, [Outro]->4
    "05": [1, 0, 1, 1, 2, 1, 3, 1, 1], # [Intro]->1, [Part 1]->0, [Hook]->1, [Post-Hook]->1, [Part 2]->2, [Hook]->1, [Bridge]->3, [Hook]->1, [Outro]->1
    "06": [0, 0, 1, 1, 2, 1, 3, 1, 1, 3], # [Intro]->0, [Part 1]->0, [Hook]->1, [Post-Hook]->1, [Part 2]->2, [Hook]->1, [Bridge]->3, [Hook]->1, [Post-Hook]->1, [Outro]->3
    "07": [1, 0, 1, 2, 1, 1, 3], # [Intro]->1, [Part 1]->0, [Hook]->1, [Part 2]->2, [Hook]->1, [Bridge]->1, [Outro]->3
    "08": [0, 0, 1, 2, 3, 1, 2, 4, 1], # [Intro]->0, [Part 1]->0, [Pre-Hook]->1, [Hook]->2, [Part 2]->3, [Pre-Hook]->1, [Hook]->2, [Bridge]->4, [Outro]->1
    "09": [1, 0, 1, 1, 2, 1, 1], # [Intro]->1, [Part 1]->0, [Hook]->1, [Interlude]->1, [Part 2]->2, [Hook]->1, [Outro]->1
    "10": [0, 0, 1, 2, 1], # [Intro]->0, [Part 1]->0, [Hook]->1, [Part 2]->2, [Hook]->1
    "11": [0, 1, 2, 1, 3, 0], # [Intro]->0, [Hook]->1, [Part]->2, [Hook]->1, [Bridge]->3, [Outro]->0
}

def get_card_idx_for_line(t_num, s_idx, l_idx, line_text, total_cards):
    mapping = stanza_mappings.get(t_num)
    if isinstance(mapping, list) and s_idx < len(mapping):
        return min(mapping[s_idx], total_cards - 1)
    return min(s_idx, total_cards - 1)


# Assemble index.html
html_parts = []

html_parts.append(f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TUA — F60.8 (2025) | Interaktive Werkanalyse & Interpretation</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script src="https://www.youtube.com/iframe_api"></script>
{orange_css}
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
    html_parts.append(f"""      <li><a href="#track-{t['num']}">{t['num']} — {t['title']}</a></li>\n""")

html_parts.append("""    </ul>
  </div>

  <!-- Hero Cover Image -->
  <div class="hero-fullbleed">
    <img src="cover.png" alt="TUA — F60.8 Cover" class="hero-video" style="object-fit: cover; object-position: center 78%; max-height: 75vh; width: 100%;">
  </div>




  <!-- Main Content -->
  <main class="main-wrapper">
    <header class="album-header">
      <span class="album-meta-tag">
        <span class="lang-de">ICD-10 F60.8 • Vollständige Werkanalyse & Psychogramm</span>
        <span class="lang-en">ICD-10 F60.8 • Full Work Analysis & Psychogram</span>
      </span>
      <h1 class="album-main-title">TUA — F60.8</h1>
      <p class="album-subtitle">
        <span class="lang-de">Eine detaillierte literarische, kulturjournalistische und psychoanalytische Untersuchung über Narzissmus, post-hedonistische Taubheit und den Mythos des freien Falls.</span>
        <span class="lang-en">An in-depth literary, cultural-journalistic, and psychoanalytic examination of narcissism, post-hedonistic numbness, and the myth of free fall.</span>
      </p>
    </header>

    <div class="tracks-list">
""")

# Build Tracks
for t in tracks_data:
    t_num = t["num"]
    t_title = t["title"]
    raw = raw_lyrics[t_num]
    cards_de = t["cards_de"]
    cards_en = t["cards_en"]
    total_cards = len(cards_de)
    
    html_parts.append(f"""
    <section class="track-section" id="track-{t_num}">
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

    # Render stanzas and map trigger lines to cards
    line_global_counter = 0
    num_stanzas = len(raw["stanzas"])
    
    for s_idx, stanza in enumerate(raw["stanzas"]):
        st_title = stanza["title"].strip("[] ")
        lines = [l.strip() for l in stanza["lines"] if l.strip()]
        if not lines:
            continue
        
        html_parts.append(f"""          <div class="stanza">\n            <div class="stanza-title">[{st_title}]</div>\n""")
        for l_idx, line in enumerate(lines):
            assigned_card_idx = get_card_idx_for_line(t_num, s_idx, l_idx, line, total_cards)
            html_parts.append(f"""            <div class="lyric-line annotated" data-line-idx="{line_global_counter}"><span class="lyric-trigger" data-track-num="{t_num}" data-target-card="{assigned_card_idx}">{line}</span></div>\n""")
            line_global_counter += 1
        html_parts.append("""          </div>\n""")


    # Right column: DE/EN Review & Card Deck
    html_parts.append(f"""        </div>
        <div class="analysis-col">
          
          <div class="lang-block lang-de">
            <div class="analysis-view-wrapper">
              <div class="narrative-review" id="review-{t_num}-de">
                {t['review_de']}
              </div>
              <div class="card-deck-view" id="card-deck-{t_num}-de" style="display: none;">
""")

    for idx, c in enumerate(cards_de):
        html_parts.append(f"""                <div class="analysis-card" id="card-{t_num}-de-{idx}" data-card-idx="{idx}">
                  <div class="card-header-bar">
                    <button class="card-back-btn" data-track-num="{t_num}" data-lang="de" aria-label="Zurück zur Review">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    </button>
                    <span class="card-badge-counter">
                      <span class="lang-de">Tiefen-Analyse {idx + 1} / {total_cards}</span>
                      <span class="lang-en">Deep Analysis {idx + 1} / {total_cards}</span>
                    </span>
                  </div>
                  <span class="card-quote">„{c['quote']}“</span>
                  <div class="card-body">
                    <p>{c['body'].replace(chr(10)+chr(10), '</p><p>').replace(chr(10), '<br>')}</p>
                  </div>
                </div>
""")

    html_parts.append(f"""              </div>
            </div>
          </div>

          <div class="lang-block lang-en">
            <div class="analysis-view-wrapper">
              <div class="narrative-review" id="review-{t_num}-en">
                {t['review_en']}
              </div>
              <div class="card-deck-view" id="card-deck-{t_num}-en" style="display: none;">
""")

    for idx, c in enumerate(cards_en):
        html_parts.append(f"""                <div class="analysis-card" id="card-{t_num}-en-{idx}" data-card-idx="{idx}">
                  <div class="card-header-bar">
                    <button class="card-back-btn" data-track-num="{t_num}" data-lang="en" aria-label="Back to Review">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    </button>
                    <span class="card-badge-counter">
                      <span class="lang-de">Tiefen-Analyse {idx + 1} / {total_cards}</span>
                      <span class="lang-en">Deep Analysis {idx + 1} / {total_cards}</span>
                    </span>
                  </div>
                  <span class="card-quote">“{c['quote']}”</span>
                  <div class="card-body">
                    <p>{c['body'].replace(chr(10)+chr(10), '</p><p>').replace(chr(10), '<br>')}</p>
                  </div>
                </div>
""")

    html_parts.append("""              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
""")

# Footer & Bottom Player
html_parts.append(f"""    </div>
  </main>

  <!-- Footer -->
  <footer>
    <p>TUA — F60.8 (2025) • MULTIMODALE INTERAKTIVE WERKANALYSE</p>
    <p>Recherche- &amp; Analysemethodik nach Close-Reading- &amp; Dissect-Standard</p>
  </footer>

  <!-- FLOATING BOTTOM MINI PLAYER (Glass Dock) -->
  <div class="bottom-player" id="bottomPlayer">
    <div class="player-left">
      <div class="player-track-info">
        <span class="player-track-num" id="bpTrackNum">01</span>
        <span class="player-track-title" id="bpTrackTitle">1996</span>
      </div>
      <div class="player-subtitle">
        <span class="lang-de">TUA • F60.8 (2025)</span>
        <span class="lang-en">TUA • F60.8 (2025)</span>
      </div>
    </div>
    <div class="player-center">
      <div class="player-controls">
        <button class="ctrl-btn" id="bpPrevBtn" aria-label="Previous Track">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 6 6 18 8.5 18 8.5 6"></polygon><polygon points="18 6 9.5 12 18 18 18 6"></polygon></svg>
        </button>
        <button class="play-pause-circle" id="bpPlayPauseBtn" aria-label="Play / Pause">
          <svg class="bp-play-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="8 5 19 12 8 19 8 5"></polygon></svg>
          <svg class="bp-pause-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><rect x="6" y="5" width="4" height="14"></rect><rect x="14" y="5" width="4" height="14"></rect></svg>
        </button>
        <button class="ctrl-btn" id="bpNextBtn" aria-label="Next Track">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><polygon points="18 6 18 18 15.5 18 15.5 6"></polygon><polygon points="6 6 14.5 12 6 18 6 6"></polygon></svg>
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

  <div id="ytPlayer" style="display:none;position:absolute;width:1px;height:1px;left:-9999px;"></div>

{adapted_js}
</body>
</html>
""")

full_html = "".join(html_parts)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Genuine Tomora-Standard App successfully written to index.html ({len(full_html.encode('utf-8'))} bytes)")
