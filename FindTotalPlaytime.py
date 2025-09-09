import osu
import time
import requests
import math
import key

#Run every 6 months
#Last Run: 9/3/2025
#Next Run: 12/1/2025
#Current Total osu! Playtime: ~1656 hours or 69 days

BANCHO_PLAYTIME_SECONDS = 1882980 #add api call
AKATSUKI_PLAYCOUNT = 38869 #add api call

def main():
    client_id = key.API_ID
    client_secret = key.API_KEY
    redirect_url = "http://127.0.0.1:8080"
    client = osu.Client.from_credentials(client_id, client_secret, redirect_url)

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

    approxPlayTimeSecondsEighth = 0
    approxPlayTimeSecondsQuarter = 0
    approxPlayTimeSecondsHalf = 0
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
            approxPlayTimeSecondsEighth += lengthOfMap
            approxPlayTimeSecondsQuarter += lengthOfMap
            approxPlayTimeSecondsHalf += lengthOfMap
        else:
            approxPlayTimeSecondsEighth += lengthOfMap
            approxPlayTimeSecondsQuarter += lengthOfMap
            approxPlayTimeSecondsHalf += lengthOfMap
            playcount-=1
            distributedLengthHalf = math.floor(lengthOfMap * 0.5)
            distributedLengthQuarter = math.floor(lengthOfMap * 0.25)
            distributedLengthEighth = math.floor(lengthOfMap * 0.125)
            restOfPlaytimeForMapHalf = distributedLengthHalf * playcount
            restOfPlaytimeForMapQuarter = distributedLengthQuarter * playcount
            restOfPlaytimeForMapEighth = distributedLengthEighth * playcount
            approxPlayTimeSecondsHalf += restOfPlaytimeForMapHalf
            approxPlayTimeSecondsQuarter += restOfPlaytimeForMapQuarter
            approxPlayTimeSecondsEighth += restOfPlaytimeForMapEighth
        print("Current Playtime (Half): " + str(approxPlayTimeSecondsHalf))
        print("Current Playtime (Quarter): " + str(approxPlayTimeSecondsQuarter))
        print("Current Playtime (Eighth): " + str(approxPlayTimeSecondsEighth))
        time.sleep(1)
    
    approxPlayTimeList = [approxPlayTimeSecondsHalf, approxPlayTimeSecondsQuarter, approxPlayTimeSecondsEighth]
    approxTimeTitle = ["Half", "Quarter", "Eighth"]
    percentOfNonIncludedAkatsukiPlaytime = (AKATSUKI_PLAYCOUNT - totalPlaycount) / AKATSUKI_PLAYCOUNT
    print("This is the percentage of playcount that isnt directly calculated: " + str(percentOfNonIncludedAkatsukiPlaytime))
    index = 0
    for approxPlayTimeSeconds in approxPlayTimeList:
        nonIncludedAkatsukiPlaytime = approxPlayTimeSeconds * percentOfNonIncludedAkatsukiPlaytime 
        approxPlayTimeSeconds = approxPlayTimeSeconds + nonIncludedAkatsukiPlaytime + BANCHO_PLAYTIME_SECONDS
        print(approxTimeTitle[index]+ ": ")
        print("Approx Playtime in Seconds: " + str(approxPlayTimeSeconds))
        approxPlayTimeMinutes = approxPlayTimeSeconds / 60
        print("Approx Playtime in Minutes: " + str(approxPlayTimeMinutes))
        approxPlayTimeHours = approxPlayTimeMinutes / 60
        print("Approx Playtime in Hours: " + str(approxPlayTimeHours))
        approxPlayTimeDays = approxPlayTimeHours / 24
        print("Approx Playtime in Days: " + str(approxPlayTimeDays))
        print("")
        index+=1

main()