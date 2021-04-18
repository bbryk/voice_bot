from ytmusicapi import YTMusic
from pprint import pprint
import webbrowser

ytmusic = YTMusic()
songs = ytmusic.search('the offspring let the bad time rolls')
pprint(songs)
title =songs[0]['videoId']
webbrowser.open_new_tab(f'https://music.youtube.com/watch?v={title}')