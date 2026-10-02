import urllib.request
import re
import json

url = "https://www.youtube.com/playlist?list=OLAK5uy_npgXAUNP4CJqSCklXMGCOBd3PUn97POEs"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
html = urllib.request.urlopen(req).read().decode("utf-8")

data_match = re.search(r'var ytInitialData = ({.*?});</script>', html)
if not data_match:
    data_match = re.search(r'window\["ytInitialData"\] = ({.*?});</script>', html)

if data_match:
    data_str = data_match.group(1)
    data = json.loads(data_str)
    
    # Traverse data to find playlist video renderers
    videos = []
    
    def find_videos(obj):
        if isinstance(obj, dict):
            if "playlistVideoRenderer" in obj:
                r = obj["playlistVideoRenderer"]
                vid = r.get("videoId")
                title = r.get("title", {}).get("runs", [{}])[0].get("text", "")
                if vid:
                    videos.append({"id": vid, "title": title})
            for k, v in obj.items():
                find_videos(v)
        elif isinstance(obj, list):
            for item in obj:
                find_videos(item)

    find_videos(data)
    print(f"Found {len(videos)} playlist videos:")
    for idx, v in enumerate(videos):
        print(f"{idx+1:02d}: {v['id']} - {v['title']}")
        
    with open("yt_playlist_tracks.json", "w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)
else:
    print("ytInitialData not found")
