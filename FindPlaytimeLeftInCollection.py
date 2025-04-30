import pydirectinput
import pyautogui
import osu
import time
import pyperclip
import key

def main():
    client_id = key.API_ID
    client_secret = key.API_KEY
    redirect_url = "http://127.0.0.1:8080"
    client = osu.Client.from_credentials(client_id, client_secret, redirect_url)
    totalPlaytime = 0
    
    while (True):
        pydirectinput.moveTo(660, 250)
        pydirectinput.leftClick()
        pydirectinput.leftClick()
        time.sleep(1)
        pyautogui.moveTo(660, 50)
        pyautogui.leftClick()
        pyautogui.hotkey('ctrl', 'c')
        url = pyperclip.paste()
        url = url.split('/')
        urlBeatsetID = url[4]
        urlBeatsetID = urlBeatsetID.split('#')
        beatmapsetID = urlBeatsetID[0]
        beatmapID = url[5]
        try:
            osuBeatmapset = client.get_beatmapset(beatmapsetID)
        except(osu.exceptions.RequestException):
            continue
        osuBeatmapset = osuBeatmapset.beatmaps
        for beatmap in osuBeatmapset:
            if beatmap.id == beatmapID:
                totalPlaytime += beatmap.hit_length
                break
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('ctrl', 'alt', 'tab')
        pyautogui.press('enter')
        pydirectinput.leftClick()
        pydirectinput.press('right')
        
if __name__ == "__main__":
    pydirectinput.PAUSE = 1
    time.sleep(3)
    main()