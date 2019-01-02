#Take a wikipedia URL for a battle and then output a file with the name, date and results of the battle.

import requests
from bs4 import BeautifulSoup
#----------------------------------------------------------------------------
#Prepare that tasty and beautiful soup to read the web page:
battles_url = requests.get('https://en.wikipedia.org/wiki/Battle_of_Waterloo').text
soup = BeautifulSoup(battles_url,'lxml')



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
outfile.write(Name.text)
