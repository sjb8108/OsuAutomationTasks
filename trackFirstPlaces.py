import requests
import json

def firstPlaceLoss(beatmapID) -> dict:
    takenFirstPlaceData = {}
    beatmapLeaderBoardURL = "https://akatsuki.gg/api/v1/scores?sort=score,desc&m=0&relax=1&b=" + str(beatmapID) + "&p=1&l=50"
    beatmapLeaderBoardData = requests.get(beatmapLeaderBoardURL).json()
    beatmapLeaderBoard = beatmapLeaderBoardData["scores"]
    firstPlaceData = {}
    if beatmapLeaderBoardData["scores"][0]["user"]["username"] == "Scottiie": #if statement happens first run through when firstPlaces.json is empty
        pass
    else:
        for placement in range(0, len(beatmapLeaderBoard)):
            if placement == 1:
                firstPlaceData = beatmapLeaderBoardData["scores"][placement]
            elif ["scores"][placement]["user"]["username"] == "Scottiie":
                print() #continue from here
                
def main():
    pageNum = 1
    firstPlaceDict = {}
    firstPlaceLossList = []
    score = []
    with open("textFiles\\firstPlaces.json", "r") as f:
        json.dump(firstPlaceDict, f)
    while score is not None:
        url = "https://akatsuki.gg/api/v1/users/scores/first?mode=0&p=" + str(pageNum) + "&l=100&rx=1&id=81870"
        firstPlaces = requests.get(url).json()
        scores = firstPlaces["scores"]
        for score in scores:
            beatmapID = firstPlaceDict["beatmap"]["beatmap_id"]
            if beatmapID in firstPlaceDict:
                continue #may need to be pass
            else: 
                takenFirstPlaceData = firstPlaceLoss()
                    
            

if __name__ == "__main__": 
    main()