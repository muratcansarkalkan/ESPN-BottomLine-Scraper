import ssl
import urllib.request
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Top headlines
# http://www.espn.com/espn/latestnews
# List of available leagues in ESPN database
# also ncf and ncb included but for now discard
leagues = ["nfl", "nba", "mlb", "nhl", "ncf", "ncb"]
leaguedict = {"nfl": "NFL", "nba": "NBA", "mlb": "MLB", "nhl": "NHL", "ncf": "NCAAF", "ncb": "NCAAB"}

def parse(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'lxml')
    return soup

for league in leagues:
    l = leaguedict.get(league)
    url = f"http://www.espn.com/{league}/bottomline/scores"
    soup = parse(url)
    x = urllib.parse.unquote(str(soup))
    # print(x)
    x = x.split("&amp")
    for i in range(1,25):
        if f"left{i}" in str(x):
            left = [s.split("=")[1] for s in x if f"left{i}=" in s]
            right = [s.split("=")[1] for s in x if f"right{i}_" in s]
            right = right[:-1]
            total = left + right
            link = [s.split(f"url{i}=")[1] for s in x if f"url{i}=" in s]
            if "preview" in link[0]:
                soup = parse(link[0])
            else:
                gameId = link[0].split("gameId=")[-1]
                recap = f"https://www.espn.com/{league}/recap/_/gameId/{gameId}"
                soup = parse(recap)
            
            # print(recap)
            try:
                title = soup.find("header", {"class": ["article-header", "Story__Header"]})
                title = title.find("h1")
                u = title.string
                total.append(u)
                total.insert(0, l)
            except:
                pass
                try:
                    title = soup.find("header", {"class": "top-stories__story-header"})
                    title = title.find("h1")
                    u = title.string
                    total.append(u)
                    total.insert(0, l)
                except:
                    total.insert(0, l)
                    pass

            print(total)