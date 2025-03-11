import pydirectinput
import time
#FOR THE TIME OSU MUST HAVE THE SETTING FULL SCREEN MODE OFF
#Any moveTo cords are specifically used for my montior resolution which is 2560 x 1440

def main(NumberOfBeatmaps):
    time.sleep(3) #Time to put cursour on osu
    while NumberOfBeatmaps > 0:
        print(NumberOfBeatmaps)
        pydirectinput.moveTo(1500, 700)
        pydirectinput.rightClick()
        pydirectinput.moveTo(1500, 400)
        pydirectinput.leftClick()
        pydirectinput.moveTo(1800, 750) #Both/Other
        pydirectinput.leftClick()
        pydirectinput.moveTo(1800, 830) #Jump
        pydirectinput.leftClick()
        pydirectinput.moveTo(1800, 870) #Stream
        pydirectinput.leftClick()
        pydirectinput.moveTo(1800, 920) #PutInCollection
        pydirectinput.leftClick()
        pydirectinput.moveTo(1650, 1150)
        pydirectinput.leftClick()
        pydirectinput.press('right')
        NumberOfBeatmaps-=1
   
pydirectinput.PAUSE = 0.25     
main(262)