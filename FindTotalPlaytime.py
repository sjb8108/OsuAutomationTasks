from osu import Client
import time
from bs4 import BeautifulSoup
import requests

client_id = 29661
client_secret = "CwzqipNRs7axuZ0C43PwEFzpe4BD3g5tyyiVqlTA"
redirect_url = "http://127.0.0.1:8080"
client = Client.from_credentials(client_id, client_secret, redirect_url)

entireMapList = []
pageNumber = 1
url = "https://akatsuki.gg/api/v1/users/most_played?id=81870&mode=0&p="+str(pageNumber)+"&l=100&rx=1"
mapData = requests.get(url).json()
while (mapData['most_played_beatmaps'] != None):
    print(pageNumber)
    entireMapList = entireMapList + mapData['most_played_beatmaps']
    pageNumber+=1
    url = "https://akatsuki.gg/api/v1/users/most_played?id=81870&mode=0&p="+str(pageNumber)+"&l=100&rx=1"
    time.sleep(1)
    mapData = requests.get(url).json()

approxPlayTime = 0
for index in range(0, len(entireMapList)):
    print("Current Index: " + index)
    beatmap = entireMapList[index]
    beatmapID = beatmap['beatmap']['beatmap_id']
    playcount = beatmap['playcount']
    osuBeatmap = client.get_beatmap(beatmapID)
    lengthOfMap = osuBeatmap.hit_length
    #need to figure out a good distrubition
    time.sleep(1)
