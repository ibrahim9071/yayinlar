import requests

USERNAME = "kennyhoopz"

def get_stream():
    try:
        url = f"https://kick.com/api/v2/channels/{USERNAME}"
        r = requests.get(url).json()

        if r.get("livestream"):
            return r["livestream"]["playback_url"]
        return None
    except:
        return None

stream = get_stream()

if stream:
    content = f"""#EXTM3U
#EXTINF:-1,Kick Live
{stream}
"""
else:
    content = "#EXTM3U\n#EXTINF:-1,OFFLINE\n"

with open("streams/live.m3u8", "w") as f:
    f.write(content)
