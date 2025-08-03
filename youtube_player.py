# youtube_player.py
from youtubesearchpython import VideosSearch
import pafy
import vlc

pafy.set_backend("yt-dlp")

def play_youtube(query):
    search = VideosSearch(query, limit=1).result()
    if not search['result']:
        print("No results.")
        return
    url = search['result'][0]['link']
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    player = vlc.MediaPlayer(playurl)
    player.play()

    print(f"Playing: {search['result'][0]['title']}")
