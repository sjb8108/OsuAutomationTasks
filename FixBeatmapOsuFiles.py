import pyautogui
import pydirectinput
import time
import pyperclip
import numpy as np
from skimage.metrics import structural_similarity as ssim
import cv2

fileStopper = "2225895 Caravan Palace - Lone Digger"

def main():
    fileBeatmap = ""
    pyautogui.moveTo(550, 120)
    pyautogui.leftClick()
    while (fileBeatmap != fileStopper):
        pyautogui.press('enter')
        pyautogui.moveTo(120, 60)
        pyautogui.leftClick()
        pyautogui.hotkey('ctrl', 'c')
        filePath = pyperclip.paste()
        fileArray = filePath.split("\\")
        fileBeatmap = fileArray[len(fileArray)-1]
        print(fileBeatmap)
        break
    
def fixBeatmapFile(fileArray):
    print()

if __name__ == "__main__": 
    time.sleep(5)
    pyautogui.PAUSE = 0.4 #I know .5 works
    main()