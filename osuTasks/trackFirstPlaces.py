import requests
import json
import time

def firstPlaceChange(beatmapID, songName) -> dict:
    takenFirstPlaceData = {}
    addedFirstPlaceData = {}
    beatmapLeaderBoardURL = "https://akatsuki.gg/api/v1/scores?sort=pp,desc&m=0&relax=1&b=" + str(beatmapID) + "&p=1&l=50"
    beatmapLeaderBoardData = requests.get(beatmapLeaderBoardURL).json()
    beatmapLeaderBoard = beatmapLeaderBoardData["scores"]
    firstPlaceData = {}
    if beatmapLeaderBoard is None: #beatmap was deleted
        return None
    if beatmapLeaderBoardData["scores"][0]["user"]["username"] == "Scottiie": #if statement happens first run through when firstPlaces.json is empty or get my first place back
        myFirstPlaceData = beatmapLeaderBoardData["scores"][0]
        addedFirstPlaceData["Map"] = songName
        addedFirstPlaceData["PP"] = myFirstPlaceData["pp"]
        addedFirstPlaceData["Accuracy"] = myFirstPlaceData["accuracy"]
        return addedFirstPlaceData
    else:
        for placement in range(0, len(beatmapLeaderBoard)):
            if placement == 0:
                firstPlaceData = beatmapLeaderBoardData["scores"][placement]
            elif beatmapLeaderBoard[placement]["user"]["username"] == "Scottiie":
                myBeatmapData = beatmapLeaderBoardData["scores"][placement]
                takenFirstPlaceData["takenBy"] = firstPlaceData["user"]["username"]
                takenFirstPlaceData["Map"] = songName
                takenFirstPlaceData["PPDifference"] = firstPlaceData["pp"] - myBeatmapData["pp"]
                takenFirstPlaceData["myAcc"] = myBeatmapData["accuracy"]
                takenFirstPlaceData["SniperAcc"] = firstPlaceData["accuracy"]
                return takenFirstPlaceData
            
def getAllFirstPlaces() -> dict:
    pageNum = 1
    CurrentFirstPlaceDict = {}
    while True:
        url = "https://akatsuki.gg/api/v1/users/scores/first?mode=0&p=" + str(pageNum) + "&l=100&rx=1&id=81870"
        firstPlaces = requests.get(url).json()
        scores = firstPlaces["scores"]
        if scores is None:
            break
        for score in scores:
            firstPlaceData = {}
            beatmapID = score["beatmap"]["beatmap_id"]
            firstPlaceData["Map"] = score["beatmap"]["song_name"]
            firstPlaceData["pp"] = score["pp"]
            firstPlaceData["Accuracy"] = score["accuracy"]
            CurrentFirstPlaceDict[beatmapID] = firstPlaceData
        pageNum+=1
        time.sleep(1)
    return CurrentFirstPlaceDict
             
def main():
    with open("textFiles\\firstPlaces.json") as f:
        priorFirstPlaceDict = json.load(f)
    with open("textFiles\\takenFirstPlaces.json", "r") as fl:
        takenFirstPlaceDict = json.load(fl)
    
    currentFirstPlaceDict = getAllFirstPlaces()
    scoreNum = 1
    
    for beatmapID in currentFirstPlaceDict:
        songName = currentFirstPlaceDict[beatmapID]["Map"]
        if str(beatmapID) not in takenFirstPlaceDict and str(beatmapID) not in priorFirstPlaceDict: #new first place
            initalFirstPlaceData = firstPlaceChange(beatmapID, songName)
            priorFirstPlaceDict[beatmapID] = initalFirstPlaceData
            scoreNum+=1
        elif str(beatmapID) in takenFirstPlaceDict and str(beatmapID) not in priorFirstPlaceDict: #got my number 1 back and need to add my data back and remove from taken first place dict/list
            del takenFirstPlaceDict[str(beatmapID)]
            snipedBackData = firstPlaceChange(beatmapID, songName)
            priorFirstPlaceDict[beatmapID] = snipedBackData
            scoreNum+=1
        else: #number 1 wasnt sniped, do nothing
            scoreNum+=1
            continue

    #loop over priorfirstplaces to see any if scores were sniped
    lossNumberOnes = []
    
    for beatmapID in priorFirstPlaceDict:
        songName = priorFirstPlaceDict[beatmapID]["Map"]
        if int(beatmapID) not in currentFirstPlaceDict: #first place taken
            lossNumberOnes.append(beatmapID)
            snipedScoreData = firstPlaceChange(beatmapID, songName)
            if snipedScoreData is None:
                continue
            takenFirstPlaceDict[beatmapID] = snipedScoreData
            
    for beatmapID in lossNumberOnes:
        del priorFirstPlaceDict[beatmapID]
    
    with open("textFiles\\firstPlaces.json", "w") as f:
        json.dump(priorFirstPlaceDict, f, indent=2)
    with open("textFiles\\takenFirstPlaces.json", "w") as fl:
        json.dump(takenFirstPlaceDict, fl, indent=2)
    
if __name__ == "__main__": 
    main()