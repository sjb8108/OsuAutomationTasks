import pydirectinput
import time
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE OFF
#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440

def main(NumberOfBeatmaps):
    time.sleep(3) #Time to put cursour on osu
    while NumberOfBeatmaps > 0:
        print(NumberOfBeatmaps)
        pydirectinput.moveTo(1500, 700)
        time.sleep(0.25)
        pydirectinput.rightClick()
        time.sleep(0.25)
        pydirectinput.moveTo(1500, 400)
        time.sleep(0.25)
        pydirectinput.leftClick()
        time.sleep(0.25)
        pydirectinput.moveTo(1800, 750) #Both/Other
        time.sleep(0.25)
        pydirectinput.leftClick()
        time.sleep(0.25)
        pydirectinput.moveTo(1800, 830) #Jump
        time.sleep(0.25)
        pydirectinput.leftClick()
        time.sleep(0.25)
        pydirectinput.moveTo(1800, 870) #Stream
        time.sleep(0.25)
        pydirectinput.leftClick()
        time.sleep(0.25)
        pydirectinput.moveTo(1800, 920) #PutInCollection
        time.sleep(0.25)
        pydirectinput.leftClick()
        time.sleep(0.25)
        pydirectinput.moveTo(1650, 1150)
        time.sleep(0.25)
        pydirectinput.leftClick()
        time.sleep(0.25)
        pydirectinput.press('right')
        time.sleep(0.25)
        NumberOfBeatmaps-=1
        
main(13)