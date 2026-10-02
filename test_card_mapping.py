import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Explicit semantic card mapping for every track and stanza
# Format: t_num -> list of card_indices for each stanza in order, or a function (s_idx, line_idx, line_text) -> card_idx

stanza_mappings = {
    "01": [0, 1, 2, 3], # [Part 1] -> 0, [Part 2] -> 1, [Hook] -> 2, [Outro] -> 3
    "02": [0, 1, 2, 1, 3, 4], # [Part 1] -> 0, [Hook] -> 1, [Part 2] -> 2, [Hook] -> 1, [Bridge] -> 3, [Outro] -> 4
    "03": [0, 1, 2, 3, 1, 4, 3, 1], # [Intro] -> 0, [Hook] -> 1, [Part 1] -> 2, [Pre-Hook] -> 3, [Hook] -> 1, [Part 2] -> 4, [Pre-Hook] -> 3, [Hook] -> 1
    "04": "custom_04", # Part 1 has 2 cards, Part 2 has 2 cards
    "05": [1, 0, 1, 1, 2, 1, 3, 1, 1], # [Intro]->1, [Part 1]->0, [Hook]->1, [Post-Hook]->1, [Part 2]->2, [Hook]->1, [Bridge]->3, [Hook]->1, [Outro]->1
    "06": [0, 0, 0, 0, 1, 0, 2, 0, 0, 3], # [Intro]->0, [Part 1]->0, [Hook]->0, [Post-Hook]->0, [Part 2]->1, [Hook]->0, [Bridge]->2, [Hook]->0, [Post-Hook]->0, [Outro]->3
    "07": [1, 0, 1, 2, 1, 1, 3], # [Intro]->1, [Part 1]->0, [Hook]->1, [Part 2]->2, [Hook]->1, [Bridge]->1, [Outro]->3
    "08": [0, 0, 1, 1, 2, 1, 1, 3, 1], # [Intro]->0, [Part 1]->0, [Pre-Hook]->1, [Hook]->1, [Part 2]->2, [Pre-Hook]->1, [Hook]->1, [Bridge]->3, [Outro]->1
    "09": [1, 0, 1, 1, 2, 1, 1], # [Intro]->1, [Part 1]->0, [Hook]->1, [Interlude]->1, [Part 2]->2, [Hook]->1, [Outro]->1
    "10": [0, 0, 1, 2, 1], # [Intro]->0, [Part 1]->0, [Hook]->1, [Part 2]->2, [Hook]->1
    "11": [0, 1, 2, 1, 3, 0], # [Intro]->0, [Hook]->1, [Part]->2, [Hook]->1, [Bridge]->3, [Outro]->0
}

def get_card_idx_for_line(t_num, s_idx, l_idx, line_text, total_cards):
    if t_num == "04":
        # Stanza 0: Part 1 (4 lines: lines 0,1 -> Card 0; lines 2,3 -> Card 1)
        if s_idx == 0:
            return 0 if l_idx < 2 else 1
        # Stanza 1: Pre-Hook -> Card 2
        elif s_idx == 1:
            return 2
        # Stanza 2: Hook -> Card 2
        elif s_idx == 2:
            return 2
        # Stanza 3: Part 2 (4 lines: lines 0,1 -> Card 3; lines 2,3 -> Card 4)
        elif s_idx == 3:
            return 3 if l_idx < 2 else 4
        # Stanza 4: Pre-Hook -> Card 2
        elif s_idx == 4:
            return 2
        # Stanza 5: Hook -> Card 2
        elif s_idx == 5:
            return 2
        # Stanza 6: Outro -> Card 2
        elif s_idx == 6:
            return 2
        return 0
    
    mapping = stanza_mappings.get(t_num)
    if isinstance(mapping, list) and s_idx < len(mapping):
        return min(mapping[s_idx], total_cards - 1)
    return min(s_idx, total_cards - 1)

raw_lyrics = json.load(open("full_genius_lyrics.json", encoding="utf-8"))

for t_num, mapping in stanza_mappings.items():
    stanzas = raw_lyrics[t_num]["stanzas"]
    print(f"\n--- TRACK {t_num} ({len(stanzas)} stanzas) ---")
    for s_idx, s in enumerate(stanzas):
        title = s["title"]
        lines = [l.strip() for l in s["lines"] if l.strip()]
        for l_idx, line in enumerate(lines):
            card_idx = get_card_idx_for_line(t_num, s_idx, l_idx, line, 10)
            print(f"  Stanza {s_idx} ({title}) Line {l_idx}: '{line[:35]}' -> Card {card_idx}")
            if l_idx >= 1 and len(lines) > 2:
                # Just show first and last
                if l_idx == 1:
                    print("    ...")
                if l_idx < len(lines) - 1:
                    continue
