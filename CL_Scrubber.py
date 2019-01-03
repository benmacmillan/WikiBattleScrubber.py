#Take a wikipedia URL for a battle and then output a file with the name, date and results of the battle.
import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser
#----------------------------------------------------------------------------
#Enable parsing through command line, prepare the soup. 
parser = ArgumentParser(description='Pull battle details from wikipedia')
parser.add_argument('-url', type=str, help='Usage: -url followed by the wiki URL you wish to use')
args = vars(parser.parse_args())
url = args['url']
battle = requests.get(url).text
soup = BeautifulSoup(battle,'lxml')

#Pull information from the battles side bar:
Name = soup.find("h1", {"class":"firstHeading"})
Date = soup.find(text="Date").findNext('td')
Location = soup.find(text="Location").findNext('td')
Result = soup.find(text="Result").findNext('td')
FileName = (Name.text)

#Show to user and save in a text file:
print (Name.text)
print (Date.text)
print (Result.text)

#write the details to a text file
outfile = open(FileName + ".txt","w")
outfile.write(Name.text + '\n' + Date.text + '\n' + Result.text)
