# Parses top headlines of last 2 days.
import ssl
import urllib.request
from bs4 import BeautifulSoup
from datetime import date, timedelta
from contents import Headline

today = date.today()
yesterday = date.today() - timedelta(days=1)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# list of leagues to be tracked
# leagues = ["soccer"]
leagues = ["nfl","nba","nhl","mlb","golf","soccer"]
leaguedict = {"nfl": "NFL", "nba": "NBA", "mlb": "MLB", "nhl": "NHL", "ncf": "NCAAF", "ncb": "NCAAB", "golf": "GOLF", "soccer": "SOCCER"}

# Little parsing function
def parse(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'lxml')
    return soup

# for recaps
for league in leagues:
    l = leaguedict.get(league)
    links = []
    url = f"https://www.espn.com/{league}/"
    soup = parse(url)
    containers = soup.find_all("section", {"class": ["headlineStack__listContainer"]})
    # Finds headline container
    for container in containers:
        u = container.find_all("a")
        for title in u:
            # Gets links for headlines
            if "https://" not in title['href']:
                link = "https://www.espn.com"+title["href"]
            else:
                link = title['href']
            if link not in links:
                links.append(link)
                soup = parse(link)
            # Checks if it has a date at header
                try:
                    date2 = soup.find("meta", {"name":"DC.date.issued"})['content']
                    if date2[0:10] == str(today) or date2[0:10] == str(yesterday):
                            headline = Headline(l, title.get_text(), link)
                            print(headline.__dict__)
                    else:
                        continue
                except:
                    continue
            else:
                continue

    # title = title.find("h1")
