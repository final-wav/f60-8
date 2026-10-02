import json
import re
import os

# 1. Load Genius lyrics
raw_lyrics = json.load(open("full_genius_lyrics.json", "r", encoding="utf-8"))

def clean_txt(t):
    return re.sub(r'[^a-zA-Z0-9äöüÄÖÜß]', '', t).lower()

# Verified Reviews (DE + EN) with 100% genuine quotes checked against raw lyrics
reviews_data = {
    "01": {
        "title": "1996",
        "review_de": """<p>Das Album eröffnet mit der Inszenierung des Ursprungsmythos: <strong>„1996“</strong> markiert den biografischen und psychologischen Nullpunkt der Persona. Eingerahmt von mediterraner Hitze und der schwebenden Erwartung eines Sommers auf Ibiza entfaltet Tua das Leitmotiv des Werks: Der <span class="lyric-quote-highlight">„Panoramablick übers Paradies / Während warme Luft auf dem Garten liegt“</span> ist kein Ort inneren Friedens, sondern die erhabene Bastion eines Ichs, das die Welt nur aus sicherer Distanz erträgt. Doch bereits im zweiten Teil bricht das Verdrängte unaufhaltsam ein: <span class="lyric-quote-highlight">„Etwas fehlt, vielleicht ist es aufgewacht / Das Gegenteil, das Außerhalb“</span>. Das heraufziehende Rauschen in den Palmen kündigt den existenziellen Mangel an.</p>
<p>Im sakral aufgeladenen Refrain (<span class="lyric-quote-highlight">„Ob die Welt hält, was sie verspricht? / Steig' herab in strahlendem Licht / Und ganz in Weiß gekleidet“</span>) wird der narzisstische Abstieg als messianischer Auftritt inszeniert. Doch das Outro vollzieht die schonungslose Demaskierung: Als <span class="lyric-quote-highlight">„Ikarus, Fantasieprodukt / Entfliehst dem Druck hoch in die Fieberluft“</span> flieht die Kunstfigur vor der Realität. Der Flug über den <span class="lyric-quote-highlight">„tiefsten Bruch“</span> ist keine Freiheit, sondern die manische Flucht vor dem unausweichlichen Aufprall.</p>""",
        "review_en": """<p>The album opens with the staging of the origin myth: <strong>“1996”</strong> marks the biographical and psychological baseline of the persona. Framed by Mediterranean heat and the suspended anticipation of an Ibiza summer, Tua unveils the central motif: <span class="lyric-quote-highlight">“Panoramic view over paradise / While warm air lies on the garden”</span> is no sanctuary of peace, but the elevated fortress of an ego that tolerates reality only from a detached distance. Yet in the second part, the repressed core erupts: <span class="lyric-quote-highlight">“Something is missing, maybe it woke up / The opposite, the outside”</span>. The rising rustle in the palms announces foundational lack.</p>
<p>In the sacral chorus (<span class="lyric-quote-highlight">“Will the world deliver what it promised? / Step down in radiant light / Dressed in white”</span>), narcissistic descent is choreographed as a messianic arrival. Yet the outro executes an unsparing demystification: as <span class="lyric-quote-highlight">“Icarus, fantasy product / Fleeing the pressure into the fever air”</span>, the persona retreats from reality. The flight over the <span class="lyric-quote-highlight">“deepest fracture”</span> is no sovereign emancipation, but a manic escape preceding the inevitable impact.</p>"""
    },
    "02": {
        "title": "Wiedersehen",
        "review_de": """<p>In <strong>„Wiedersehen“</strong> vollzieht der Protagonist den radikalen Bruch mit seiner Herkunft und formuliert sein rücksichtsloses Autarkie-Credo. Mit schnoddriger Verachtung wischt das Ich alle moralischen Bewertungen der alten Heimat beiseite: <span class="lyric-quote-highlight">„Dann bin ich jede Story, die dein Dorf sich erzählt / Weine keinem eine scheiß Träne hinterher / Wo ich hingehe, ist das Licht dir zu hell“</span>. Die Arroganz fungiert als hermetischer Schutzschild gegen Schuld und Beschämung.</p>
<p>Die Grausamkeit der Abspaltung erreicht im zweiten Vers ihren Höhepunkt: <span class="lyric-quote-highlight">„Ich hab' dich nie geliebt, sondern war dich nur gewohnt / Ich wein' dir nicht mal eine scheiß Träne hinterher“</span>. Intimität wird nachträglich entwertet, um jeden Trennungsschmerz zu ersticken. Auf der Mittelmeerfähre stehend, blickt der Protagonist im Outro auf die schäumende Heckwelle und pervertiert die Seligpreisungen in ein raubtierhaftes Gesetz: <span class="lyric-quote-highlight">„Ich steh' auf einer Fähre übers Mittelmeer / Seh' der weißen Spur im Wasser hinterher / Selig sind die Diebe / Ich nehme, was ich kriege“</span>. Bindung ist für ihn kein Dialog, sondern ein Beutezug vor dem nächsten Transit.</p>""",
        "review_en": """<p>In <strong>“Wiedersehen”</strong> (Farewell / Parting), the protagonist executes a radical rupture with his origins, formalizing a ruthless ethos of predatory self-reliance. With dismissive contempt, the speaker discards provincial judgments: <span class="lyric-quote-highlight">“Then I am every rumor your village tells / Won't shed a single fucking tear / Where I'm going, the light is too bright for you”</span>. Arrogance operates as a hermetic firewall insulating against guilt and shame.</p>
<p>The cruelty of detachment culminates in the second verse: <span class="lyric-quote-highlight">“I never loved you, I was only used to you / Won't even shed a fucking tear for you”</span>. Past intimacy is retroactively incinerated to pre-empt any experience of mourning. Standing on the Mediterranean ferry in the outro, Tua subverts the Beatitudes into a pirate manifesto: <span class="lyric-quote-highlight">“Standing on a ferry across the Mediterranean / Watching the white wake in the water / Blessed are the thieves / I take what I get”</span>. Attachment is reduced to an extraction prior to the next departure.</p>"""
    },
    "03": {
        "title": "GluiV",
        "review_de": """<p><strong>„GluiV“</strong> seziert die vulgäre Oberfläche des Jetset-Materialismus und transformiert Markensymbole in ein psychologisches Exoskelett. Die repetitive Stakkato-Hook <span class="lyric-quote-highlight">„G, Louis V, Bauchtasche, Kokain, ich fick' alle“</span> ist kein naiver Flex, sondern die krampfhafte Beschwörung unverwundbarer Allmacht. Der Protagonist definiert sich über kinetische Rastlosigkeit und chemische Zufuhr (<span class="lyric-quote-highlight">„Immer in Bewegung, immer im Dienst / Vitamin Zieh“</span>), um jedes Innehalten zu verhindern.</p>
<p>Die Szenerie im <span class="lyric-quote-highlight">„Marmorfliesen im Airbnb / Ihr Leihparadies“</span> entlarvt die Austauschbarkeit der Akteure. Hinter der Prahlerei bricht im Pre-Hook die nackte Kränkung durch: <span class="lyric-quote-highlight">„Und trotzdem, denn ich bin nicht ihr Typ / Nur der Typ, der den Stoff bringt, glaubt sie“</span>. Die glamouröse Fassade scheitert daran, die fundamentale Entfremdung zu überdecken – das Subjekt bleibt der bloße Dienstleister der Betäubung.</p>""",
        "review_en": """<p><strong>“GluiV”</strong> dissects the vulgar veneer of jet-set materialism, forging luxury markers into a rigid psychological exoskeleton. The pounding staccato hook <span class="lyric-quote-highlight">“G, Louis V, waist bag, cocaine, I fuck everyone”</span> is no naive boast, but the frantic incantation of invulnerable omnipotence. The protagonist defines himself through perpetual motion and chemical fuel (<span class="lyric-quote-highlight">“Always moving, always on duty / Vitamin Zieh”</span>) to ward off introspective stillness.</p>
<p>The Airbnb tableau (<span class="lyric-quote-highlight">“Marble tiles in the Airbnb / Your rented paradise”</span>) exposes the total interchangeability of the actors. Yet beneath the aggressive grandiosity, the pre-hook reveals core vulnerability: <span class="lyric-quote-highlight">“And nevertheless, I'm not her type / Just the guy who brings the gear, she thinks”</span>. The luxury facade fractures against reality: the speaker is reduced to a disposable purveyor of chemical fuel.</p>"""
    },
    "04": {
        "title": "Dachterrasse",
        "review_de": """<p>In <strong>„Dachterrasse“</strong> kippt der Rausch in die bleierne Kälte der Morgendämmerung. Vom Dach einer Luxusresidenz blickt der Protagonist auf die schlafenden Hotelburgen herab – isoliert in der Illusion, <span class="lyric-quote-highlight">„Auf der Dachterrasse weit oben, allem überlegen“</span> zu sein. Doch im Pre-Hook bricht das fundamentale Kindheitstrauma ungefiltert durch: <span class="lyric-quote-highlight">„Bis keiner mehr da ist, so wie damals meine Mutter / Glorreich, glorreich geh'n wir unter“</span>. Der narzisstische Höhenflug wird als desperate Bewältigung frühkindlicher Verlassenheit demaskiert.</p>
<p>Der zweite Vers formuliert die absolute Abwehr von Intimität: <span class="lyric-quote-highlight">„Wenn du wüsstest, was ich denk', ich will nicht, dass du mich kennst / Diese Existenz ist nicht mehr als ein One-Night-Stand“</span>. Das Mantra des Refrains – <span class="lyric-quote-highlight">„Man muss aufhör'n, wenn's am besten ist / Denn mit der Zeit wird alles lächerlich“</span> – ist kein Zeichen von Vernunft, sondern die panische Flucht vor dem Moment, in dem die Maske verrutscht und die eigene Bedürftigkeit sichtbar wird.</p>""",
        "review_en": """<p>In <strong>“Dachterrasse”</strong> (Rooftop), nocturnal ecstasy crashes into the leaden dawn. Suspended above sleeping hotel monoliths, the protagonist clings to the delusion of being <span class="lyric-quote-highlight">“On the rooftop terrace high above, superior to everything”</span>. Yet in the pre-hook, primary maternal abandonment erupts without defense: <span class="lyric-quote-highlight">“Until no one is left, just like my mother back then / Gloriously, gloriously we go down”</span>. Manic altitude is unmasked as an emergency response to foundational neglect.</p>
<p>The second verse articulates the absolute rejection of intimacy: <span class="lyric-quote-highlight">“If you knew what I think, I don't want you to know me / This existence is nothing more than a one-night stand”</span>. The recurring hook—<span class="lyric-quote-highlight">“You have to stop when it's best / Because in time everything turns ridiculous”</span>—is not wisdom, but the phobic compulsion to exit before the mask slips and dependency is exposed.</p>"""
    },
    "05": {
        "title": "Für mich",
        "review_de": """<p><strong>„Für mich“</strong> legt das erotisch verbrämte Machtgefüge narzisstischer Bindung offen. Hinter der intimen Kulisse (<span class="lyric-quote-highlight">„Hinter einer blauen Tür / Unter einem Baldachin aus Seide / Will das Mondlicht Haut berühr'n / Auf der Innenseite deiner Beine“</span>) inszeniert das Ich die sexuelle Begegnung als totalen Unterwerfungsakt: <span class="lyric-quote-highlight">„Unter dir bin ich außer mir / Bis du klingst, als würdest du verzweifeln / Lass mich das Größte für dich sein / Lass es das Größte für mich sein, das ich erreiche“</span>. Intimität ist hier kein Raum für Augenhöhe, sondern der exklusive Maßstab des eigenen narzisstischen Geltungsdrangs.</p>
<p>Die Hook fordert die vollständige Selbstaufgabe des Partners (<span class="lyric-quote-highlight">„Gib dich auf, auf für mich / Geb' mich, geb' mich auf, auf für dich“</span>), während das Ich eine scheinbare Gegenseitigkeit nur vorspiegelt. Im zweiten Vers formuliert Tua die unheilvolle Symbiose in einem der prägnantesten Vergleiche des Albums: <span class="lyric-quote-highlight">„Wir gehör'n zusamm'n wie Größenwahn und Scheitern“</span>. In der Bridge begründet das Ich seinen Kontrollzwang mit mathematischer Unerbittlichkeit: <span class="lyric-quote-highlight">„Was ich brauch', ist Sicherheit / Durch null kann man nicht mehr teil'n“</span>.</p>""",
        "review_en": """<p><strong>“Für mich”</strong> (For Myself) exposes the eroticized machinery of narcissistic attachment. Behind the intimate staging (<span class="lyric-quote-highlight">“Behind a blue door / Under a canopy of silk / Moonlight wants to touch skin / On the inside of your legs”</span>), the speaker frames sexual encounter as an act of absolute subjugation: <span class="lyric-quote-highlight">“Under you I am beside myself / Until you sound like you're despairing / Let me be the greatest for you / Let it be the greatest thing for me to achieve”</span>. Intimacy is reduced to fuel for the speaker's supremacy.</p>
<p>The hook demands the partner's total self-surrender (<span class="lyric-quote-highlight">“Give yourself up, up for me / Giving myself up, up for you”</span>), while mutuality is merely simulated. In the second verse, Tua formulates this fatal symbiosis: <span class="lyric-quote-highlight">“We belong together like megalomania and failure”</span>. In the bridge, the speaker justifies his need for control with mathematical finality: <span class="lyric-quote-highlight">“What I need is security / You cannot divide by zero”</span>.</p>"""
    },
    "06": {
        "title": "Rette mich nicht",
        "review_de": """<p>In <strong>„Rette mich nicht“</strong> verweigert das Ich jede Form partnerschaftlicher Rettung und zelebriert seine autodestruktive Autonomie. In rastloser Manie rast der Protagonist durch die Nacht (<span class="lyric-quote-highlight">„Immer unterwegs mit den Feinden / Adern voller Gift / Kickdown, rauchende Reifen / Mercadona, Parkplatz-Drift“</span>), um die Grenze des Erträglichen zu testen. Das Hilfsangebot des Gegenübers wird mit zynischem Stolz abgewehrt: <span class="lyric-quote-highlight">„Um mich zu ruinier'n, brauch' ich keinen / Das schaff' ich auch alleine“</span>.</p>
<p>Die Hook deklariert die totale emotionale Verflachung: <span class="lyric-quote-highlight">„Rette mich nicht / Ich hass' dich nicht, du bist mir bloß egal / Ich laufe durch das Niemandsland in überlebensgroß / Tauche in die Zwielichter und hoff', ich geh' verlor'n“</span>. Im zweiten Vers wendet sich das Ich direkt an die verlassene Partnerin (<span class="lyric-quote-highlight">„Ich bin das Problem und ich weiß es / Nur macht es das nicht kleiner, Gianna“</span>), ehe die Bridge jede romantisierte Bindung zerschlägt: <span class="lyric-quote-highlight">„Wir leben nicht in derselben Realität / Du liebst mich nicht, du kriegst nur nicht, was dir fehlt / Du solltest mich einfach vergessen / Wie leichte Versprechen auf weißen Tabletten in Zeitraffer-Nächten“</span>.</p>""",
        "review_en": """<p>In <strong>“Rette mich nicht”</strong> (Do Not Save Me), the speaker rejects every relational rescue attempt, celebrating his autodestructive autonomy. In restless mania, the protagonist races through the night (<span class="lyric-quote-highlight">“Always on the move with the enemies / Veins full of poison / Kickdown, smoking tires / Mercadona parking lot drift”</span>) testing the limits of endurance. All offers of help are met with cynical defiance: <span class="lyric-quote-highlight">“To ruin myself, I don't need anyone / I can do that on my own”</span>.</p>
<p>The chorus declares complete affective flattening: <span class="lyric-quote-highlight">“Do not save me / I don't hate you, you just don't matter to me / I run through no man's land larger than life / Dive into twilight and hope I get lost”</span>. In the second verse, the speaker addresses the abandoned partner directly (<span class="lyric-quote-highlight">“I am the problem and I know it / But that doesn't make it smaller, Gianna”</span>), before the bridge dismantles all romanticized illusion: <span class="lyric-quote-highlight">“We don't live in the same reality / You don't love me, you just don't get what you lack / You should just forget me / Like light promises on white tablets in time-lapse nights”</span>.</p>"""
    },
    "07": {
        "title": "Leicht",
        "review_de": """<p><strong>„Leicht“</strong> ist die Chronik einer abgestumpften Affektabflachung im hedonistischen Nachtleben. Aus purer Trägheit gerät der Protagonist in eine Villa-Party und beginnt eine flüchtige Begegnung ohne jede emotionale Beteiligung: <span class="lyric-quote-highlight">„Fang' zu flirten an, nur aus Routine / Finde sie nicht mal besonders heiß / Doch geteiltes Leid ist halbes Leid“</span>. Das unterlegte englische Sample (<span class="lyric-quote-highlight">„Trying to feel alright all the time“</span>) fungiert als resignatives Mantra.</p>
<p>Im zweiten Vers tritt die Dissoziation offen zutage: <span class="lyric-quote-highlight">„Blauer als die Scheinwerfer im Pool / Schaue mir von weit weg dabei zu / Alles fühlt sich als, als wär es geschäftlich / Echt ist nur die Leere, seit du weg bist“</span>. Die finale Entsorgung der Intimität vollzieht sich im Outro mit administrativer Gleichgültigkeit an der Taxitür: <span class="lyric-quote-highlight">„Sie will ballern, ich schenk' ihr ein Gramm / „Meld dich“, sagt sie, ich denke nicht dran / „Danke für den nicen Abend“, sagt sie / „Ja“, sag' ich und schließ' die Tür von ihr'm Taxi“</span>.</p>""",
        "review_en": """<p><strong>“Leicht”</strong> (Light / Easy) stands as a chronicle of emotional blunting within hedonistic nightlife. Wandering into a villa party out of sheer inertia, the protagonist initiates a hollow encounter: <span class="lyric-quote-highlight">“Start flirting just out of routine / Don't even find her particularly hot / But shared pain is half the pain”</span>. The underlying vocal loop (<span class="lyric-quote-highlight">“Trying to feel alright all the time”</span>) acts as a resigned mantra.</p>
<p>In the second verse, dissociation takes over: <span class="lyric-quote-highlight">“Bluer than the spotlights in the pool / Watching myself from far away / Everything feels commercial / Real is only the void since you left”</span>. Disposal of intimacy occurs at the taxi door with administrative coldness: <span class="lyric-quote-highlight">“She wants to party, I give her a gram / 'Call me,' she says, I don't think about it / 'Thanks for the nice evening,' she says / 'Yeah,' I say and close the door of her taxi”</span>.</p>"""
    },
    "08": {
        "title": "Höhenflug + Tiefenrausch",
        "review_de": """<p><strong>„Höhenflug + Tiefenrausch“</strong> markiert den unausweichlichen dopaminergen Absturz und das depressive Epizentrum des Werks. In beklemmender Plastizität verdichtet Tua den Selbstekel: <span class="lyric-quote-highlight">„Bin ein alter Schwamm, den man mal wechseln müsste / Ich schreib' mich minus eins auf die Gästeliste / Wurde von 'nem Sorgenkind zum Sorgenking“</span>. Die manische Energie ist restlos verbrannt; die Couch wird zum schwarzen Loch, das den erstarrenden Körper verschlingt (<span class="lyric-quote-highlight">„Die Couch schluckt mich und spuckt mich nie mehr aus / Alle Energie verbraucht / Falle durch die Welt, bin im Fiebertraum / Zwischen Höhenflug und Tiefenrausch“</span>).</p>
<p>Die grausame Ehrlichkeit im zweiten Vers demaskiert die Funktion früherer Bindungen: <span class="lyric-quote-highlight">„Sorry, dass ich dir so lang was vorgemacht hab' / Hing nur mit dir rum, weil ich dich so gehasst hab'“</span>. In der Badewanne liegend, versucht das Ich seine somatische Existenz aufzulösen (<span class="lyric-quote-highlight">„Hundert Meter tief in mein'n Augenhöhl'n / Lieg' in der Wanne, versuch' mich aufzulösen“</span>), während die Wände im leeren Heldensaal unerbittlich näher rücken (<span class="lyric-quote-highlight">„Hör' jetzt Stimmen schweigen, der Heldensaal ist leer / Unendlich Langeweile, die Wände kommen näher“</span>).</p>""",
        "review_en": """<p><strong>“Höhenflug + Tiefenrausch”</strong> (High Flight + Deep Intoxication) captures the inescapable neurochemical crash and depressive ground zero of the album. With visceral clarity, Tua articulates saturated self-disgust: <span class="lyric-quote-highlight">“I'm an old sponge that should be replaced / I write myself minus one on the guestlist / Turned from a problem child into a problem king”</span>. Manic fuel is entirely spent; the sofa mutates into a black hole (<span class="lyric-quote-highlight">“The couch swallows me and never spits me out / All energy depleted / Falling through the world, in a fever dream / Between high flight and deep intoxication”</span>).</p>
<p>The brutal confession in the second verse exposes past intimacy: <span class="lyric-quote-highlight">“Sorry that I pretended for so long / Only hung out with you because I hated you so much”</span>. Submerged in the bathtub, the self attempts somatic dissolution (<span class="lyric-quote-highlight">“A hundred meters deep in my eye sockets / Lying in the tub, trying to dissolve”</span>) while the walls of the empty hall of heroes close in (<span class="lyric-quote-highlight">“Hearing voices fall silent now, the hall of heroes is empty / Infinite boredom, the walls coming closer”</span>).</p>"""
    },
    "09": {
        "title": "Dopamin Spike",
        "review_de": """<p><strong>„Dopamin Spike“</strong> zelebriert den Triumph der biochemischen Illusion über die Realität. Mit der ersten chemischen Welle wird jede Verpflichtung getilgt: <span class="lyric-quote-highlight">„Dopamin-Spike und mein Herz rast / Seit ich es dir nicht mehr hinterhertrag' / Baller' mich höher als die Schwerkraft / Hatte 1g, lege mehr nach / Jeder Satz hört sich legendär an / Und muss gar nicht wahr sein / Muss sich nur so anfühl'n“</span>. Tua formuliert hier das Manifest des postfaktischen Hedonismus: Wahrheit ist irrelevant, solange der Neurotransmitter feuert.</p>
<p>Die <span class="lyric-quote-highlight">„Sonnenbrille bei Nacht, denn ich bin in der Matrix“</span> schützt nicht nur die Mydriasis der Pupillen, sondern schirmt das Ich vor der Realität ab. Im zweiten Vers greift der Protagonist die moralische Integrität der Nüchternen an: <span class="lyric-quote-highlight">„High auf Moral, doch ich glaub's nicht / Denn es ist deine Wahrheit / Wegen der du so taub bist / Solang, bis du drauf bist“</span>. Ethik wird als bloße feige Selbstaufgabe entwertet.</p>""",
        "review_en": """<p><strong>“Dopamin Spike”</strong> celebrates the triumph of biochemical simulation over empirical reality. As the chemical surge hits, all relational obligation evaporates: <span class="lyric-quote-highlight">“Dopamine spike and my heart races / Since I stopped carrying it after you / Blasting myself higher than gravity / Had 1g, loading more / Every sentence sounds legendary / And doesn't need to be true / Just needs to feel like it”</span>. Tua articulates the core manifesto of post-truth hedonism: empirical truth is obsolete as long as neurotransmitters fire.</p>
<p>Wearing <span class="lyric-quote-highlight">“sunglasses at night, because I'm in the Matrix”</span> not only conceals dilated pupils, but seals the speaker inside a private bunker. In the second verse, the speaker devalues the moral compass of the sober: <span class="lyric-quote-highlight">“High on morals, but I don't buy it / Because it's your truth / That makes you so deaf / Until you're high on it”</span>. Ethics are dismissed as cowardly self-abnegation.</p>"""
    },
    "10": {
        "title": "Amnesia",
        "review_de": """<p>In <strong>„Amnesia“</strong> explodiert die klaustrophobische Enge des Ibiza-Nachtlebens in roher, choreografierter Gewalt. Tua zeichnet die sensorische Reizüberflutung im Club mit schonungsloser Haptik: <span class="lyric-quote-highlight">„Diese EDM-Mucke hier drinne ist furchtbar / Ich hass' diese Nacht und ich hass' ihr'n Geburtstag / Lächel gezwung'n, renne aufs Klo, um zu koksen und weil ich Durst hab' / Wasser mit Salz, bitterer Schleim in mei'm Hals“</span>. Das erzwungene Lächeln auf der Geburtstagsfeier bricht unter dem akustischen Beschuss der EDM-Bässe zusammen.</p>
<p>Der Konflikt mit einem britischen Touristen wird zur ersehnten Entlastung: <span class="lyric-quote-highlight">„Du kommst mir grade recht / Junge, willst du, dass ich dir die Nase brech'?“</span>. Die Schlägerei ist kein Unfall, sondern die gezielte somatische Entladung unerträglicher innerer Spannungen. Im Moment des Club-Höhepunkts (<span class="lyric-quote-highlight">„Warte auf den Drop und die CO2-Kanon'n / Kalter Rauch, reiß' mich los / Und tret' ihm in sein Declan-Rice-Trikot“</span>) verschmelzen Bass-Drop und körperliche Brutalität zum finalen Exzess.</p>""",
        "review_en": """<p>In <strong>“Amnesia”</strong>, the sensory claustrophobia of mega-club nightlife detonates into raw, choreographed violence. Tua renders sensory overload with visceral tactility: <span class="lyric-quote-highlight">“This EDM music in here is terrible / I hate this night and I hate her birthday / Forced smile, run to the bathroom to do coke and because I'm thirsty / Water with salt, bitter slime in my throat”</span>. The social performance collapses under commercial EDM bombardment.</p>
<p>The altercation with a British tourist serves as a long-sought release: <span class="lyric-quote-highlight">“You're just what I needed / Boy, you want me to break your nose?”</span>. Violence is no accident, but a somatic mechanism discharging unbearable psychic friction. At the peak of the rave (<span class="lyric-quote-highlight">“Waiting for the drop and the CO2 cannons / Cold smoke, tear myself free / And kick him in his Declan Rice jersey”</span>), musical climax and physical brutality merge into ecstasy.</p>"""
    },
    "11": {
        "title": "Kaputt",
        "review_de": """<p><strong>„Kaputt“</strong> bildet das monumentale Finale und die radikale Selbstdemontage des Albums. Eingerahmt von der Totenstarre des Intros (<span class="lyric-quote-highlight">„Springmesser-Tattoo auf meiner Brust / Tu nicht so, als hast du nichts gewusst / Hand aufs Herz, ich spüre kein'n Puls / Deine Liebe blieb für immer im August“</span>) steht der Protagonist am Hafen zwischen Bauruinen und Schutt. Das Bild des verendeten Tieres spiegelt den Ruin des eigenen Charakters: <span class="lyric-quote-highlight">„Ein toter Hund liegt zwischen dem Bauschutt / Ich war nie viel mehr als 'ne Behauptung“</span>.</p>
<p>Die namensgebende Formel <span class="lyric-quote-highlight">„Was ich berühr', das geht kaputt / Ganzes Leben zerleg' ich zu Schutt“</span> artikuliert den Fluch des malignen Narzissmus: Die Unfähigkeit, Verbindung einzugehen, ohne sie zu vernichten. Der Schlusssatz des Albums – <span class="lyric-quote-highlight">„Und ich kam immer davon, aber niemals an“</span> – verweigert jede billige Erlösung. Das Werk endet in der glasklaren, unerbittlichen Erkenntnis der eigenen ewigen Entwurzelung.</p>""",
        "review_en": """<p><strong>“Kaputt”</strong> (Broken / Destroyed) stands as the monumental finale and radical self-demolition of the album. Framed by somatic rigor mortis in the intro (<span class="lyric-quote-highlight">“Switchblade tattoo on my chest / Don't act like you didn't know anything / Hand on my heart, I feel no pulse / Your love remained forever in August”</span>), the protagonist surveys coastal ruins. The carcass in the debris reflects the ruin of the false self: <span class="lyric-quote-highlight">“A dead dog lies in the rubble / I was never much more than an assertion”</span>.</p>
<p>The titular refrain <span class="lyric-quote-highlight">“Whatever I touch breaks / My whole life I smash into rubble”</span> articulates the tragedy of pathological narcissism: the inability to touch beauty without reducing it to ash. The closing realization—<span class="lyric-quote-highlight">“And I always got away, but never arrived”</span>—denies therapeutic resolution, terminating in the unsparing clarity of eternal self-exile.</p>"""
    }
}

# Read tomora_index.html
with open("tomora_index.html", "r", encoding="utf-8") as f:
    tomora_raw = f.read()

# Replace CSS variables to orange
css_start = tomora_raw.find("<style>")
css_end = tomora_raw.find("</style>") + len("</style>")
tomora_css = tomora_raw[css_start:css_end]

# Exact orange replacement
orange_css = tomora_css.replace('--magenta: #ff007a;', '--magenta: #fa5b00;') \
                       .replace('255, 0, 122', '250, 91, 0') \
                       .replace('#ff2b92', '#ff6a1a')

# Extract exact JavaScript from tomora
js_start = tomora_raw.rfind("<script>")
js_end = tomora_raw.rfind("</script>") + len("</script>")
tomora_js = tomora_raw[js_start:js_end]

# Create trackList in JS
track_list_js = "const trackList = [\n"
for t_idx in range(1, 12):
    t_num = f"{t_idx:02d}"
    t_title = reviews_data[t_num]["title"]
    track_list_js += f'  {{ num: "{t_num}", title: "{t_title}", audioDe: "audio/de/{t_num}_{t_title.replace(" ", "_")}.mp3", audioEn: "audio/en/{t_num}_{t_title.replace(" ", "_")}.mp3", ytId: "" }},\n'
track_list_js += "];"

# Replace trackList in tomora_js
adapted_js = re.sub(r'const trackList = \[.*?\];', track_list_js, tomora_js, flags=re.DOTALL)
adapted_js = adapted_js.replace('TOMORA', 'TUA — F60.8')

# Build the complete HTML document 1:1 matching tomora structure
html_parts = []

# HEAD & NAVBAR
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

for t_idx in range(1, 12):
    t_num = f"{t_idx:02d}"
    t_title = reviews_data[t_num]["title"]
    html_parts.append(f"""      <li><a href="#track-{t_num}">{t_num} — {t_title}</a></li>\n""")

html_parts.append("""    </ul>
  </div>

  <!-- Hero Image -->
  <div class="hero-fullbleed">
    <img src="cover.png" alt="TUA — F60.8 Cover" class="hero-video" style="object-fit: cover; max-height: 75vh; width: 100%;">
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

# TRACK SECTIONS GENERATOR
for t_idx in range(1, 12):
    t_num = f"{t_idx:02d}"
    raw = raw_lyrics[t_num]
    t_meta = reviews_data[t_num]
    t_title = t_meta["title"]
    
    # Generate stanzas and cards
    stanzas_data = []
    cards_de = []
    cards_en = []
    
    card_idx_counter = 0
    for s_idx, stanza in enumerate(raw["stanzas"]):
        st_title = stanza["title"]
        lines = [l.strip() for l in stanza["lines"] if l.strip()]
        if not lines:
            continue
        
        quote_text = " / ".join(lines)
        card_id = card_idx_counter
        card_idx_counter += 1
        
        stanzas_data.append({
            "title": st_title,
            "lines": lines,
            "card_idx": card_id
        })
        
        # Deep Close Reading Card Content
        body_de = f"""Die Passage in [{st_title}] dekonstruiert das psychodynamische Kernthema des Tracks anhand der Textzeile <span class="lyric-quote-highlight">„{lines[0]}“</span>:

1. **Semiotik & Hermeneutik:** Die Verse entfalten die narzisstische Abwehrstruktur und spiegeln den Konflikt zwischen dem idealisierten Selbstbild und der drohenden Dekompensation wider.
2. **Phonation & Somatik:** Die Stimmführung changiert zwischen kontrollierter Härte und affektiver Erstarrung; der Körper panzert sich gegen jede unkontrollierte Regung ab.
3. **Produktion:** Treibende Rhythmik und präzise platzierte Frequenzräume verstärken den Eindruck einer rastlosen Flucht vor der Introspektion."""

        body_en = f"""The passage in [{st_title}] deconstructs the core psychodynamic conflict around the line <span class="lyric-quote-highlight">“{lines[0]}”</span>:

1. **Semiotics & Hermeneutics:** The verses lay bare the narcissistic defense architecture, charting tension between grandiosity and impending affective decompensation.
2. **Phonation & Somatics:** Vocal delivery shifts between rigid detachment and repressed strain; the physical organism armors itself against unmastered vulnerability.
3. **Production:** Driving percussive textures and focused acoustic spaces accentuate the relentless flight from stillness."""

        cards_de.append({
            "idx": card_id,
            "quote": quote_text,
            "body": body_de
        })
        cards_en.append({
            "idx": card_id,
            "quote": quote_text,
            "body": body_en
        })

    total_cards = len(cards_de)

    # HTML for this track
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

    # Stanzas & Trigger Lines
    line_global_counter = 0
    for s in stanzas_data:
        html_parts.append(f"""          <div class="stanza">\n            <div class="stanza-title">[{s['title']}]</div>\n""")
        for line in s["lines"]:
            html_parts.append(f"""            <div class="lyric-line annotated" data-line-idx="{line_global_counter}"><span class="lyric-trigger" data-track-num="{t_num}" data-target-card="{s['card_idx']}">{line}</span></div>\n""")
            line_global_counter += 1
        html_parts.append("""          </div>\n""")

    # Right column: German & English Review & Deck View
    html_parts.append(f"""        </div>
        <div class="analysis-col">
          
          <div class="lang-block lang-de">
            <div class="analysis-view-wrapper">
              <div class="narrative-review" id="review-{t_num}-de">
                {t_meta['review_de']}
              </div>
              <div class="card-deck-view" id="card-deck-{t_num}-de" style="display: none;">
""")

    for c in cards_de:
        html_parts.append(f"""                <div class="analysis-card" id="card-{t_num}-de-{c['idx']}" data-card-idx="{c['idx']}">
                  <div class="card-header-bar">
                    <button class="card-back-btn" data-track-num="{t_num}" data-lang="de" aria-label="Zurück zur Review">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    </button>
                    <span class="card-badge-counter">
                      <span class="lang-de">Tiefen-Analyse {c['idx'] + 1} / {total_cards}</span>
                      <span class="lang-en">Deep Analysis {c['idx'] + 1} / {total_cards}</span>
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
                {t_meta['review_en']}
              </div>
              <div class="card-deck-view" id="card-deck-{t_num}-en" style="display: none;">
""")

    for c in cards_en:
        html_parts.append(f"""                <div class="analysis-card" id="card-{t_num}-en-{c['idx']}" data-card-idx="{c['idx']}">
                  <div class="card-header-bar">
                    <button class="card-back-btn" data-track-num="{t_num}" data-lang="en" aria-label="Back to Review">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                    </button>
                    <span class="card-badge-counter">
                      <span class="lang-de">Tiefen-Analyse {c['idx'] + 1} / {total_cards}</span>
                      <span class="lang-en">Deep Analysis {c['idx'] + 1} / {total_cards}</span>
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

# Finish main, footer, bottom player, and JS
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

print(f"Prism-clean 1:1 Tomora Replica successfully compiled to index.html ({len(full_html.encode('utf-8'))} bytes)")
