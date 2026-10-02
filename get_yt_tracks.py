import subprocess
import json

cmd = ['python', '-m', 'yt_dlp', '--flat-playlist', '-j', 'https://youtube.com/playlist?list=OLAK5uy_npgXAUNP4CJqSCklXMGCOBd3PUn97POEs']
output = subprocess.check_output(cmd).decode('utf-8')

tracks = []
for line in output.strip().split('\n'):
    if line.strip():
        data = json.loads(line)
        tracks.append({'id': data['id'], 'title': data['title']})

print(f"Total tracks extracted: {len(tracks)}")
for idx, t in enumerate(tracks):
    print(f"{idx+1:02d}: {t['id']} -> {t['title']}")

with open('yt_official_tracks.json', 'w', encoding='utf-8') as f:
    json.dump(tracks, f, ensure_ascii=False, indent=2)
