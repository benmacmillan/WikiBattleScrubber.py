# Wikipedia Battle Scraper
A basic web scraper that pulls some of the sidebar battle information for historic battle pages on Wikipedia. 
There are currently two versions of the project, the main script which takes URLs from a text file and a command line version which can only do one battle at a time currently. 

- Requires BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/)
- Requires Tabulate (https://pypi.org/project/tabulate/)

## WikiBattleScraper.py
The Main version of the script, place the URLs of wikipedia battles you wish to scrape (one per line) and it will create a table in the battles.txt document. **Some wikipedia battle pages use a non uniform formatting of the sidebar and thus will not currently work - Most should however.** 

## cl_scraper.py
A now less useful version made to run in command line, it only can handle one URL at a time.  
Example: **cl_scraper.py -url https://en.wikipedia.org/wiki/Battle_of_Thymbra**

