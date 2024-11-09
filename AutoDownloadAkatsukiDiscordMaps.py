import pyautogui
import pydirectinput
import time
import pyperclip
#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE ON
#Next step is to make it so it skips taiko, mania, and ctb by looking at the icon instead of downloading the map and such

def main(mapNumber):
    downloadNumberOfMaps = mapNumber
    downloadedMaps = 0
    while downloadedMaps < downloadNumberOfMaps:
        pyautogui.PAUSE = 0.5
        pixelColor = pyautogui.pixel(770, 1200)
        if pixelColor == (43, 45, 49):
            pyautogui.moveTo(435, 1115)
        else:
            pyautogui.moveTo(430, 972)
        pyautogui.leftClick()
        downloadBeatmapTracker()
        pyautogui.hotkey('ctrl', 'alt', 'tab')
        pyautogui.PAUSE = 2
        if downloadedMaps == 0:
            pyautogui.press('right', presses=1)
        else:
            pyautogui.press('right')
        pyautogui.PAUSE = 0.5
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
    
if __name__ == "__main__": 
    time.sleep(30)
    main(54) #paramter set manually by user, have discord open, google tab open that isnt blank, osu with date added as caterogry and osu is muted
    