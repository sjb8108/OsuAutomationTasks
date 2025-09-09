import pydirectinput
import pyautogui
import time
#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE OFF
#Fully Ran on Date: 9/1/2025
#Should Run Next on Date: 12/1/2025
#Goal: Combine MovePendingAndDeletedBeatmaps.py into here

def main(numberOfMapsToProcess):
    pydirectinput.moveTo(1000, 600)
    while numberOfMapsToProcess > 0:
        print("Maps left to process: "+ str(numberOfMapsToProcess))
        timeSpent = 0
        while timeSpent < 2:
            pixel = pyautogui.pixel(35,35)
            if pixel == (252, 252, 252) or pixel == (255, 255, 255):
                pydirectinput.moveTo(1500, 700)
                pydirectinput.rightClick()
                pydirectinput.moveTo(1500, 400)
                pydirectinput.leftClick()
                pydirectinput.moveTo(1650, 250)
                pydirectinput.leftClick()
                pydirectinput.moveTo(1650, 1150)
                pydirectinput.leftClick()
                pydirectinput.moveTo(1600, 800)
                break
            else:
                try:
                    pyautogui.locateCenterOnScreen("Images\\RemovedV2.png")
                    pydirectinput.moveTo(1500, 700)
                    pydirectinput.rightClick()
                    pydirectinput.moveTo(1500, 400)
                    pydirectinput.leftClick()
                    pydirectinput.moveTo(1650, 250)
                    pydirectinput.leftClick()
                    pydirectinput.moveTo(1650, 1150)
                    pydirectinput.leftClick()
                    pydirectinput.moveTo(1600, 800)
                    break
                except pyautogui.ImageNotFoundException:
                    pydirectinput.moveTo(300, 250)
                    pydirectinput.leftClick()
                    pydirectinput.moveTo(300, 400)
                    pydirectinput.leftClick()
                    time.sleep(1)
                    timeSpent+=1
                
        pydirectinput.press("right")
        numberOfMapsToProcess-=1

if __name__ == "__main__":
    time.sleep(30)
    pydirectinput.PAUSE = .5
    main(1900)