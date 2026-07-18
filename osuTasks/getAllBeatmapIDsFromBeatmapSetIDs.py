#Given a folder of osu (.osz) files that look like 30 The Cloud Room - Hey Now Now.osz format put all beatmapids into a text file

import time
import osu
from pathlib import Path
import key as key
import os


LOCATION = key.ROOT
client_id = key.API_ID
client_secret = key.API_KEY

def main():
    root = Path(LOCATION)
    for file in root.rglob("*.osz"):
        _, file = os.path.split(file)
        beatmapsetID = file.split(" ")[0]
        redirect_url = "http://127.0.0.1:8080"
        client = osu.Client.from_credentials(client_id, client_secret, redirect_url)
        beatmapset = client.get_beatmapset(beatmapsetID)
        for beatmap in beatmapset.beatmaps:
            with open(r"textFiles\\allBeatmapIDs.txt", "a") as txtFile:
                txtFile.write(str(beatmap.id) + "\n")
        time.sleep(1)
        
main()