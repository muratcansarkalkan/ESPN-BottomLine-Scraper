# Parses top headlines of last 2 days.
import ssl
import urllib.request
from bs4 import BeautifulSoup
from datetime import date, timedelta

today = date.today()
yesterday = date.today() - timedelta(days=1)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# list of leagues to be tracked
# leagues = ["soccer"]
leagues = ["nfl","nba","nhl","mlb","golf","soccer"]

# Little parsing function
def parse(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'lxml')
    return soup

for league in leagues:
    url = f"https://www.espn.com/{league}/"
    soup = parse(url)
    container = soup.find("section", {"class": ["headlineStack__listContainer"]})
    # Finds headline container
    u = container.find_all("a")
    for title in u:
        # Gets links for headlines
        link = "https://www.espn.com"+title["href"]
        soup = parse(link)
        # Checks if it has a date at header
        try:
            date2 = soup.find("meta", {"name":"DC.date.issued"})['content']

            if date2[0:10] == str(today) or date2[0:10] == str(yesterday):
                print(date2[0:10], link, title.get_text())
            else:
                continue
        except:
            continue
        
    # title = title.find("h1")
