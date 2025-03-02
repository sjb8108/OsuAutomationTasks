import pyautogui
import time
import pyperclip
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE ON

#Last Ran on Date: 2/19/2025
#Date of Next Run: 3/5/2025
#Runs every two weeks

#Next step: Make it so the program knows if the beatmap was unable to load and skip beatmap if so
#Find the icon placements for msgs that contain no beatmap backgroud
#Make it skip any map I changed the status of
#Maybe: Try to save time by making a beatmap not get downloaded twice
#Make it skip beatmap i nomiated

def main(mapNumber):
    downloadNumberOfMaps = mapNumber
    downloadedMaps = 0
    iconStd = False
    while downloadedMaps < downloadNumberOfMaps:
        pixelColor = pyautogui.pixel(770, 1200)
        if pixelColor == (43, 45, 49):
            iconStd = findIconWithNoBackGround()
            pyautogui.moveTo(435, 1115)
            if iconStd is False:
                pyautogui.press('down')
                continue
        else:
            iconStd = findIconWithBackGround()
            pyautogui.moveTo(430, 972)
            if iconStd is False:
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

def findIconWithBackGround():
    #If the title and artist is 2 lines its region for icon is and have background (399, 953, 20, 20) Ex: Mero Meroido
    #If three lines (399, 931, 20, 20) Ex: Geometertu Dash menu
    #If one line (399, 975, 20, 20) Ex: My time
    #if four line (super rare) (399, 909, 20, 20) Ex: Spiderman
    #if five line (I have now only seen it once)) () Ex: Bike Chase
    imageOneLine = pyautogui.screenshot(region=(399, 975, 20, 20))
    imageIconOneLine = np.array(imageOneLine)
    imageIconOneLineGrey = cv2.cvtColor(imageIconOneLine, cv2.COLOR_BGR2GRAY)
    imageTwoLine = pyautogui.screenshot(region=(399, 953, 20, 20))
    imageIconTwoLine = np.array(imageTwoLine)
    imageIconTwoLineGrey = cv2.cvtColor(imageIconTwoLine, cv2.COLOR_BGR2GRAY)
    imageThreeLine = pyautogui.screenshot(region=(399, 931, 20, 20))
    imageIconThreeLine = np.array(imageThreeLine)
    imageIconThreeLineGrey = cv2.cvtColor(imageIconThreeLine, cv2.COLOR_BGR2GRAY)
    imageFourLine = pyautogui.screenshot(region=(399, 909, 20, 20))
    imageIconFourLine = np.array(imageFourLine)
    imageIconFourLineGrey = cv2.cvtColor(imageIconFourLine, cv2.COLOR_BGR2GRAY)
    IconStdImage = cv2.imread("Images\IconStd.png")
    IconStdImageGrey = cv2.cvtColor(IconStdImage, cv2.COLOR_BGR2GRAY)
    differenceRankedFromStatusOneLine, _ = ssim(imageIconOneLineGrey, IconStdImageGrey, full=True)
    differenceRankedFromStatusTwoLine, _ = ssim(imageIconTwoLineGrey, IconStdImageGrey, full=True)
    differenceRankedFromStatusThreeLine, _ = ssim(imageIconThreeLineGrey, IconStdImageGrey, full=True)
    differenceRankedFromStatusFourLine, _ = ssim(imageIconFourLineGrey, IconStdImageGrey, full=True)
    difference = max(differenceRankedFromStatusOneLine, differenceRankedFromStatusTwoLine,
                     differenceRankedFromStatusThreeLine, differenceRankedFromStatusFourLine)
    difference = int(difference * 100)
    if difference > 90:
        return True
    return False
    
def findIconWithNoBackGround():
    return True    
    
if __name__ == "__main__": 
    time.sleep(30)
    pyautogui.PAUSE = 0.5
    main(21) #paramter set manually by user, have discord open, google tab open that isnt blank, osu with date added as caterogry and osu is muted