import pandas as pd
import numpy as np
from collections import defaultdict

# get all music information for later check
def getAllMusic():
    df = pd.read_excel("./Music_Index.xlsx", sheet_name=["song"])
    table = df["song"]
    music_list = []

    first_line = table.columns.array
    music_list.append(str(first_line[0])+str(first_line[1]))

    for index in range(0, table.shape[0]):
        music_list.append(str(table.iat[index,0])+str(table.iat[index,1]))
    return music_list

# get the planned play list dict
# Also check with real PL
def getEstimatePL(sheet, name_col, singer_col, real_pl):
    df = pd.read_excel("./Music_Index.xlsx", sheet_name=[sheet])
    table = df[sheet]
    playlist = defaultdict(int)

    first_line = table.columns.array
    playlist[str(first_line[name_col])+str(first_line[singer_col])] = 0

    for index in range(0, table.shape[0]):
        # ways to check nan
        if(table.iat[index,name_col] != table.iat[index,name_col]): break
        playlist[str(table.iat[index,name_col])+str(table.iat[index,singer_col])] = 0

    df = pd.read_excel("./Music_Index.xlsx", sheet_name=[real_pl])
    table = df[real_pl]
    real_playlist = []

    for index in range(0, table.shape[0]):
        real_playlist.append(str(table.iat[index,0])+str(table.iat[index,1]))
    Flag = True
    for item in real_playlist:
        playlist[item] += 1
        if(item not in playlist):
            print("Item Error " + item)
            Flag = False
    for key in playlist:
        if(playlist[key] != 1):
            print("Key Error " + key)
            print(playlist[key])
            Flag = False
    if(Flag): print("Check Success " + real_pl + " !")
    return real_playlist

# check all songs = all playlists, no duplicate or missing
def finalCheck(playlists, music_list):
    print(len(playlists), len(music_list))
    Flag = True
    for song in music_list:
        if(song not in playlists):
            print("Music Error " + song)
            Flag = False
    for song in playlists:
        if(song not in music_list):
            print("Play list Error " + song)
            Flag = False
    if(Flag): print("Check Success !")

music_list = getAllMusic()
joker_playlist = getEstimatePL("中文", 0, 1, "Joker")
Spade_playlist = getEstimatePL("中文", 2, 3, "Spade")
Heart_playlist = getEstimatePL("中文", 4, 5, "Heart")
Club_playlist = getEstimatePL("中文", 6, 7, "Club")
Diamond_playlist = getEstimatePL("中文", 8, 9, "Diamond")
playlist_2013 = getEstimatePL("欧美", 0, 1, "2013-Present")
playlist_2000 = getEstimatePL("欧美", 3, 4, "2000-2012")
playlist_1999 = getEstimatePL("欧美", 6, 7, "Pre-1999")
Anime1_playlist = getEstimatePL("东亚", 0, 1, "Anime1")
Asia_playlist = getEstimatePL("东亚", 2, 3, "Asia")
BGM_playlist = getEstimatePL("BGM", 0, 1, "BGM-1")
TV_playlist = getEstimatePL("BGM", 2, 3, "TV")
Classical_playlist = getEstimatePL("放松+古典", 0, 1, "Classical")
Relax_playlist = getEstimatePL("放松+古典", 3, 4, "Relax")
playlists = joker_playlist + Spade_playlist + Heart_playlist + Club_playlist + Diamond_playlist + playlist_2013
playlists = playlists + playlist_2000 + playlist_1999 + Anime1_playlist + Asia_playlist + BGM_playlist + TV_playlist
playlists = playlists + Classical_playlist + Relax_playlist
finalCheck(playlists, music_list)