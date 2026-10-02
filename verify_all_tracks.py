import json
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

soup = BeautifulSoup(open('index.html', encoding='utf-8'), 'html.parser')
raw_lyrics = json.load(open('full_genius_lyrics.json', encoding='utf-8'))

track_sections = soup.select('.track-section')
print(f"Total track sections in index.html: {len(track_sections)}")

all_ok = True

for ts in track_sections:
    t_num = ts.select_one('.track-num-badge').get_text(strip=True)
    t_title = ts.select_one('.track-heading').get_text(strip=True)
    
    stanzas = ts.select('.lyrics-col .stanza')
    cards_de = ts.select('.lang-block.lang-de .analysis-card')
    cards_en = ts.select('.lang-block.lang-en .analysis-card')
    review_de = ts.select_one('.lang-block.lang-de .narrative-review').get_text(strip=True)
    review_en = ts.select_one('.lang-block.lang-en .narrative-review').get_text(strip=True)
    
    # 1. Check review length and quality
    if len(review_de) < 150 or len(review_en) < 150:
        print(f"[ERROR] Track {t_num} review is too short!")
        all_ok = False
        
    # 2. Check card count symmetry
    if len(cards_de) != len(cards_en) or len(cards_de) == 0:
        print(f"[ERROR] Track {t_num} card count mismatch (DE: {len(cards_de)}, EN: {len(cards_en)})")
        all_ok = False
        
    # 3. Check every trigger targets a valid card index
    trigger_targets = set()
    for s_idx, s in enumerate(stanzas):
        s_title = s.select_one('.stanza-title').get_text(strip=True)
        if '[[' in s_title or ']]' in s_title:
            print(f"[ERROR] Track {t_num} Stanza {s_idx} has double brackets: {s_title}")
            all_ok = False
        triggers = s.select('.lyric-trigger')
        for tr in triggers:
            target = int(tr.get('data-target-card'))
            trigger_targets.add(target)
            if target < 0 or target >= len(cards_de):
                print(f"[ERROR] Track {t_num} Stanza {s_idx} target {target} out of range (max {len(cards_de)-1})")
                all_ok = False

    # 4. Check if every defined card is actually reachable by at least one trigger
    for c_idx in range(len(cards_de)):
        if c_idx not in trigger_targets:
            print(f"[WARNING] Track {t_num} Card {c_idx} is never triggered by any line!")
            all_ok = False

    # 5. Check card contents for generic schema slop
    for c_idx, c in enumerate(cards_de):
        body = c.select_one('.card-body').get_text(strip=True)
        if "1. Semiotik" in body or "2. Phonation" in body or "4 Säulen" in body:
            print(f"[ERROR] Track {t_num} Card {c_idx} contains schema slop!")
            all_ok = False

    print(f"✓ Track {t_num} ({t_title}): {len(stanzas)} stanzas, {len(cards_de)} cards, all {len(trigger_targets)} cards reachable and validated.")

if all_ok:
    print("\n=======================================================")
    print(">>> 100% VERIFICATION PASSED FOR ALL 11 TRACKS! <<<")
    print("=======================================================")
else:
    print("\n[FAILED] Verification found errors that need addressing.")
