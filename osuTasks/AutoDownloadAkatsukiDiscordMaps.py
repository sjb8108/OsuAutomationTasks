import pyautogui
import time
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2
import pyperclip

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE ON, discord background on Onyx color

#Last Ran on Date: 9/7/25
#Date of Next Run: 9/21/25
#Runs every two weeks

#Make it skip any map I changed the status of/nomiated

defaultBeatmapString = "https://osu.ppy.sh/beatmapsets/"

def main(mapNumber):
    downloadNumberOfMaps = mapNumber
    downloadedMaps = 0
    while downloadedMaps < downloadNumberOfMaps:
        iconStdBackground = findIcon(968, 858) #adding both by 20 (948, 838)
        iconStdNonBackground = findIcon(1095, 985) #adding both by 20
        if iconStdBackground:
            sameMap = isSameMap()
        if (iconStdBackground is False and iconStdNonBackground is False) or sameMap:
            pyautogui.press('down')
            downloadedMaps+=1
            print("Maps left: " + str(downloadNumberOfMaps - downloadedMaps))
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
        pyautogui.moveTo(locDownload[0], locDownload[1])
        pyautogui.leftClick()
    except pyautogui.ImageNotFoundException: #means the beatmap has video
        try:
            locDownload = pyautogui.locateCenterOnScreen("images\\downloadAkatsuki.png", confidence=0.95)
            pyautogui.moveTo(locDownload[0], locDownload[1])
            pyautogui.leftClick()
        except:
            #means download corrupted and need to press reload button
            pass
            
    time.sleep(1)
    
    foundAPIError = False
    errorCountDownload = 0
    while errorCountDownload < 480: #two minutes to load beatmap
        if foundAPIError is False:
            try:
                pyautogui.locateCenterOnScreen("images\\APIError.png", confidence=0.95)
                beatmapPos = getBanchoBeatmap()
                if beatmapPos == (0,0):
                    locComplete = (200, 60)
                    break
                pyautogui.moveTo(beatmapPos[0], beatmapPos[1])
                pyautogui.leftClick()
                foundAPIError = True
            except:
                try:
                    akatBeatmapError = pyautogui.locateCenterOnScreen("images\\akatBeatmapError.png", confidence=0.95)
                    backUpImage = cv2.imread("Images\\backupForAkatBeatmapError.png")
                    cv2.imwrite("Images\\mapBackground.png", backUpImage)
                    locComplete = (200, 60)
                    break
                except:
                    pass
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

def findIcon(ypos, breakypos) -> bool:
    XPOSITION = 464
    YPositionCurrent = ypos
    AREA = 20
    IconStdImage = cv2.imread("Images\IconStd.png")
    IconStdImageGrey = cv2.cvtColor(IconStdImage, cv2.COLOR_BGR2GRAY)
    while True:
        if YPositionCurrent == breakypos:
            return False
        imageLine = pyautogui.screenshot("Images\mode.png", region=(XPOSITION, YPositionCurrent, AREA, AREA))
        imageIconLine = np.array(imageLine)
        imageIconLineGrey = cv2.cvtColor(imageIconLine, cv2.COLOR_BGR2GRAY)
        difference, _ = ssim(imageIconLineGrey, IconStdImageGrey, full=True)
        difference = int(difference * 100)
        if difference > 90:
            pyautogui.moveTo(XPOSITION+30, YPositionCurrent+12)
            return True
        else:
            YPositionCurrent-=22
            
def isSameMap() -> bool:
    lastMapBackground = cv2.imread("Images\mapBackground.png")
    lastMapBackgroundGray = cv2.cvtColor(lastMapBackground, cv2.COLOR_BGR2GRAY)
    currentMapBackground = pyautogui.screenshot("Images\mapBackground.png", region=(467, 1130, 394, 110))
    currentMapBackground = np.array(currentMapBackground)
    currentMapBackgroundGray = cv2.cvtColor(currentMapBackground, cv2.COLOR_BGR2GRAY)
    difference, _ = ssim(currentMapBackgroundGray, lastMapBackgroundGray, full=True)
    difference = int(difference * 100)
    if difference > 90:
        return True
    return False

def getBanchoBeatmap() -> tuple:
    pyautogui.moveTo(200, 60)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    akatsukiAPIURL = pyperclip.paste()
    akatsukiAPIURL = akatsukiAPIURL.split("/")
    beatmapID = akatsukiAPIURL[len(akatsukiAPIURL) - 1]
    beatmapURL = defaultBeatmapString + beatmapID + " "
    pyautogui.typewrite(beatmapURL)
    pyautogui.press('enter')
    websiteLoad = 0
    while websiteLoad < 120:
        pixelExistBeatmap = pyautogui.pixel(200,200)
        pixelDeletedBeatmap = pyautogui.pixel(1000,1000)
        if pixelDeletedBeatmap == (28, 23, 25) or pixelExistBeatmap == (31, 41, 46):
            break
        else:
            websiteLoad+=1
        time.sleep(.25)
    time.sleep(.25)
    if websiteLoad == 120:
        raise pyautogui.PyAutoGUIException #website loaded to slow
    try:
        locDownload = pyautogui.locateCenterOnScreen("Images\\Download.png", confidence=0.95)
        return (locDownload[0], locDownload[1])
    except pyautogui.ImageNotFoundException: #means the beatmap has video
        try:
            locDownload = pyautogui.locateCenterOnScreen("images\\downloadVideo.png", confidence=0.95)
            return (locDownload[0], locDownload[1])
        except: 
            return (0, 0)
        
    
if __name__ == "__main__": 
    time.sleep(30)
    pyautogui.PAUSE = 0.5
    main(764) #paramter set manually by user, have discord open, google tab open that isnt blank, osu with date added as caterogry and osu is muted