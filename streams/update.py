import requests

USERNAME = "kennyhoopz"

def get_m3u8():
    try:
        url = f"https://kick.com/api/v2/channels/{USERNAME}"
        r = requests.get(url).json()

        playback = r.get("playback_url")

        return playback
    except:
        return None

stream = get_m3u8()

if stream:
    content = f"""#EXTM3U
#EXTINF:-1,Kenny Hoopz (Kick)
{stream}
"""
else:
    content = """#EXTM3U
#EXTINF:-1,OFFLINE
"""

with open("streams/live.m3u8", "w") as f:
    f.write(content)
