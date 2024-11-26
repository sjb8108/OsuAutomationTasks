import cv2
import pyautogui
import pydirectinput
import numpy as np
from skimage.metrics import structural_similarity as ssim
import time
#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE OFF

def main(numberOfMapsToProcess):
    time.sleep(3) #Time for me to put cursour on osu
    rankedImage = cv2.imread("\Images\Ranked.png")
    lovedImage = cv2.imread("\Images\Loved.png")
    pendingImage = cv2.imread("\Images\Pending.png")
    removedImage = cv2.imread("\Images\Removed.png")
    qualifiedImage = cv2.imread("\Images\Qualified.png")
    rankedImageGray = cv2.cvtColor(rankedImage, cv2.COLOR_BGR2GRAY)
    lovedImageGray = cv2.cvtColor(lovedImage, cv2.COLOR_BGR2GRAY)
    pendingImageGray = cv2.cvtColor(pendingImage, cv2.COLOR_BGR2GRAY)
    removedImageGray = cv2.cvtColor(removedImage, cv2.COLOR_BGR2GRAY)
    qualifiedImageGray = cv2.cvtColor(qualifiedImage, cv2.COLOR_BGR2GRAY)
    while numberOfMapsToProcess > 0:
        print(numberOfMapsToProcess)
        time.sleep(3)  #Time for beatmap to load
        mapStatusImage = pyautogui.screenshot(region=(10,10,50,50))
        mapStatusImage = np.array(mapStatusImage)
        mapStatusImageGray = cv2.cvtColor(mapStatusImage, cv2.COLOR_BGR2GRAY)
        differenceRankedFromStatus, _ = ssim(mapStatusImageGray, rankedImageGray, full=True)
        differenceLovedFromStatus, _ = ssim(mapStatusImageGray, lovedImageGray, full=True)
        differencePendingFromStatus, _ = ssim(mapStatusImageGray, pendingImageGray, full=True)
        differenceRemovedFromStatus, _ = ssim(mapStatusImageGray, removedImageGray, full=True)
        differenceQualifiedFromStatus, _ = ssim(mapStatusImageGray, qualifiedImageGray, full=True)
        if (differencePendingFromStatus > differenceRankedFromStatus and 
            differencePendingFromStatus > differenceLovedFromStatus and 
            differencePendingFromStatus > differenceRemovedFromStatus and
            differencePendingFromStatus > differenceQualifiedFromStatus):
            
            time.sleep(0.5)
            pydirectinput.moveTo(1500, 700)
            time.sleep(0.5)
            pydirectinput.rightClick()
            time.sleep(0.5)
            pydirectinput.moveTo(1500, 400)
            time.sleep(0.5)
            pydirectinput.leftClick()
            time.sleep(0.5)
            pydirectinput.moveTo(1650, 250)
            time.sleep(0.5)
            pydirectinput.leftClick()
            time.sleep(0.5)
            pydirectinput.moveTo(1650, 1150)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.5)
            
        elif (differenceRemovedFromStatus > differenceRankedFromStatus and
            differenceRemovedFromStatus > differenceLovedFromStatus and
            differenceRemovedFromStatus > differencePendingFromStatus and
            differenceRemovedFromStatus > differenceQualifiedFromStatus):
            
            time.sleep(0.5)
            pydirectinput.moveTo(1500, 700)
            time.sleep(0.5)
            pydirectinput.rightClick()
            time.sleep(0.5)
            pydirectinput.moveTo(1500, 400)
            time.sleep(0.5)
            pydirectinput.leftClick()
            time.sleep(0.5)
            pydirectinput.moveTo(1650, 250)
            time.sleep(0.5)
            pydirectinput.leftClick()
            time.sleep(0.5)
            pydirectinput.moveTo(1650, 1150)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.5)
        pydirectinput.press('right')
        numberOfMapsToProcess-=1
     
main(4000)
