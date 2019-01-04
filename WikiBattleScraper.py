# Wiki Battle Scraper - Script
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
# ----------------------------------------------------------------------------
# Prepare a tasty and beautiful soup to scrape:
battle = requests.get('https://en.wikipedia.org/wiki/Battle_of_Waterloo').text
soup = BeautifulSoup(battle, 'lxml')

# Pull information from side bar:
name = soup.find("h1", {"class": "firstHeading"})
date = soup.find(text="Date").findNext('td')
location = soup.find(text="Location").findNext('td')
result = soup.find(text="Result").findNext('td')

#Put information into a table, set the output file name.
table = [["Name", name.text], ["Date", date.text], ["Result", result.text]]
fileName = (name.text)

# Show to user in console
print (tabulate(table))

# write details to file
outfile = open(fileName + ".txt", "w")
outfile.write(tabulate(table))
