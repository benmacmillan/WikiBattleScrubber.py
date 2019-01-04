# Wiki Battle Scraper - URL Text
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup

table = []
headers = ['Name', 'Date', 'Location', 'Result']
urls = open("urls.txt").read().splitlines()

for index in range(len(urls)):
    # Prepare a tasty and beautiful soup to scrape:
    battle = requests.get(urls[index]).text
    soup = BeautifulSoup(battle, 'lxml')

    # Pull information from side bar:
    name = soup.find("h1", {"class": "firstHeading"})
    date = soup.find(text="Date").findNext('td')
    location = soup.find(text="Location").findNext('td')
    result = soup.find(text="Result").findNext('td')

    column = [name.text, date.text, location.text, result.text]
    table.append(column)

print(tabulate(table, headers))

outputFile = open("Battles" + ".txt", "w")
outputFile.write(tabulate(table, headers))
outputFile.close


  