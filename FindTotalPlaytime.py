from osu import Client
import osu
import time
import requests
import math

#Run every 6 months
#Last Run: 3/11/2025
#Next Run: 6/1/2025
#Current Total osu! Playtime: 22 days (Bancho) + 33 days (Akatsuki recorded in most played beatmaps ~24k = 68%) + 16 days (Average for playtime that wasnt recorded ~11k = 31%) = ~71 days +-1 at 25%
#Current Total osu! Playtime: 22 days (Bancho) + 41 days (Akatsuki recorded in most played beatmaps ~24k = 68%) + 19 days (Average for playtime that wasnt recorded ~11k = 31%) = ~82 days +-1 at 50% 


client_id = no_id_for_you
client_secret = "no secret for u"
redirect_url = "http://127.0.0.1:8080"
client = Client.from_credentials(client_id, client_secret, redirect_url)

entireMapList = []
pageNumber = 1
url = "https://akatsuki.gg/api/v1/users/most_played?id=81870&mode=0&p="+str(pageNumber)+"&l=100&rx=1"
mapData = requests.get(url).json()
while (mapData['most_played_beatmaps'] != None):
    entireMapList = entireMapList + mapData['most_played_beatmaps']
    pageNumber+=1
    url = "https://akatsuki.gg/api/v1/users/most_played?id=81870&mode=0&p="+str(pageNumber)+"&l=100&rx=1"
    time.sleep(1)
    mapData = requests.get(url).json()

print("Loading playcounts completed.")
#Can make more variable if I wanted to have different distrubitions current is 50%
approxPlayTimeSeconds = 0
totalPlaycount = 0
for index in range(0, len(entireMapList)):
    beatmap = entireMapList[index]
    beatmapID = beatmap['beatmap']['beatmap_id']
    playcount = beatmap['playcount']
    try:
        osuBeatmap = client.get_beatmap(beatmapID)
    except(osu.exceptions.RequestException):
        continue
    lengthOfMap = osuBeatmap.hit_length
    totalPlaycount += playcount
    print("Current Index: " + str(index) + "(" + (str((len(entireMapList)) - index)) + " Remaining)")
    print("Current Map: " + beatmap['beatmap']['song_name'])
    print("Current Total Playcount: " + str(totalPlaycount))
    if playcount == 1:
        approxPlayTimeSeconds += lengthOfMap
    else:
        approxPlayTimeSeconds += lengthOfMap
        playcount-=1
        distributedLength = math.floor(lengthOfMap * 0.5)
        restOfPlaytimeForMap = distributedLength * playcount
        approxPlayTimeSeconds += restOfPlaytimeForMap
    print("Current Playtime: " + str(approxPlayTimeSeconds))
    time.sleep(1)

print("Approx Playtime in Seconds: " + str(approxPlayTimeSeconds))
approxPlayTimeMinutes = approxPlayTimeSeconds / 60
print("Approx Playtime in Minutes: " + str(approxPlayTimeMinutes))
approxPlayTimeHours = approxPlayTimeMinutes / 60
print("Approx Playtime in Hours: " + str(approxPlayTimeHours))
approxPlayTimeDays = approxPlayTimeHours / 24
print("Approx Playtime in Days: " + str(approxPlayTimeDays))
