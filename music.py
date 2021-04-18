from ytmusicapi import YTMusic
from pprint import pprint
import webbrowser
def play_music(text):
    ytmusic = YTMusic()
    songs = ytmusic.search(f'{text}')
    # pprint(songs)
    title =songs[0]['videoId']
    webbrowser.open_new_tab(f'https://music.youtube.com/watch?v={title}')

