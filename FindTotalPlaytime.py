from bs4 import BeautifulSoup
import requests
url = "https://osu.ppy.sh/beatmapsets/2162554#osu/4746232"
stuff = requests.get(url)
soup = BeautifulSoup(stuff.content, "html5lib")
with open("testFile.txt", "w", encoding="utf-8") as file:
    file.write(str(soup))