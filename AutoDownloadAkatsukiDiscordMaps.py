import pyautogui
import time
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE ON

#Last Ran on Date: 8/6/25
#Date of Next Run: 8/20/25
#Runs every two weeks

#Next step: Make it so the program knows if the beatmap was unable to load and skip beatmap if so
#Make it skip any map I changed the status of/nomiated
#Maybe: Try to save time by making a beatmap not get downloaded twice

def main(mapNumber):
    downloadNumberOfMaps = mapNumber
    downloadedMaps = 0
    while downloadedMaps < downloadNumberOfMaps:
        iconStdBackground = findIcon(972, 862)
        iconStdNonBackground = findIcon(1099, 989)
        if iconStdBackground is False and iconStdNonBackground is False:
            pyautogui.press('down')
            downloadedMaps+=1
            print("Downloaded Maps: " + str(downloadedMaps))
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
        print("Maps left: " + str(downloadNumberOfMaps - downloadedMaps))
    
def downloadBeatmapTracker():
    #at some point should also implement the download checker that checks to make sure the download finished for now its fine
    #should also make the lower maybe a function that can be called from a different file where the pixel loc and color are parameters
    websiteLoad = 0
    while websiteLoad < 120:
        pixel = pyautogui.pixel(100,100)
        if pixel == (53, 88, 130):
            break
        else:
            websiteLoad+=1
        time.sleep(.25)
    time.sleep(.25)
    if websiteLoad == 120:
        raise pyautogui.PyAutoGUIException #website loaded to slow
    try:
        locDownload = pyautogui.locateCenterOnScreen("Images\\downloadVideoAkatsuki.png", confidence=0.95)
    except pyautogui.ImageNotFoundException: #means the beatmap has video
        try:
            locDownload = pyautogui.locateCenterOnScreen("images\\downloadAkatsuki.png", confidence=0.95)
            pyautogui.moveTo(locDownload[0], locDownload[1])
            pyautogui.leftClick()
        except:
            raise pyautogui.ImageNotFoundException #means download corrupted and need to press reload button
        
    time.sleep(1)
    
    errorCountDownload = 0
    while errorCountDownload < 480: #two minutes to load beatmap
        try:
            locComplete = pyautogui.locateCenterOnScreen("Images\\downloadComplete.png")
            break
        except:
            errorCountDownload+=1
        time.sleep(.25)
    if errorCountDownload == 480:
        raise pyautogui.PyAutoGUIException #wifi is really slow
    pyautogui.moveTo(locComplete[0], locComplete[1])
    pyautogui.leftClick()
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl', 'w')

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
    main(123) #paramter set manually by user, have discord open, google tab open that isnt blank, osu with date added as caterogry and osu is muted