import pytesseract
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def main(numOfMaps) -> None:
    mapsDone = 0
    while(mapsDone != numOfMaps):
        currentTime = pyautogui.screenshot("Images\\beatmapLength.png", region=(120, 75, 75, 35))
        text = pytesseract.image_to_string(currentTime)
        print(text)
        mapsDone+=1
        
if __name__ == "__main__":
    main(1)