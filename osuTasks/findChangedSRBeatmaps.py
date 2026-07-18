import osu
import key as key
import os
import time
import subprocess
import json
import math

BASE_DIR = key.BASE_DIRECTORY
DOTNET_EXE = "dotnet"
DLL_PATH = key.DLLPATH

#Run this program after running getAllBeatmapIDsFromBeatmapSetIDs.py

def main():
    client_id = key.API_ID
    client_secret = key.API_KEY
    redirect_url = "http://127.0.0.1:8080"
    client = osu.Client.from_credentials(client_id, client_secret, redirect_url)
    directory = os.path.join(BASE_DIR, "textFiles", "allBeatmapIDs.txt")
    listOfAllIds = []
    currentIndex = 0
    with open(directory, "r") as f:
        for line in f:
            listOfAllIds.append(line)
    sortedList = sorted(listOfAllIds, key=int)
    resume = ""
    for beatmapID in sortedList:
        #if beatmapID < resume: #can comment out for debugging
            #continue
        newSRValue = math.floor(client.get_beatmap(beatmapID).difficulty_rating *100) / 100
        command = [DOTNET_EXE, DLL_PATH, "difficulty", beatmapID, "-j"]
        while True:
            try:
                result = subprocess.run(command, capture_output=True, text=True)
                data = json.loads(result.stdout)
                oldSRValue = math.floor(data["results"][0]["attributes"]["star_rating"]*100)/100
                break
            except Exception:
                pass
        if newSRValue > 5.99 and oldSRValue < 6.0:
            with open(os.path.join(BASE_DIR, "textFiles", "changedSR.txt"), "a") as myfile:
                myfile.write(beatmapID+"\n")  
        currentIndex += 1
        print("Current Index: " + str(currentIndex) + " / " + str(len(listOfAllIds)))
        os.remove(os.path.join(BASE_DIR, "cache", beatmapID.strip()+".osu"))
        #time.sleep(0.5) #uncomment if you leave the program unattended for long periods of time

if __name__ == "__main__":
    main()