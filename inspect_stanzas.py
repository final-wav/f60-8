import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

import build_genuine_tomora

tracks_data = build_genuine_tomora.tracks_data
raw_lyrics = json.load(open('full_genius_lyrics.json', encoding='utf-8'))

for t in tracks_data:
    t_num = t['num']
    t_title = t['title']
    raw = raw_lyrics[t_num]
    cards = t['cards_de']
    
    print(f"\n==================== TRACK {t_num}: {t_title} ({len(cards)} CARDS) ====================")
    print("CARDS:")
    for c_idx, c in enumerate(cards):
        print(f"  [Card {c_idx}]: {c['quote']}")
    
    print("STANZAS:")
    for s_idx, s in enumerate(raw['stanzas']):
        title = s['title']
        lines = [l.strip() for l in s['lines'] if l.strip()]
        first_line = lines[0] if lines else ""
        print(f"  [Stanza {s_idx}]: {title} (First line: \"{first_line[:50]}\")")
