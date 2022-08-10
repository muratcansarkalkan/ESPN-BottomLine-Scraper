# ESPN-BottomLine-Scraper
Simple scraper written in Python to get scores from ESPN bottomline<br>
It can scrape the box scores, major stats, cautionary print for game links and headlines for the games, if available.</br>

<h3>Prerequisites</h3>
<ul>
  <li>Latest Python version, I guess</li>
  <li>BeautifulSoup 4</li>
</ul>
<h3>Changelog:</h3>
<ul>
  <li>2015: Initial commit.</li>
  <li>04/18/2022: Remade the script with 2022 standards</li>
  <li>04/18/2022: Now the script prints header, content, and title if it's available.</li>
  <li>04/19/2022: Script for top headlines available.</li>
  <li>04/19/2022: Fixed bug with top headlines. Now some links are printed multiple times but after implementation of JSON output they will be fixed.</li>
  <li>04/21/2022: Now the livescores and headlines are stored as objects, also news are stored only once.</li>
</ul>
</ul>

<h3>How it works:</h3>
<ul>
  <li>Run espn.py from anywhere you want.</li>
</ul>

<h3>Future:</h3>
<ul>
  <li>Use of APIs instead of BS4</li>
  <li>A web application that can be included in bottom of a webpage</li>
  <li>A GUI.</li>
</ul>
