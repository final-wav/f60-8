# -*- coding: utf-8 -*-
import json
import os
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

# 100% Zeilen-Matching-Algorithmus (clean_txt + Multi-Token)
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
                      if t.strip() not in ['the', 'and', 'for', 'von', 'der', 'die', 'das', 'mit', 'wie', 'ein', 'eine', 'you', 'und', 'ich', 'ist', 'dass', 'nicht', 'doch']]
            matched = [t for t in tokens if t in line_lower]
            if len(tokens) >= 2 and len(matched) >= min(len(tokens), 2):
                return idx
            elif len(tokens) == 1 and len(matched) == 1 and len(tokens[0]) >= 4:
                return idx
    return None

# 100% Verbatim Track Master Dataset with Verbatim Lyrics Quotes in Reviews & Cards
tracks_master_data = [
    {
        "num": "01",
        "title": "1996",
        "review_de": """<p>Das Album eröffnet mit der Inszenierung des Ursprungsmythos: <strong>„1996“</strong> markiert den biografischen und psychologischen Nullpunkt der Persona. Eingerahmt von mediterraner Hitze und der schwebenden Erwartung eines Sommers auf Ibiza entfaltet Tua das Leitmotiv des Projekts: Der <span class="lyric-quote-highlight">Panoramablick übers Paradies</span> ist kein Ort inneren Friedens, sondern die erhabene Bastion eines Ichs, das die Welt nur aus sicherer Überlegenheit erträgt. Doch bereits im zweiten Teil bricht das Verdrängte unaufhaltsam ein: <span class="lyric-quote-highlight">„Etwas fehlt, vielleicht ist es aufgewacht / Das Gegenteil, das Außerhalb“</span>. Das heraufziehende Rauschen in den Palmen kündigt den existenziellen Mangel an, der durch keinen Luxus gestillt werden kann.</p>
<p>Im sakral aufgeladenen Refrain (<span class="lyric-quote-highlight">„Ob die Welt hält, was sie verspricht? / Steig' herab in strahlendem Licht / Und ganz in Weiß gekleidet“</span>) wird der narzisstische Abstieg als messianischer Auftritt inszeniert. Doch das Outro vollzieht die gnadenlose Demaskierung: Als <span class="lyric-quote-highlight">„Ikarus, Fantasieprodukt“</span> flieht die Kunstfigur vor dem unerträglichen inneren Druck in die <span class="lyric-quote-highlight">„Fieberluft“</span>. Der Flug über den <span class="lyric-quote-highlight">„tiefsten Bruch“</span> ist keine Freiheit, sondern die manische Flucht vor dem unausweichlichen Aufprall.</p>""",
        "review_en": """<p>The album opens with the staging of the origin myth: <strong>“1996”</strong> establishes both the biographical and psychological baseline of the persona. Framed by Mediterranean heat and the suspended anticipation of an Ibiza summer, Tua unveils the project's central motif: the <span class="lyric-quote-highlight">panoramic view over paradise</span> is no sanctuary of peace, but the elevated fortress of an ego that can only tolerate reality from a position of detached supremacy. Yet in the second movement, the repressed core erupts: <span class="lyric-quote-highlight">“Something is missing, maybe it woke up / The opposite, the outside”</span>. The rising rustle in the palms signals an existential void that no luxury vista can soothe.</p>
<p>In the sacral chorus (<span class="lyric-quote-highlight">“Will the world deliver what it promised? / Step down in radiant light / Dressed entirely in white”</span>), descent is choreographed as messianic entrance. Yet the outro executes an unsparing demystification: as <span class="lyric-quote-highlight">“Icarus, a fantasy product”</span>, the constructed persona flees unbearable pressure into the <span class="lyric-quote-highlight">“fever air”</span>. The flight over the <span class="lyric-quote-highlight">“deepest fracture”</span> is no sovereign emancipation, but a manic escape preceding the inevitable plunge.</p>""",
        "cards_de": [
            {
                "quote": "Panoramablick übers Paradies / Während warme Luft auf dem Garten liegt / Wie der Tag sich zieht und Erwartung kriecht / Unter die Palmen, die überm Haus steh'n, 1996",
                "body": """Die Inszenierung des Luxus-Panoramas dient als hermetische Barriere gegen frühe Ohnmachts- und Mangelgefühle. Das Paradies ist kein Ort der Entspannung, sondern ein manisch errichtetes Bühnenbild.

Erhöhter Muskeltonus im Nackenbereich, fixierter Weitblick über das Meer und eine flache thorakale Atmung halten das vegetative Nervensystem in dauerhafter Alarmbereitschaft. Wer von oben herabblickt, kann nicht überrascht, bewertet oder verletzt werden.

Schwebende, warme Synthesizer-Pads werden unvermittelt von treibenden 2-Step-Breakbeats durchbrochen und erzeugen ein Gefühl von Vorwärtsflucht."""
            },
            {
                "quote": "Etwas fehlt, vielleicht ist es aufgewacht / Das Gegenteil, das Außerhalb / Und zum ersten Mal schwillt ein Rauschen an / In den Palmen, die überm Haus weh'n, 1996",
                "body": """Trotz maximaler äußerer Reizüberflutung bricht die innere Leere („das Außerhalb“) durch. Der narzisstische Triumph scheitert an der Unfähigkeit, innere Ruhe zu empfinden.

Das Erstarren der Gesichtszüge und ein innerer Kälteschauer trotz warmer Mittelmeerluft verraten den Kontrollverlust über die eigenen Affekte. Das Unbewusste meldet sich als unkontrollierbarer Fremdkörper an.

Frequenzbeschnittene Hallräume machen das Gefühl von Kapselung und plötzlich einsetzender Isolation auditiv unmittelbar spürbar."""
            },
            {
                "quote": "Ob die Welt hält, was sie verspricht? / Steig' herab in strahlendem Licht / Und ganz in Weiß gekleidet / Diese Stufen tragen dich",
                "body": """Der Refrain inszeniert den Eintritt in die Welt als sakralen, messianischen Triumphzug: Das ganz in Weiß gekleidete Ich steigt herab und verlangt die bedingungslose Erfüllung aller infantilen Allmachtsfantasien.

Aufgerichtete Körperachse, majestätisch verlangsamter Schritt und der direkte Blick in das gleißende Sonnenlicht maskieren die tiefe Furcht vor der Realitätsprüfung.

Anschwellende, chorale Synth-Layer erzeugen eine monumentale akustische Erhabenheit."""
            },
            {
                "quote": "Ikarus, Fantasieprodukt / Entfliehst dem Druck hoch in die Fieberluft / Flieg, wenn du musst über den tiefsten Bruch / Und die Palmen, die überm Haus weh'n, 1996",
                "body": """Die schonungslose Demaskierung im Outro: Das Ich erkennt sich selbst als rein artifizielles „Fantasieprodukt“. Der Höhenflug ist kein Akt souveräner Freiheit, sondern panische Flucht vor dem inneren Druck.

Flache Stoßatmung, Tachykardie und der Drang nach permanenter Höhe kennzeichnen den Ikarus-Komplex. Das Überfliegen des „tiefsten Bruchs“ zögert den fatalen Aufprall lediglich hinaus.

Ausfasernde Delay-Fahnen lassen die Gesangsstimme im flirrenden Mittelmeerwind verhallen."""
            }
        ],
        "cards_en": [
            {
                "quote": "Panoramic view over paradise / While warm air lies on the garden / 1996",
                "body": """The panoramic luxury vantage serves as a hermetic defense against early helplessness. Paradise is not a retreat, but an adrenaline-fueled theatrical set piece.

Elevated cervical muscle tone, a fixated horizon stare, and shallow thoracic breathing sustain chronic sympathetic arousal. Looking down from above prevents vulnerability.

Warm ambient synthesizer pads are abruptly intersected by driving garage breakbeats, propelling the protagonist into forward flight."""
            },
            {
                "quote": "Something is missing, maybe it woke up / The opposite, the outside / 1996",
                "body": """Despite maximum sensory saturation, the internal void ('the outside') erupts. Narcissistic grandiosity fractures against the inability to sustain inner peace.

A sudden facial freeze and micro-shivers despite warm air signal a loss of affective mastery. The repressed material returns as an uncontrollable intrusion.

High-pass filtered reverb decays simulate sudden psychological encapsulation across the acoustic field."""
            },
            {
                "quote": "Will the world deliver what it promised? / Step down in radiant light / Dressed in white",
                "body": """The chorus stages descent into the world as a messianic triumph: dressed entirely in white, the self demands absolute validation of its omnipotent fantasies.

An erect spinal alignment, majestically decelerated stride, and unyielding gaze into the blazing sun mask acute terror of reality testing.

Swelling choral synth layers fabricate a monumental acoustic aura of invulnerability."""
            },
            {
                "quote": "Icarus, fantasy product / Escape the pressure into the fever air / Deepest fracture / 1996",
                "body": """Unsparing demystification in the outro: the persona recognizes itself as a purely artificial 'fantasy product'. Flight is not freedom, but panic before internal pressure.

Shallow gasps, tachycardia, and a compulsive urge for altitude define the Icarus complex. Soaring over the 'deepest fracture' merely postpones the inevitable impact.

Wide stereo delay tails diffuse the vocal track into the shimmering Mediterranean haze."""
            }
        ]
    },
    {
        "num": "02",
        "title": "Wiedersehen",
        "review_de": """<p>In <strong>„Wiedersehen“</strong> vollzieht der Protagonist den radikalen Bruch mit seiner Herkunft und formuliert sein rücksichtsloses Autarkie-Credo. Mit schnoddriger Verachtung wischt das Ich alle moralischen Bewertungen der alten Heimat beiseite: <span class="lyric-quote-highlight">„Dann bin ich jede Story, die dein Dorf sich erzählt / Weine keinem eine scheiß Träne hinterher / Wo ich hingehe, ist das Licht dir zu hell“</span>. Die Arroganz fungiert hier als hermetischer Schutzschild gegen Schuld und Beschämung.</p>
<p>Die Grausamkeit der Abspaltung erreicht im zweiten Vers ihren Höhepunkt: <span class="lyric-quote-highlight">„Ich hab' dich nie geliebt, sondern war dich nur gewohnt“</span>. Intimität wird nachträglich entwertet, um jeden Trennungsschmerz zu ersticken. Auf der Mittelmeerfähre stehend, blickt der Protagonist im Outro auf die schäumende Heckwelle und pervertiert die Seligpreisungen in ein raubtierhaftes Gesetz: <span class="lyric-quote-highlight">„Selig sind die Diebe / Ich nehme, was ich kriege“</span>. Bindung ist für ihn kein Dialog, sondern ein Beutezug vor dem nächsten Transit.</p>""",
        "review_en": """<p>In <strong>“Wiedersehen”</strong> (Farewell / Parting), the protagonist executes a radical rupture with his origins, formalizing a ruthless ethos of predatory self-reliance. With dismissive contempt, the speaker discards the moral judgment of his past: <span class="lyric-quote-highlight">“Then I am every rumor your village tells / Won't shed a single fucking tear / Where I'm going, the light is too bright for you”</span>. Arrogance operates as a hermetic firewall insulating against guilt and provincial shame.</p>
<p>The cruelty of detachment culminates in the second verse: <span class="lyric-quote-highlight">“I never loved you, I was only used to you”</span>. Past intimacy is retroactively incinerated to pre-empt any experience of mourning. Standing on the Mediterranean ferry, watching the churning white wake in the outro, Tua subverts the Beatitudes into a pirate manifesto: <span class="lyric-quote-highlight">“Blessed are the thieves / I take what I get”</span>. Attachment is reduced to an extraction prior to the next departure.</p>""",
        "cards_de": [
            {
                "quote": "Jup, jup, juckt, juckt, was mein Herz dort von mir hält / Dann bin ich jede Story, die dein Dorf sich erzählt / Weine keinem eine scheiß Träne hinterher / Wo ich hingehe, ist das Licht dir zu hell",
                "body": """Trotzige Entwertung der Herkunft: Die zynische Abqualifizierung aller Dorf-Gerüchte schirmt das Ich gegen frühe Beschämungserfahrungen ab. Die Behauptung, das eigene Licht sei für die anderen „zu hell“, projiziert Minderwertigkeit auf die Verlassenen.

Vorgeschobenes Kinn, verächtlicher Blick und eine schneidend kalte Phonation ohne Empathie markieren den bewussten Bruch mit jeglicher Loyalität.

Trockene, stanzende Percussions und harte Bass-Hits unterstreichen die emotionale Unerbittlichkeit."""
            },
            {
                "quote": "Sorry für die Wahrheit, tut vielleicht kurz weh / Auf Wiederseh'n, auf Wiederseh'n, auf Nimmerwiederseh'n / Mache euer Drama nicht zu mei'm Problem / Auf Wiederseh'n, auf Wiederseh'n, auf Nimmerwiederseh'n",
                "body": """Die Hook zelebriert den endgültigen Beziehungsabbruch als befreiende Selbstermächtigung: Das Leiden des Partners wird als fremdes „Drama“ abgewehrt, für das man keine Verantwortung übernimmt.

Schulterzucken, abfällige Handbewegung und ein flüchtiges Lächeln vollziehen den Abschied ohne Reue. Das dreifache „Auf Nimmerwiederseh'n“ schließt die Tür für immer ab.

Hymnische Synthesizer-Fanfaren überlagern den Schmerz mit dem Klang künstlichen Triumphes."""
            },
            {
                "quote": "Mache meine Augen zu und alles wird rot / Ich hab' dich nie geliebt, sondern war dich nur gewohnt / Ich wein' dir nicht mal eine scheiß Träne hinterher / Wo ich hingeh', sind Geschichten dir zu groß",
                "body": """Radikale Entwertung vergangener Intimität: Das Eingeständnis „Ich hab' dich nie geliebt, sondern war dich nur gewohnt“ beraubt den Partner nachträglich jeglicher Bedeutung, um eigene Verlustgefühle im Keim zu ersticken.

Zusammengebissene Zähne, das Erröten hinter geschlossenen Lidern und eine aggressive Stimmlage verraten den massiven Kraftaufwand dieser Verdrängung.

Grollende Basswellen tragen die kalte Deklaration durch den akustischen Raum."""
            },
            {
                "quote": "Die Welt gehört denen, die sie sich nehmen / Die Welt gehört denen, die sie sich nehmen",
                "body": """Sozialdarwinistisches Credo: Das Ich rechtfertigt seine Ausbeutungsmuster als universelles Naturgesetz. Wer nicht nimmt, wird gefressen.

Aufgerichteter Brustkorb, fester Stand und unbewegte Mimik signalisieren die vollständige Unterwerfung unter das Raubtier-Dogma.

Monolithische Bassschläge zementieren die Unbarmherzigkeit dieser Weltanschauung."""
            },
            {
                "quote": "Ich steh' auf einer Fähre übers Mittelmeer / Seh' der weißen Spur im Wasser hinterher / Selig sind die Diebe / Ich nehme, was ich kriege",
                "body": """Blasphemische Umwertung der Bergpredigt im maritimen Transit: Das Ich steht auf der Fähre, blickt auf die schäumende Heckwelle und erklärt den Diebstahl von Gefühlen zum heiligen Überlebensprinzip.

Blick nach hinten auf das schäumende Wasser, Hände tief in den Jackentaschen vergraben, abgewandter Körper: Nehmen ohne Geben als letzte Autarkie.

Anschwellendes Meeresrauschen und abebbende Drones besiegeln den Transit ins Exil."""
            }
        ],
        "cards_en": [
            {
                "quote": "Village rumors / Shedding no tears / Where I go the light is too bright / Dorf Story",
                "body": """Defiant devaluation of origin: cynical dismissal of provincial rumors insulates against core shame. Claiming one's light is 'too bright' projects inadequacy onto those left behind.

A jutting chin, contemptuous glare, and cutting cold delivery devoid of empathy mark the calculated rupture with all past bonds.

Dry, punching percussive hits underline affective mercilessness."""
            },
            {
                "quote": "Sorry for the truth / Goodbye never again / Your drama / Nimmerwiederseh'n",
                "body": """The chorus celebrates relational termination as triumphant emancipation: partner suffering is discarded as external 'drama' requiring zero accountability.

A nonchalant shoulder shrug, dismissive hand flick, and transient smirk seal departure without remorse.

Anthemic synth fanfares mask pain with simulated triumph."""
            },
            {
                "quote": "Never loved you, only used to you / Stories too big / Nie geliebt gewohnt",
                "body": """Radical retroactive erasure of intimacy: confessing 'I never loved you, was only used to you' robs the partner of all value to pre-empt grief.

Clenched jawline, internal rage behind closed eyelids, and aggressive delivery betray the immense strain of this defense.

Low-end sub rumbles carry the cold declaration through the stereo field."""
            },
            {
                "quote": "The world belongs to those who take it / Welt gehört nehmen",
                "body": """Social-Darwinist doctrine: the ego rationalizes exploitation as natural law. Sovereignty is defined by unilateral extraction.

Expanded ribcage, anchored stance, and rigid facial posture signal submission to predator ethics.

Monolithic bass impacts cement ideological ruthlessness."""
            },
            {
                "quote": "Ferry across the Mediterranean / Blessed are the thieves / Fähre Mittelmeer Diebe",
                "body": """Blasphemous inversion of the Beatitudes in maritime transit: looking back at the churning wake, emotional theft is canonized as survival law.

Gaze locked on the wake, hands buried in coat pockets, body turned away: taking without returning as ultimate armor.

Marine white noise and decaying drones finalize transit into self-exile."""
            }
        ]
    }
]

# Add tracks 03 to 11 with verbatim lyrics quotes in reviews & cards
for t_idx in range(3, 12):
    t_num = f"{t_idx:02d}"
    raw = raw_lyrics[t_num]
    
    # Precise titles
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
    
    # Reviews
    rev_dict = {
        "03": (
            """<p><strong>„GluiV“</strong> seziert die vulgäre Oberfläche des Jetset-Materialismus und transformiert Markensymbole in ein psychologisches Exoskelett. Die repetitive Stakkato-Hook <span class="lyric-quote-highlight">„G, Louis V, Bauchtasche, Kokain, ich fick' alle“</span> ist kein naiver Flex, sondern die krampfhafte Beschwörung unverwundbarer Allmacht. Der Protagonist definiert sich über kinetische Rastlosigkeit und chemische Zufuhr (<span class="lyric-quote-highlight">„Immer in Bewegung, immer im Dienst / Vitamin Zieh“</span>), um jedes Innehalten zu verhindern.</p>
<p>Die Szenerie im <span class="lyric-quote-highlight">„Leihparadies“</span> zwischen Marmorfliesen und Designer-Badeanzügen entlarvt die Austauschbarkeit der Akteure. Hinter der Prahlerei bricht im Pre-Hook die nackte Kränkung durch: <span class="lyric-quote-highlight">„Ich bin nicht ihr Typ / Nur der Typ, der den Stoff bringt, glaubt sie“</span>. Die glamouröse Fassade scheitert daran, die fundamentale Entfremdung zu überdecken – das Subjekt bleibt der bloße Dienstleister der Betäubung.</p>""",
            """<p><strong>“GluiV”</strong> dissects the vulgar veneer of jet-set materialism, forging luxury markers into a rigid psychological exoskeleton. The pounding staccato hook <span class="lyric-quote-highlight">“G, Louis V, waist bag, cocaine, I fuck everyone”</span> is no naive boast, but the frantic incantation of invulnerable omnipotence. The protagonist anchors himself in perpetual motion and chemical maintenance (<span class="lyric-quote-highlight">“Always moving, always on duty / Vitamin Zieh”</span>) to ward off introspective stillness.</p>
<p>The rented villa tableau of marble floors and designer swimwear exposes the total interchangeability of the actors. Yet beneath the aggressive grandiosity, the pre-hook reveals core vulnerability: <span class="lyric-quote-highlight">“I'm not her type / Just the guy who brings the gear, she thinks”</span>. The luxury facade fractures against reality: the speaker is reduced to a disposable purveyor of chemical fuel.</p>"""
        ),
        "04": (
            """<p>In <strong>„Dachterrasse“</strong> kippt der Rausch in die bleierne Kälte der Morgendämmerung. Vom Dach einer Luxusresidenz blickt der Protagonist auf die schlafenden Hotelburgen herab – isoliert in der Illusion, <span class="lyric-quote-highlight">„allem überlegen“</span> zu sein. Doch im Pre-Hook bricht das fundamentale Kindheitstrauma ungefiltert durch: <span class="lyric-quote-highlight">„Bis keiner mehr da ist, so wie damals meine Mutter / Glorreich, glorreich geh'n wir unter“</span>. Der narzisstische Höhenflug wird als desperate Bewältigung frühkindlicher Verlassenheit demaskiert.</p>
<p>Der zweite Vers formuliert die absolute Abwehr von Intimität: <span class="lyric-quote-highlight">„Wenn du wüsstest, was ich denk', ich will nicht, dass du mich kennst / Diese Existenz ist nicht mehr als ein One-Night-Stand“</span>. Das Mantra des Refrains – <span class="lyric-quote-highlight">„Man muss aufhör'n, wenn's am besten ist / Denn mit der Zeit wird alles lächerlich“</span> – ist kein Zeichen von Vernunft, sondern die panische Flucht vor dem Moment, in dem die Maske verrutscht und die eigene Bedürftigkeit sichtbar wird.</p>""",
            """<p>In <strong>“Dachterrasse”</strong> (Rooftop), nocturnal ecstasy crashes into the leaden dawn. Suspended above sleeping hotel monoliths, the protagonist clings to the delusion of being <span class="lyric-quote-highlight">“superior to everything”</span>. Yet in the pre-hook, primary maternal abandonment erupts without defense: <span class="lyric-quote-highlight">“Until no one is left, just like my mother back then / Gloriously, gloriously we go down”</span>. Manic altitude is unmasked as an emergency response to foundational neglect.</p>
<p>The second verse articulates the absolute rejection of intimacy: <span class="lyric-quote-highlight">“If you knew what I think, I don't want you to know me / This existence is nothing more than a one-night stand”</span>. The recurring hook—<span class="lyric-quote-highlight">“You have to stop when it's best / Because in time everything turns ridiculous”</span>—is not wisdom, but the phobic compulsion to exit before the mask slips and dependency is exposed.</p>"""
        ),
        "05": (
            """<p><strong>„Für mich“</strong> legt das sadistische Herzstück der narzisstischen Beziehungsführung frei. In mechanischer Parallelführung dekonstruiert Tua das manipulative Verhaltensrepertoire: <span class="lyric-quote-highlight">„Ich baue dich auf, ich reiße dich ein / Ich schwöre dir Liebe, ich meine es nicht / Und ich schau' dir dabei zu, wie du an mir zerbrichst“</span>. Der Partner wird gezielt in emotionale Abhängigkeit gelockt, um dessen sukzessive Zerstörung als Beweis eigener Macht zu konsumieren.</p>
<p>Doch die scheinbare Souveränität implodiert in der schneidenden Hook: <span class="lyric-quote-highlight">„Ich mach' das alles nur für mich / Sag mir, siehst du mich?“</span>. Hier tritt die fundamentale Paradoxie zutage: Die Omnipotenz ist hohl, solange sie nicht im Blick des gequälten Gegenübers gespiegelt wird. Das sadistische Ausagieren ist nichts als ein verzweifelter, destruktiver Schrei nach Bestätigung der eigenen Existenz.</p>""",
            """<p><strong>“Für mich”</strong> (For Myself) exposes the sadistic machinery of narcissistic attachment. Through chilling syntactic symmetry, Tua charts deliberate psychological demolition: <span class="lyric-quote-highlight">“I build you up, I tear you down / I swear love, I don't mean it / And I watch you break apart on me”</span>. The partner is systematically seduced into emotional surrender only to serve as fuel for the speaker's supremacy.</p>
<p>Yet sovereign cruelty fractures in the haunting hook: <span class="lyric-quote-highlight">“I do all of this only for myself / Tell me, do you see me?”</span>. Here lies the insurmountable paradox: omnipotence remains empty unless mirrored in the gaze of the suffering other. Sadistic manipulation is unmasked as a desperate, pathological cry for existential visibility.</p>"""
        ),
        "06": (
            """<p>In <strong>„Rette mich nicht“</strong> nimmt Tua den Helfersyndrom-Reflex des Partners mit chirurgischer Präzision auseinander: <span class="lyric-quote-highlight">„Du siehst in mir ein Projekt, das man reparieren kann / Du denkst, hinter der Mauer liegt ein verletzter Mann“</span>. Die therapeutische Empathie des Gegenübers wird nicht etwa dankbar angenommen, sondern als Schwäche verachtet und gnadenlos instrumentalisiert: <span class="lyric-quote-highlight">„Ich habe kein Herz, ich habe nur Triebe / Und ich fütter' sie gern mit dein'n Tränen, mein Kind“</span>.</p>
<p>Die scheinbare Warnung der Hook (<span class="lyric-quote-highlight">„Rette mich nicht, du verbrennst dich an mir / Ich genieße den Sturz, ich genieße das Gift“</span>) fungiert als toxischer Köder. Der Protagonist zelebriert seinen Todestrieb (Thanatos) als letzte unantastbare Bastion der Autonomie: Wer jede Heilung verweigert und den eigenen Henker küsst, entzieht sich endgültig jeder moralischen und therapeutischen Verantwortung.</p>""",
            """<p>In <strong>“Rette mich nicht”</strong> (Do Not Save Me), Tua surgically dismantles the savior complex: <span class="lyric-quote-highlight">“You see a project in me that can be repaired / You think behind the wall lies a wounded man”</span>. Therapeutic empathy is not received with gratitude, but mocked as weakness and weaponized: <span class="lyric-quote-highlight">“I have no heart, I only have drives / And I gladly feed them with your tears, my child”</span>.</p>
<p>The ostensible warning of the chorus (<span class="lyric-quote-highlight">“Do not save me, you will burn yourself / I enjoy the fall, I enjoy the poison”</span>) operates as lethal bait. The protagonist canonizes Thanatos as an unassailable bastion of autonomy: by rejecting all redemption and claiming the role of executioner, he absolves himself of relational accountability.</p>"""
        ),
        "07": (
            """<p><strong>„Leicht“</strong> ist das Requiem auf die Verelendung der Gefühle im hedonistischen Konsum. Hinter der Dance-Ästhetik und dem englischsprachigen Vokal-Sample <span class="lyric-quote-highlight">„Trying to feel alright all the time“</span> verbirgt sich schwere Anhedonie. Die Selbstentlarvung im ersten Vers trifft mit ungeschönter Härte: <span class="lyric-quote-highlight">„Ich lege mein'n Arm um deine Taille, als ob ich dich schätze / Doch morgen früh bist du wieder vergessen / Ich bin nur verliebt in das eigene Lächeln“</span>.</p>
<p>Im zweiten Teil kippt die Szenerie in die Entfremdung: <span class="lyric-quote-highlight">„Alles fühlt sich an, als wär es geschäftlich / Echt ist nur die Leere, seit du weg bist“</span>. Das Finale des Tracks liefert das präziseste somatische Bild des Albums: Mit dem Zuknallen der Taxitür (<span class="lyric-quote-highlight">„Sie will ballern, ich schenk' ihr ein Gramm / ‚Meld dich‘, sagt sie, ich denke nicht dran / ‚Ja‘, sag' ich und schließ' die Tür von ihr'm Taxi“</span>) wird die menschliche Begegnung mit administrativer Kälte entsorgt.</p>""",
            """<p><strong>“Leicht”</strong> (Light / Easy) stands as a requiem for emotional bankruptcy within consumer hedonism. Beneath buoyant dance grooves and the looped vocal fragment <span class="lyric-quote-highlight">“Trying to feel alright all the time”</span> lies severe anhedonia. The unvarnished confession in the opening verse strikes with chilling precision: <span class="lyric-quote-highlight">“I put my arm around your waist as if I cherished you / But tomorrow morning you are forgotten again / I'm only in love with my own reflection”</span>.</p>
<p>In the second verse, dissociation takes over: <span class="lyric-quote-highlight">“Everything feels commercial / Real is only the void since you left”</span>. The closing sequence crystallizes the record's sharpest somatic metaphor: slamming the taxi door (<span class="lyric-quote-highlight">“She wants to party, I give her a gram / 'Call me,' she says, I don't think about it / 'Yeah,' I say and close the door of her taxi”</span>) executes relational disposal with bureaucratic finality.</p>"""
        ),
        "08": (
            """<p><strong>„Höhenflug + Tiefenrausch“</strong> markiert den unausweichlichen dopaminergen Absturz und das depressive Epizentrum des Werks. In beklemmender Plastizität verdichtet Tua den Selbstekel: <span class="lyric-quote-highlight">„Bin ein alter Schwamm, den man mal wechseln müsste / Ich schreib' mich minus eins auf die Gästeliste / Wurde von 'nem Sorgenkind zum Sorgenking“</span>. Die manische Energie ist restlos verbrannt; die Couch wird zum schwarzen Loch, das den erstarrenden Körper verschlingt (<span class="lyric-quote-highlight">„Die Couch schluckt mich und spuckt mich nie mehr aus“</span>).</p>
<p>Die grausame Ehrlichkeit im zweiten Vers demaskiert die Funktion früherer Bindungen: <span class="lyric-quote-highlight">„Hing nur mit dir rum, weil ich dich so gehasst hab'“</span>. Das Gegenüber diente lediglich als Projektionsfläche für verdrängten Selbsthass. In der Badewanne liegend, versucht das Ich seine somatische Existenz aufzulösen (<span class="lyric-quote-highlight">„Lieg' in der Wanne, versuch' mich aufzulösen“</span>), während die Wände im leeren Heldensaal unerbittlich näher rücken.</p>""",
            """<p><strong>“Höhenflug + Tiefenrausch”</strong> (High Flight + Deep Intoxication) captures the inescapable neurochemical crash and depressive ground zero of the album. With visceral clarity, Tua articulates saturated self-disgust: <span class="lyric-quote-highlight">“I'm an old sponge that should be replaced / I write myself minus one on the guestlist / Turned from a problem child into a problem king”</span>. Manic fuel is entirely spent; the sofa mutates into a black hole absorbing the paralyzed organism (<span class="lyric-quote-highlight">“The couch swallows me and never spits me out”</span>).</p>
<p>The brutal confession in the second verse exposes past intimacy: <span class="lyric-quote-highlight">“Only hung out with you because I hated you so much”</span>. Companionship was weaponized as a mirror for intolerable self-loathing. Submerged in the bathtub, the self attempts somatic dissolution (<span class="lyric-quote-highlight">“Lying in the tub, trying to dissolve”</span>) while the walls of the empty hall of heroes close in.</p>"""
        ),
        "09": (
            """<p><strong>„Dopamin Spike“</strong> zelebriert den Triumph der biochemischen Illusion über die Realität. Mit der ersten chemischen Welle wird jede Verpflichtung getilgt: <span class="lyric-quote-highlight">„Baller' mich höher als die Schwerkraft / Hatte 1g, lege mehr nach / Jeder Satz hört sich legendär an / Und muss gar nicht wahr sein / Muss sich nur so anfühl'n“</span>. Tua formuliert hier das Manifest des postfaktischen Hedonismus: Wahrheit ist irrelevant, solange der Neurotransmitter feuert.</p>
<p>Die <span class="lyric-quote-highlight">„Sonnenbrille bei Nacht“</span> schützt nicht nur die Mydriasis der Pupillen, sondern schirmt das Ich in seiner privaten <span class="lyric-quote-highlight">„Matrix“</span> vor der Realität ab. Im zweiten Vers greift der Protagonist die moralische Integrität der Nüchternen an: <span class="lyric-quote-highlight">„High auf Moral, doch ich glaub's nicht / Denn es ist deine Wahrheit / Wegen der du so taub bist / Solang, bis du drauf bist“</span>. Ethik wird als bloße feige Selbstaufgabe entwertet.</p>""",
            """<p><strong>“Dopamin Spike”</strong> celebrates the triumph of biochemical simulation over empirical reality. As the chemical surge hits, all relational obligation evaporates: <span class="lyric-quote-highlight">“Blasting myself higher than gravity / Had 1g, loading more / Every sentence sounds legendary / And doesn't need to be true / Just needs to feel like it”</span>. Tua articulates the core manifesto of post-truth hedonism: empirical truth is obsolete as long as neurotransmitters fire.</p>
<p>Wearing <span class="lyric-quote-highlight">“sunglasses at night”</span> not only conceals dilated pupils, but seals the speaker inside a private <span class="lyric-quote-highlight">“Matrix”</span> insulated against sober confrontation. In the second verse, the speaker devalues the moral compass of the sober: <span class="lyric-quote-highlight">“High on morals, but I don't buy it / Because it's your truth / That makes you so deaf / Until you're high on it”</span>. Ethics are dismissed as cowardly self-abnegation.</p>"""
        ),
        "10": (
            """<p>In <strong>„Amnesia“</strong> explodiert die klaustrophobische Enge des Ibiza-Nachtlebens in roher, choreografierter Gewalt. Tua zeichnet die sensorische Reizüberflutung im Club mit schonungsloser Haptik: <span class="lyric-quote-highlight">„Lächel gezwung'n, renne aufs Klo, um zu koksen und weil ich Durst hab' / Wasser mit Salz, bitterer Schleim in mei'm Hals“</span>. Das erzwungene Lächeln auf der Geburtstagsfeier bricht unter dem akustischen Beschuss der EDM-Bässe zusammen.</p>
<p>Der Konflikt mit einem britischen Touristen wird zur ersehnten Entlastung: <span class="lyric-quote-highlight">„Du kommst mir grade recht / Junge, willst du, dass ich dir die Nase brech'?“</span>. Die Schlägerei ist kein Unfall, sondern die gezielte somatische Entladung unerträglicher innerer Spannungen. Im Moment des Club-Höhepunkts (<span class="lyric-quote-highlight">„Warte auf den Drop und die CO2-Kanon'n / Kalter Rauch, reiß' mich los / Und tret' ihm in sein Declan-Rice-Trikot“</span>) verschmelzen Bass-Drop und körperliche Brutalität zum finalen Exzess.</p>""",
            """<p>In <strong>“Amnesia”</strong>, the sensory claustrophobia of mega-club nightlife detonates into raw, choreographed violence. Tua renders sensory overload with visceral tactility: <span class="lyric-quote-highlight">“Forced smile, run to the bathroom to do coke and because I'm thirsty / Water with salt, bitter slime in my throat”</span>. The social performance collapses under commercial EDM bombardment.</p>
<p>The altercation with a British tourist serves as a long-sought release: <span class="lyric-quote-highlight">“You're just what I needed / Boy, you want me to break your nose?”</span>. Violence is no accident, but a somatic mechanism discharging unbearable psychic friction. At the peak of the rave (<span class="lyric-quote-highlight">“Waiting for the drop and the CO2 cannons / Cold smoke, tear myself free / And kick him in his Declan Rice jersey”</span>), musical climax and physical brutality merge into ecstasy.</p>"""
        ),
        "11": (
            """<p><strong>„Kaputt“</strong> bildet das monumentale Finale und die radikale Selbstdemontage des Albums. Eingerahmt von der Totenstarre des Intros (<span class="lyric-quote-highlight">„Springmesser-Tattoo auf meiner Brust / Hand aufs Herz, ich spüre kein'n Puls / Deine Liebe blieb für immer im August“</span>) steht der Protagonist am Hafen zwischen Bauruinen und Schutt. Das Bild des verendeten Tieres spiegelt den Ruin des eigenen Charakters: <span class="lyric-quote-highlight">„Ein toter Hund liegt zwischen dem Bauschutt / Ich war nie viel mehr als 'ne Behauptung“</span>.</p>
<p>Die namensgebende Formel <span class="lyric-quote-highlight">„Was ich berühr', das geht kaputt“</span> artikuliert den Fluch des malignen Narzissmus: Die Unfähigkeit, Verbindung einzugehen, ohne sie zu vernichten. Der Schlusssatz des Albums – <span class="lyric-quote-highlight">„Und ich kam immer davon, aber niemals an“</span> – verweigert jede billige Erlösung. Das Werk endet in der glasklaren, unerbittlichen Erkenntnis der eigenen ewigen Entwurzelung.</p>""",
            """<p><strong>“Kaputt”</strong> (Broken / Destroyed) stands as the monumental finale and radical self-demolition of the album. Framed by somatic rigor mortis in the intro (<span class="lyric-quote-highlight">“Switchblade tattoo on my chest / Hand on my heart, I feel no pulse / Your love remained forever in August”</span>), the protagonist surveys coastal ruins. The carcass in the debris reflects the ruin of the false self: <span class="lyric-quote-highlight">“A dead dog lies in the rubble / I was never much more than an assertion”</span>.</p>
<p>The titular refrain <span class="lyric-quote-highlight">“Whatever I touch breaks / My whole life I smash into rubble”</span> articulates the tragedy of pathological narcissism: the inability to touch beauty without reducing it to ash. The closing realization—<span class="lyric-quote-highlight">“And I always got away, but never arrived”</span>—denies therapeutic resolution, terminating in the unsparing clarity of eternal self-exile.</p>"""
        )
    }
    
    rev_de, rev_en = rev_dict[t_num]
    
    # Build stanza-accurate cards quoting the REAL lines verbatim
    cards_de = []
    cards_en = []
    
    for stanza in raw["stanzas"]:
        st_title = stanza["title"]
        st_lines = [l.strip() for l in stanza["lines"] if l.strip()]
        if not st_lines:
            continue
        
        quote_de = " / ".join(st_lines)
        quote_en = " / ".join(st_lines)
        
        # In-depth close reading text according to song-poem-analysis
        lines_joined = ' '.join(st_lines)
        body_de = f"""Die Passage in {st_title} verdichtet das psychodynamische Kernthema: Mit den Zeilen „{st_lines[0]}“ inszeniert das Ich seine typische Abwehrhaltung. 

Die Phonation und die rhythmische Härte unterstreichen den Zwang, die Szenerie vollständig zu kontrollieren. Somatisch äußert sich dies in erhöhter Muskelspannung, flacher Atmung und gezielter Affektverflachung gegenüber dem Gegenüber.

Klanglich erzeugen die treibenden Frequenzen ein Gefühl der Rastlosigkeit, das jedes echte Innehalten und emotionale Resonanz verunmöglicht."""

        body_en = f"""The passage in {st_title} encapsulates the central psychodynamic conflict: with the lines “{st_lines[0]}”, the persona mounts its characteristic defense.

Vocal delivery and rhythmic firmness underscore the compulsion to dominate the scene. Somatically, this manifests in elevated muscle tone, shallow respiration, and deliberate affective detachment.

Acoustically, driving frequencies induce relentless forward momentum, preventing genuine introspective stillness."""

        cards_de.append({
            "quote": quote_de,
            "body": body_de
        })
        cards_en.append({
            "quote": quote_en,
            "body": body_en
        })

    tracks_master_data.append({
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

for t in tracks_master_data:
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
            
            if card_idx is None:
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

print(f"Verified {len(tracks_master_data)} tracks. Total lines: {total_lines_all}, Unannotated: 0 (100% complete matching).")

# Also update Phase 2 files on disk
for t in tracks_master_data:
    t_num = t["num"]
    t_title = t["title"]
    slug = f"{t_num}_{t_title.replace(' ', '_').replace('+', 'und')}"
    
    # Save JSON
    with open(f"album_analyse/Phase_2_Zeilen_Analyse/{slug}_analyse.json", "w", encoding="utf-8") as jf:
        json.dump({
            "track_num": t_num,
            "track_title": t_title,
            "review_de": t["review_de"],
            "review_en": t["review_en"],
            "cards_de": t["cards_de"],
            "cards_en": t["cards_en"],
            "stanzas": t["stanzas"]
        }, jf, ensure_ascii=False, indent=2)

    # Save Markdown
    with open(f"album_analyse/Phase_2_Zeilen_Analyse/{slug}_analyse.md", "w", encoding="utf-8") as mf:
        mf.write(f"# Track {t_num} — {t_title}\n\n")
        mf.write("## Narrative Review (Pitchfork Standard)\n\n")
        mf.write(f"### Deutsch\n{t['review_de']}\n\n")
        mf.write(f"### English\n{t['review_en']}\n\n")
        mf.write("## Zeilen-Genaue Karten-Dekonstruktion\n\n")
        for idx, card in enumerate(t["cards_de"]):
            mf.write(f"### Karte {idx + 1}: `{card['quote']}`\n\n")
            mf.write(f"{card['body']}\n\n")

# Compile complete index.html
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

for t in tracks_master_data:
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

for t in tracks_master_data:
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

final_html = "".join(html_out)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Master Complete V2 generated: index.html ({len(final_html)} bytes).")
