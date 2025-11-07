import osu
import key as key
import os
import rosu_pp_py
import key as key
import pyautogui
import requests
import time

BASE_DIR = key.BASE_DIRECTORY

def main():
    client_id = key.API_ID
    client_secret = key.API_KEY
    redirect_url = "http://127.0.0.1:8080"
    client = osu.Client.from_credentials(client_id, client_secret, redirect_url)
    calc = rosu_pp_py.Difficulty()
    directory = os.path.join(BASE_DIR, "testOsuFiles", "2025_10_08_osu_files")
    currentIndex = 0
    lst = os.listdir(directory)
    sortedList = sorted(lst, key=lambda x: int(x.split(".")[0]))
    resume = "3454811"
    for filename in sortedList:
        beatmapID = filename.split(".")[0]
        if int(resume) > int(beatmapID):
            currentIndex += 1
            continue
        pyautogui.moveTo(1000, 1000) #comment out pyautogui lines if you use the computer while program is running
        pyautogui.leftClick()
        print("Processing File: " + filename)
        try:
            newSRValue = client.get_beatmap(beatmapID).difficulty_rating
        except(osu.exceptions.RequestException):
            currentIndex += 1
            continue
        except(requests.exceptions.HTTPError):
            while True:
                try:
                    newSRValue = client.get_beatmap(beatmapID).difficulty_rating
                    currentIndex += 1
                    break
                except(requests.exceptions.HTTPError):
                    time.sleep(1)
        beatmap = rosu_pp_py.Beatmap(path=os.path.join(directory, filename))
        oldSRValue = calc.calculate(beatmap).stars
        print("New SR Value: " + str(newSRValue) + " | Old SR Value: " + str(oldSRValue))
        if newSRValue > 5.99 and oldSRValue < 6.0:
            with open(os.path.join(BASE_DIR, "textFiles", "changedSR.txt"), "a") as myfile:
                myfile.write(filename+"\n")  
        currentIndex += 1
        print("Current Index: " + str(currentIndex) + " / " + str(len(os.listdir(directory))))
        pyautogui.moveTo(1000, 500)
        pyautogui.leftClick()
        #time.sleep(0.5) #uncomment if you leave the program unattended for long periods of time
        
if __name__ == "__main__":
    main()