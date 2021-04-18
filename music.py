from ytmusicapi import YTMusic
from pprint import pprint
import webbrowser
# from  selenium import webdriver
#
# COUNTER = 0
#
#
#
# def play_music(text , driver=None):
#     ytmusic = YTMusic()
#     songs = ytmusic.search(f'{text}')
#     pprint(songs)
#     global COUNTER
#     for material in songs:
#         material_type = material['resultType']
#         if material_type=='song':
#             id = material['videoId']
#             break
#     link = f'https://music.youtube.com/watch?v={id}'
#
#     driver.get(link)
#     if COUNTER > 0:
#         driver.switch_to.window(driver.window_handles[0])
#         driver.close()
#     COUNTER +=1







def play_music(text):
    ytmusic = YTMusic()
    songs = ytmusic.search(f'{text}')
    pprint(songs)
    for material in songs:
        material_type = material['resultType']
        if material_type=='song':
            id = material['videoId']
            break

    webbrowser.open_new_tab(f'https://music.youtube.com/watch?v={id}')

