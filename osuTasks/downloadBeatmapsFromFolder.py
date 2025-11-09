import pyautogui
import time
import os
import key

BASE_DIR = key.BASE_DIRECTORY

def main():
    allBeatmaps = []
    resumeFrom = ""
    with open(os.path.join(BASE_DIR, "textFiles", "changedSR.txt"), "r") as myfile:
        for map in myfile:
            allBeatmaps.append(map)
    currentIndex = 1
    resume = "221870"
    for beatmap in allBeatmaps:
        print("Downloading " + str(beatmap))
        print("Currently at index " + str(currentIndex) + " / " + str(len(allBeatmaps)))
        beatmapID = beatmap.split(".")[0]
        if int(resume) > int(beatmapID):
            currentIndex += 1
            continue
        pyautogui.moveTo(900,300)
        pyautogui.leftClick()
        pyautogui.write(beatmapID)
        pyautogui.press('enter')
        pageLoad = 0
        pageError = True
        nonStdBeatmap = False
        while pageLoad != 120:
            try:
                pageComplete = pyautogui.locateCenterOnScreen("Images\\banchoIconStd.png", confidence=0.85)
                pageError = False
                break
            except:
                try:
                    pageComplete = pyautogui.locateCenterOnScreen("Images\\banchoBeatmapError.png", confidence=0.95)
                    nonStdBeatmap = True
                except:
                    pageLoad+=1
            time.sleep(.25)
        if nonStdBeatmap:
            continue
        if pageError:
            raise Exception("Osu Beatmap Page Did Not Load")
        pyautogui.moveTo(1250, 615)
        pyautogui.leftClick()
        downloadCounter = 0
        downloadError = True
        while downloadCounter != 120:
            try:
                downloadComplete = pyautogui.locateCenterOnScreen("Images\\downloadComplete.png")
                pyautogui.moveTo(downloadComplete[0], downloadComplete[1])
                pyautogui.leftClick()
                pyautogui.leftClick()
                downloadError = False
                break
            except:
                downloadCounter+=1
                time.sleep(.25)
        if downloadError:
            raise Exception("Beatmap Downloaded Too Slowly")
        pyautogui.moveTo(900,300)
        pyautogui.leftClick()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        currentIndex+=1
        
if __name__ == "__main__":
    #time.sleep(10)
    pyautogui.PAUSE = 0.5
    main()