import pyautogui
import pydirectinput
import time
import pyperclip
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE ON
#Next step is to make it so it skips taiko, mania, and ctb by looking at the icon instead of downloading the map and such


def main(mapNumber):
    downloadNumberOfMaps = mapNumber
    downloadedMaps = 0
    iconStd = False
    while downloadedMaps < downloadNumberOfMaps:
        pixelColor = pyautogui.pixel(770, 1200)
        if pixelColor == (43, 45, 49):
            pyautogui.moveTo(435, 1115)
        else:
            pyautogui.moveTo(430, 972)
            iconStd = findIconWithBackGround()
        pyautogui.leftClick()
        downloadBeatmapTracker()
        pyautogui.hotkey('ctrl', 'alt', 'tab')
        time.sleep(2)
        if downloadedMaps == 0:
            pyautogui.press('right', presses=1)
        else:
            pyautogui.press('right')
        pyautogui.moveTo(650,270)
        pyautogui.press('space')
        pyautogui.leftClick()
        pyautogui.leftClick()
        pyautogui.hotkey('ctrl', 'alt', 'tab')
        pyautogui.press('left')
        pyautogui.press('enter')
        url = getURL()
        if "mania" in url or "taiko" in url or "fruits" in url:
            deleteBeatmap()
        pyautogui.hotkey('ctrl', 'f4')
        pyautogui.hotkey('ctrl', 'alt', 'tab')
        pyautogui.press('right')
        pyautogui.press('enter')
        pyautogui.moveTo(430, 5)
        pyautogui.leftClick()
        pyautogui.press('up')
        pyautogui.press('down')
        downloadedMaps+=1

def deleteBeatmap():
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    pyautogui.press('space')
    pydirectinput.moveTo(1500, 700)
    pyautogui.rightClick()
    pydirectinput.moveTo(1500, 500)
    pyautogui.leftClick()
    pydirectinput.moveTo(1500, 325)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    pyautogui.press('enter')
    
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
    return False
    
if __name__ == "__main__": 
    image = pyautogui.screenshot(region=(399, 953, 20, 20))
    image.save(r"C:\Users\Scott\Documents\OsuCoding\status.png")
    imageIcon = np.array(image)
    imageIconGrey = cv2.cvtColor(imageIcon, cv2.COLOR_BGR2GRAY)
    IconStdImage = cv2.imread("IconStd.png")
    IconStdImageGrey = cv2.cvtColor(IconStdImage, cv2.COLOR_BGR2GRAY)
    differenceRankedFromStatus, _ = ssim(imageIconGrey, IconStdImageGrey, full=True)
    print(differenceRankedFromStatus)
    #time.sleep(30)
    pyautogui.PAUSE = 0.5
    #main(112) #paramter set manually by user, have discord open, google tab open that isnt blank, osu with date added as caterogry and osu is muted
    #If the title and artist is 2 lines its region for icon is and have background (399, 953, 20, 20) Ex: Mero Meroido
    #If three lines (399, 931, 20, 20) Ex: Geometertu Dash menu
    #If one line (399, 975, 20, 20) Ex: My time
    #if four line (super rare) (399, 909, 20, 20) Ex: Spiderman