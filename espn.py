import ssl
import urllib.request
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# List of available leagues in ESPN database
leagues = ["nfl", "nba", "mlb", "nhl", "ncf", "ncb"]

for league in leagues:
    url = f"http://www.espn.com/{league}/bottomline/scores"
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'lxml')
    x = urllib.parse.unquote(str(soup))
    # print(x)
    x = x.split("&amp")
    for i in range(1,50):
        if f"left{i}" in str(x):
            left = [s.split("=")[1] for s in x if f"left{i}=" in s]
            right = [s.split("=")[1] for s in x if f"right{i}_" in s]
            right = right[:-1]
            link = [s.split(f"url{i}=")[1] for s in x if f"url{i}=" in s]
            print(link)
            gameId = link[0].split("gameId=")[-1]
            
            recap = f"https://www.espn.com/{league}/recap/_/gameId/{gameId}"
            # print(recap)
            try:
                html = urllib.request.urlopen(recap, context=ctx).read()
                soup = BeautifulSoup(html,'lxml')
                title = soup.find("header", {"class": ["article-header", "Story__Header"]})
                title = title.find("h1")
                u = title.string
            except:
                pass
                try:
                    recap = f"https://www.espn.com/{league}/game/_/gameId/{gameId}"
                    html = urllib.request.urlopen(recap, context=ctx).read()
                    soup = BeautifulSoup(html,'lxml')
                    title = soup.find("header", {"class": "top-stories__story-header"})
                    title = title.find("h1")
                    u = title.string
                except:
                    u = "Not found"
                    pass
            print(left,right,u)
            


