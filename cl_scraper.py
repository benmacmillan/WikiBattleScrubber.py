#Take a wikipedia URL for a battle and then output a file with the name, date and results of the battle.
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
from argparse import ArgumentParser
#----------------------------------------------------------------------------
#Parsing
parser = ArgumentParser(description='Pull battle details from wikipedia')
parser.add_argument('-url', type=str, help='Usage: -url followed by the wiki URL you wish to use')
args = vars(parser.parse_args())

#Soup
url = args['url']
battle = requests.get(url).text
soup = BeautifulSoup(battle,'lxml')

#Information to scrape
Name = soup.find("h1", {"class":"firstHeading"})
Date = soup.find(text="Date").findNext('td')
Location = soup.find(text="Location").findNext('td')
Result = soup.find(text="Result").findNext('td')
Table = [["Name",Name.text],["Date",Date.text],["Result",Result.text]]
FileName = (Name.text)

#Display in console
print (tabulate(Table))

#Write to file 
outfile = open(FileName + ".txt","w")
outfile.write(tabulate(Table))
