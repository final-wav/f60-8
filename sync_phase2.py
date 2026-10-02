import json
from build_genuine_tomora import tracks_data

for t in tracks_data:
    t_num = t['num']
    t_title = t['title']
    slug = f"{t_num}_{t_title.replace(' ', '_').replace('+', 'und')}"
    
    with open(f"album_analyse/Phase_2_Zeilen_Analyse/{slug}_analyse.md", "w", encoding="utf-8") as mf:
        mf.write(f"# Track {t_num} — {t_title}\n\n")
        mf.write("## Narrative Review (Pitchfork Standard)\n\n")
        mf.write(f"### Deutsch\n{t['review_de']}\n\n")
        mf.write(f"### English\n{t['review_en']}\n\n")
        mf.write("## Zeilen-Genaue Karten-Dekonstruktion (Tomora Standard)\n\n")
        for idx, card in enumerate(t['cards_de']):
            mf.write(f"### Karte {idx + 1}: `{card['quote']}`\n\n")
            mf.write(f"**Deutsch:**\n{card['body']}\n\n")
            mf.write(f"**English:**\n{t['cards_en'][idx]['body']}\n\n---\n\n")
            
    with open(f"album_analyse/Phase_2_Zeilen_Analyse/{slug}_analyse.json", "w", encoding="utf-8") as jf:
        json.dump(t, jf, ensure_ascii=False, indent=2)

print("Phase 2 files successfully synced with genuine literary prose!")
