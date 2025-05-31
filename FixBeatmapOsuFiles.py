import pyautogui
import time
import pyperclip

#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440
#Have it so tabs start with file explorer, then google chrome from left to right, osu must still be open but the first two tabs are file and chrome
#Last Ran on Date: 05/27/2025
#Date of Next Run: 06/27/2025
#Run every month

#Just need to account for deleted beatmaps/page missing on bancho

fileStopper = "2027968 "
defaultBeatmapString = "https://osu.ppy.sh/beatmapsets/"

def main():
    fileBeatmap = ""
    y_cord = 120
    while (True):
        if y_cord > 1360:
            y_cord = 120
            pyautogui.press('down', presses=61)
            pyautogui.moveTo(550, y_cord)
            pyautogui.leftClick()
            pyautogui.press('up')
            time.sleep(2)
        pyautogui.moveTo(550, y_cord)
        pyautogui.leftClick()
        pyautogui.hotkey('alt', 'enter')
        locFile = pyautogui.locateOnScreen("Images\\fileNameFinder.png")
        pyautogui.moveTo(locFile[0]+20, locFile[1]-30)
        pyautogui.leftClick()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        fileBeatmap = pyperclip.paste()
        pyautogui.hotkey('alt', 'f4')
        fileBeatmap = fileBeatmap.split(" ")
        if fileBeatmap[0] == fileStopper:
            break
        elif len(fileBeatmap) > 1:
            y_cord+=21
        else:
            pyautogui.press('del')
            pyautogui.hotkey('ctrl', 'alt', 'tab')
            pyautogui.press('enter')
            fixBeatmapFile(fileBeatmap[0])
        
        
def fixBeatmapFile(beatmapID):
    pyautogui.hotkey('ctrl', 't')
    beatmapURL = defaultBeatmapString + beatmapID
    pyautogui.typewrite(beatmapURL)
    pyautogui.press('enter')
    websiteLoad = 0
    while websiteLoad < 120:
        pixel = pyautogui.pixel(200,200)
        if pixel == (31, 41, 46):
            break
        else:
            websiteLoad+=1
        time.sleep(.25)
    time.sleep(.25)
    if websiteLoad == 120:
        raise pyautogui.PyAutoGUIException #website loaded to slow
    try:
        locDownload = pyautogui.locateCenterOnScreen("Images\\Download.png")
    except pyautogui.ImageNotFoundException: #means the beatmap has video
        try:
            locDownload = pyautogui.locateCenterOnScreen("images\\downloadVideo.png")
        except:
            raise pyautogui.ImageNotFoundException #means it couldnt find beatmap download button, should never happen
    pyautogui.moveTo(locDownload[0], locDownload[1])
    pyautogui.leftClick()
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
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    pyautogui.press('enter')

if __name__ == "__main__":
    time.sleep(10)
    pyautogui.PAUSE = 0.5
    main()