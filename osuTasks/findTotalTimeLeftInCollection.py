import pytesseract
import pyautogui
import time
import pydirectinput

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def main(numOfMaps) -> None:
    mapsDone = 0
    totalTimeInSeconds = 0
    while(mapsDone != numOfMaps):
        currentTime = pyautogui.screenshot("Images\\beatmapLength.png", region=(120, 75, 83, 35))
        text = pytesseract.image_to_string(currentTime)
        minute = text[0:2]
        seconds = text[3:5]
        if "O" in minute:
            minute = minute.replace("O", "0")
        if "O" in seconds:
            seconds = seconds.replace("O", "0")
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
        time.sleep(.5)
        
    print("Approx Completion of Collection in Seconds: " + str(totalTimeInSeconds))
    totalTimeInMinutes = totalTimeInSeconds / 60
    print("Approx Completion of Collection in Minutes: " + str(totalTimeInMinutes))
    totalTimeInHours = totalTimeInMinutes / 60
    print("Approx Completion of Collection in Hours: " + str(totalTimeInHours))
if __name__ == "__main__":
    time.sleep(3)
    main(660) 