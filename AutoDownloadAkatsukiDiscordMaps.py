import pyautogui
import time
import pyperclip
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE ON

#Last Ran on Date: 3/19/2025
#Date of Next Run: 4/2/2025
#Runs every two weeks

#Next step: Make it so the program knows if the beatmap was unable to load and skip beatmap if so
#Find the icon placements for msgs that contain no beatmap backgroud
#Make it skip any map I changed the status of
#Maybe: Try to save time by making a beatmap not get downloaded twice
#Make it skip beatmap i nomiated

def main(mapNumber):
    downloadNumberOfMaps = mapNumber
    downloadedMaps = 0
    while downloadedMaps < downloadNumberOfMaps:
        iconStdBackground = findIcon(972, 862)
        iconStdNonBackground = findIcon(1099, 989)
        if iconStdBackground is False and iconStdNonBackground is False:
            pyautogui.press('down')
            continue
        time.sleep(2)
        pyautogui.leftClick()
        downloadBeatmapTracker()
        pyautogui.hotkey('ctrl', 'alt', 'tab')
        pyautogui.press('enter')
        pyautogui.moveTo(430, 5)
        pyautogui.leftClick()
        pyautogui.press('up')
        pyautogui.press('down')
        downloadedMaps+=1
    
def downloadBeatmapTracker():
    url = getURL()
    while "api" in url:
        url = getURL()
    
def getURL():
    pyautogui.moveTo(300, 60)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.moveTo(1000, 1000)
    pyautogui.leftClick()
    url = pyperclip.paste()
    return url

def findIcon(ypos, breakypos):
    XPOSITION = 465
    YPositionCurrent = ypos
    AREA = 20
    IconStdImage = cv2.imread("Images\IconStd.png")
    IconStdImageGrey = cv2.cvtColor(IconStdImage, cv2.COLOR_BGR2GRAY)
    while True:
        if YPositionCurrent == breakypos:
            return False
        imageLine = pyautogui.screenshot(region=(XPOSITION, YPositionCurrent, AREA, AREA))
        imageIconLine = np.array(imageLine)
        imageIconLineGrey = cv2.cvtColor(imageIconLine, cv2.COLOR_BGR2GRAY)
        difference, _ = ssim(imageIconLineGrey, IconStdImageGrey, full=True)
        difference = int(difference * 100)
        if difference > 90:
            pyautogui.moveTo(XPOSITION+30, YPositionCurrent+12)
            return True
        else:
            YPositionCurrent-=22
    
if __name__ == "__main__": 
    time.sleep(30)
    pyautogui.PAUSE = 0.5
    main(340) #paramter set manually by user, have discord open, google tab open that isnt blank, osu with date added as caterogry and osu is muted