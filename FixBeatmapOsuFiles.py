import pyautogui
import time
import pyperclip

fileStopper = "2225895"
defaultBeatmapString = "https://osu.ppy.sh/beatmapsets/"

def main():
    fileBeatmap = ""
    pyautogui.moveTo(550, 120)
    pyautogui.leftClick()
    while (True):
        pyautogui.press('enter')
        pyautogui.moveTo(120, 60)
        pyautogui.leftClick()
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        filePath = pyperclip.paste()
        fileArray = filePath.split("\\")
        fileBeatmap = fileArray[7]
        fileBeatmap = fileBeatmap.split(" ")
        if fileBeatmap[0] == fileStopper:
            break
        elif len(fileBeatmap) > 1:
            pass
        else:
            fixBeatmapFile(fileBeatmap[0])
        pyautogui.moveTo(15, 60)
        pyautogui.leftClick()
        pyautogui.press('down')
        
def fixBeatmapFile(beatmapID):
    #go to osu and delete beatmap
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    #wait and see how many presses to get to web
    pyautogui.hotkey('ctrl', 't')
    beatmapURL = defaultBeatmapString + str(beatmapID)
    pyautogui.typewrite(beatmapURL)
    pyautogui.press('enter')
    pyautogui.moveTo(900, 605)
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    time.sleep(10)
    #wait and see how many presses to get to file explorer

if __name__ == "__main__": 
    time.sleep(30)
    pyautogui.PAUSE = 0.5
    main()