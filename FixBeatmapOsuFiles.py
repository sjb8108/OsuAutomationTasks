import pyautogui
import pydirectinput
import time
import pyperclip

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE ON
#Have it so tabs start with file explorer, then osu!, then google chrome from left to right
#osu! must be in the group : "No Grouping" selected

fileStopper = "2225895 "
defaultBeatmapString = "https://osu.ppy.sh/beatmapsets/"

def main():
    fileBeatmap = ""
    pyautogui.moveTo(550, 120)
    pyautogui.leftClick()
    loopcounter = 0
    while (True):
        pyautogui.press('enter')
        pyautogui.moveTo(120, 60)
        pyautogui.leftClick()
        time.sleep(5) #time for contents in beatmap file to load
        pyautogui.leftClick()
        pyautogui.hotkey('ctrl', 'c')
        filePath = pyperclip.paste()
        fileArray = filePath.split("\\")
        fileBeatmap = fileArray[7]
        fileBeatmap = fileBeatmap.split(" ")
        pyautogui.moveTo(15, 60)
        pyautogui.leftClick()
        pyautogui.press('down')
        if fileBeatmap[0] == fileStopper:
            break
        elif len(fileBeatmap) > 1:
            pass
        else:
            pyautogui.hotkey('ctrl', 'alt', 'tab')
            if loopcounter > 0:
                pyautogui.moveTo(1600, 500)
                pyautogui.leftClick()
            else:
                pyautogui.moveTo(1250, 500)
                pyautogui.leftClick()
            fixBeatmapFile(fileBeatmap[0])
        loopcounter+=1
        
        
def fixBeatmapFile(beatmapID):
    pyautogui.typewrite(beatmapID)
    pydirectinput.moveTo(930, 1350)
    pydirectinput.leftClick()
    pydirectinput.moveTo(1500, 500)
    pydirectinput.leftClick()
    pydirectinput.moveTo(1500, 320)
    pydirectinput.leftClick()
    pydirectinput.press('backspace', presses=len(beatmapID))
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    pyautogui.press('right')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 't')
    beatmapURL = defaultBeatmapString + beatmapID
    pyautogui.typewrite(beatmapURL)
    pyautogui.press('enter')
    pyautogui.moveTo(900, 605)
    pyautogui.leftClick()
    time.sleep(5) #time to download beatmap
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    pyautogui.press('right')
    pyautogui.press('enter')

if __name__ == "__main__":
    time.sleep(30)
    pyautogui.PAUSE = 1
    pydirectinput.PAUSE = 1
    main()