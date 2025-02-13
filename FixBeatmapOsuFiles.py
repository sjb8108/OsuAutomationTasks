import pyautogui
import pydirectinput
import time
import pyperclip

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#Have it so tabs start with file explorer, then google chrome from left to right
#Last Ran on Date: 
#Date of Next Run: 
#Run every 2 months


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
        if fileBeatmap[0] == fileStopper:
            break
        elif len(fileBeatmap) > 1:
            pass
        else:
            pyautogui.press('del')
            pyautogui.press('down')
            pyautogui.press('up')
            pyautogui.hotkey('ctrl', 'alt', 'tab')
            pyautogui.press('enter')
            fixBeatmapFile(fileBeatmap[0])
        
        
def fixBeatmapFile(beatmapID):
    pyautogui.hotkey('ctrl', 't')
    beatmapURL = defaultBeatmapString + beatmapID
    pyautogui.typewrite(beatmapURL)
    pyautogui.press('enter')
    pyautogui.moveTo(900, 605)
    pyautogui.leftClick()
    time.sleep(5) #time to download beatmap
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    pyautogui.press('enter')

if __name__ == "__main__":
    time.sleep(30)
    pyautogui.PAUSE = 1
    pydirectinput.PAUSE = 1
    main()