import pytesseract
import pyautogui
import time
import pydirectinput
import datetime

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def main(numOfMaps) -> None:
    mapsDone = 0
    totalTimeInSeconds = 0
    mapLengthList = []
    while(mapsDone != numOfMaps):
        currentTime = pyautogui.screenshot("Images\\beatmapLength.png", region=(120, 75, 81, 35))
        text = pytesseract.image_to_string(currentTime)
        text = text.replace("°", ".").replace(":", ".").replace("O", "0").replace("|", "")
        mapLength = float(text)
        minute = text[0:2]
        seconds = text[3:5]
        minute = int(minute)
        seconds = int(seconds)
        totalTimeInSeconds = totalTimeInSeconds + ((minute * 60) + seconds)
        mapsDone+=1
        print("Maps Done: " + str(mapsDone) + " / " + str(numOfMaps))
        nextBeatmapPixel = pyautogui.pixel(2300,800)
        redValue = nextBeatmapPixel[0]
        if redValue <= 10:
            pydirectinput.press('down')
        else:
            pydirectinput.press('right')
            mapLengthList.append(mapLength)
        time.sleep(.5)
    
    mapLengthList = sorted(mapLengthList)
    medianIndex = int(len(mapLengthList) / 2)
    medianMapLength = mapLengthList[medianIndex]
    medianMapLength = str(medianMapLength).replace(".", ":")
    print("Approx Completion of Collection in Seconds: " + str(totalTimeInSeconds))
    totalTimeInMinutes, secondRemainder = divmod(totalTimeInSeconds, 60)
    print("Approx Completion of Collection in Minutes:Seconds: " + str(totalTimeInMinutes) + ":" + str(secondRemainder))
    totalTimeInHours, minuteRemainder = divmod(totalTimeInMinutes, 60)
    print("Approx Completion of Collection in Hours:Minutes:Seconds: " + str(totalTimeInHours) + ":" + str(minuteRemainder) + ":" + str(secondRemainder))
    meanTimeMinute, meanSecondRemainder = divmod(int(totalTimeInSeconds)/28, 60)
    print("Approx Mean Map Length in minutes: " + str(int(meanTimeMinute)) + ":" + str(int(meanSecondRemainder)))
    print("Median Map Length: " + medianMapLength)
if __name__ == "__main__":
    time.sleep(3)
    main(28)