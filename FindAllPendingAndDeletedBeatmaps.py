import cv2
import pydirectinput
import numpy as np
from skimage.metrics import structural_similarity as ssim
import mss
#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE OFF
#Currently at keep weaving your spider way, spider way diff
#Fully Ran on Date: 12/24/2024
#Should Run Next on Date: 04/01/2025
#Goal: Combine MovePendingAndDeletedBeatmaps.py into here

def main(numberOfMapsToProcess):
    pydirectinput.PAUSE = 3
    pydirectinput.moveTo(1000, 600)
    rankedImage = cv2.imread("Images\Ranked.png")
    lovedImage = cv2.imread("Images\Loved.png")
    pendingImage = cv2.imread("Images\Pending.png")
    removedImage = cv2.imread("Images\Removed.png")
    qualifiedImage = cv2.imread("Images\Qualified.png")
    rankedImageGray = cv2.cvtColor(rankedImage, cv2.COLOR_BGR2GRAY)
    lovedImageGray = cv2.cvtColor(lovedImage, cv2.COLOR_BGR2GRAY)
    pendingImageGray = cv2.cvtColor(pendingImage, cv2.COLOR_BGR2GRAY)
    removedImageGray = cv2.cvtColor(removedImage, cv2.COLOR_BGR2GRAY)
    qualifiedImageGray = cv2.cvtColor(qualifiedImage, cv2.COLOR_BGR2GRAY)
    while numberOfMapsToProcess > 0:
        print(numberOfMapsToProcess)
        region = {"left": 10, "top": 10, "width": 50, "height": 50}
        mapStatusImage = mss.mss().grab(region) 
        mapStatusIconImage = np.array(mapStatusImage)
        mapStatusImageGray = cv2.cvtColor(mapStatusIconImage, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("captured_status.png", mapStatusImageGray)
        differenceRankedFromStatus = ssim(mapStatusImageGray, rankedImageGray)
        differenceLovedFromStatus = ssim(mapStatusImageGray, lovedImageGray)
        differencePendingFromStatus = ssim(mapStatusImageGray, pendingImageGray)
        differenceRemovedFromStatus = ssim(mapStatusImageGray, removedImageGray)
        differenceQualifiedFromStatus = ssim(mapStatusImageGray, qualifiedImageGray)
        print(differenceLovedFromStatus)
        print(differencePendingFromStatus)
        print(differenceQualifiedFromStatus)
        print(differenceRankedFromStatus)
        print(differenceRemovedFromStatus)
        
        if differenceLovedFromStatus != 1 and differenceRankedFromStatus != 1:
            
            pydirectinput.PAUSE = 0.5
            pydirectinput.moveTo(1500, 700)
            pydirectinput.rightClick()
            pydirectinput.moveTo(1500, 400)
            pydirectinput.leftClick()
            pydirectinput.moveTo(1650, 250)
            pydirectinput.leftClick()
            pydirectinput.moveTo(1650, 1150)
            pydirectinput.leftClick()
            pydirectinput.moveTo(1600, 800)
            pydirectinput.PAUSE = 3
                
        pydirectinput.press("right")
        numberOfMapsToProcess-=1

main(4000)