# youtube_player.py
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
import vlc
import time

def get_best_stream_url(youtube_url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return info['url'], info.get('title', 'Unknown Title')

def play_youtube(query):
    search = VideosSearch(query, limit=1).result()
    if not search['result']:
        print("No results.")
        return
    
    video_info = search['result'][0]
    url = video_info['link']
    title = video_info['title']

    stream_url, actual_title = get_best_stream_url(url)
    print(f"Playing: {title}")

    player = vlc.MediaPlayer(stream_url)
    player.play()

    # Wait for playback to start
    time.sleep(1)

    # Keep running while playing
    while True:
        state = player.get_state()
        # End playback if video finished or error occurred
        if state in [vlc.State.Ended, vlc.State.Error]:
            break
        time.sleep(1)

    player.stop()
