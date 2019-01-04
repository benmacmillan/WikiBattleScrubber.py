# Wiki Battle Scraper - Command line 
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
from argparse import ArgumentParser
# ----------------------------------------------------------------------------
# Parsing
parser = ArgumentParser(description='Pull battle details from wikipedia')
parser.add_argument('-url', type=str, help='Usage: -url followed by page URL')
args = vars(parser.parse_args())

# Soup
url = args['url']
battle = requests.get(url).text
soup = BeautifulSoup(battle, 'lxml')

# Information to scrape
name = soup.find("h1", {"class": "firstHeading"})
date = soup.find(text="Date").findNext('td')
location = soup.find(text="Location").findNext('td')
result = soup.find(text="Result").findNext('td')

#Put information into a table, set the output file name.
table = [["Name", name.text], ["Date", date.text], ["Result", result.text]]
fileName = (name.text)

# Display in console
print (tabulate(table))

# Write to file
outfile = open(fileName + ".txt", "w")
outfile.write(tabulate(table))
