import pyautogui
import time
import pyperclip
import cv2

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#Have it so tabs start with file explorer, then google chrome from left to right, osu must still be open but the first two tabs are file and chrome
#Last Ran on Date: 03/19/2025
#Date of Next Run: 04/19/2025
#Run every month

#Make it so it left clicks folder and gets id instead of having it open the file location as opening file location has caused problems if 
#it takes to long to load in

fileStopper = "1640260"
defaultBeatmapString = "https://osu.ppy.sh/beatmapsets/"

def main():
    fileBeatmap = ""
    pyautogui.moveTo(550, 120)
    pyautogui.leftClick()
    while (True):
        pyautogui.moveTo(600, 600)
        pyautogui.hotkey('alt', 'enter')
        loc = pyautogui.locateOnScreen("Images\\fileNameFinder.png")
        pyautogui.moveTo(loc[0]+20, loc[1]-30)
        pyautogui.leftClick()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        fileBeatmap = pyperclip.paste()
        pyautogui.hotkey('alt', 'f4')
        fileBeatmap = fileBeatmap.split(" ")
        if fileBeatmap[0] == fileStopper:
            break
        elif len(fileBeatmap) > 1:
            pyautogui.press('down')
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
    time.sleep(3)
    pyautogui.PAUSE = 1
    main()