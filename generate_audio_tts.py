import asyncio
import edge_tts
import json
import os
import re
from bs4 import BeautifulSoup
from build_genuine_tomora import tracks_data

# Create audio directories
os.makedirs("audio/de", exist_ok=True)
os.makedirs("audio/en", exist_ok=True)

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

def clean_html_for_tts(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    text = soup.get_text(separator=" ")
    text = re.sub(r'\s+', ' ', text).strip()
    return text

async def generate_track_audio(t_num, t_title, text_de, text_en):
    slug = f"{t_num}_{t_title.replace(' ', '_').replace('+', 'und')}"
    out_de = f"audio/de/{slug}.mp3"
    out_en = f"audio/en/{slug}.mp3"
    
    # Generate DE audio
    print(f"[{t_num}] Generating DE TTS -> {out_de}...")
    communicate_de = edge_tts.Communicate(text_de, "de-DE-ConradNeural", rate="+3%", pitch="-1Hz")
    await communicate_de.save(out_de)
    
    # Generate EN audio
    print(f"[{t_num}] Generating EN TTS -> {out_en}...")
    communicate_en = edge_tts.Communicate(text_en, "en-US-ChristopherNeural", rate="+2%", pitch="-1Hz")
    await communicate_en.save(out_en)
    
    print(f"[{t_num}] OK ({os.path.getsize(out_de)} bytes DE, {os.path.getsize(out_en)} bytes EN)")

async def main():
    print("Starting Neural TTS Audio Essay Generation for all 11 Tracks...")
    for t in tracks_data:
        t_num = t["num"]
        t_title = t["title"]
        text_de = clean_html_for_tts(t["review_de"])
        text_en = clean_html_for_tts(t["review_en"])
        await generate_track_audio(t_num, t_title, text_de, text_en)
    print("\n>>> ALL 22 AUDIO ESSAYS SUCCESSFULLY GENERATED! <<<")

if __name__ == "__main__":
    asyncio.run(main())
