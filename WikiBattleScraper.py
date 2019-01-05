# Wiki Battle Scraper - URL Text
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup

infoTable = []
bibTable = []
headers = ['Name', 'Date', 'Location', 'Result']
urls = open("data/URL.txt").read().splitlines()

for index in range(len(urls)):
    # Prepare a tasty and beautiful soup to scrape:
    battle = requests.get(urls[index]).text
    soup = BeautifulSoup(battle, 'lxml')
    # Pull information from side bar:
    name = soup.find("h1", {"class": "firstHeading"})
    date = soup.find(text="Date").findNext('td')
    location = soup.find(text="Location").findNext('td')
    result = soup.find(text="Result").findNext('td')
    # Combine information and append to table
    battleInfo = [name.text, date.text, location.text, result.text]
    infoTable.append(battleInfo)
   
# Show in console
print(tabulate(infoTable, headers))

# Save table to file
infoFile = open("data/WBS_Exported" + ".txt", "w")
infoFile.write(tabulate(infoTable, headers))
infoFile.close