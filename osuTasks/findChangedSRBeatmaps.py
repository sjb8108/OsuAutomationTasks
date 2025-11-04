import osu
import key as key
import os
import rosu_pp_py
import key as key
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
    for filename in sortedList:
        print("Processing File: " + filename)
        beatmapID = filename.split(".")[0]
        newSRValue = client.get_beatmap(beatmapID).difficulty_rating
        beatmap = rosu_pp_py.Beatmap(path=os.path.join(directory, filename))
        oldSRValue = calc.calculate(beatmap).stars
        print("New SR Value: " + str(newSRValue) + " | Old SR Value: " + str(oldSRValue))
        if newSRValue > 5.99 and oldSRValue < 6.0:
            with open(os.path.join(BASE_DIR, "textFiles", "changedSR"), "a") as myfile:
                myfile.write(filename+"\n")  
        currentIndex += 1
        print("Current Index: " + str(currentIndex) + " / " + str(len(os.listdir(directory))))
        time.sleep(1)
        
if __name__ == "__main__":
    main()