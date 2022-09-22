# Opp
Code to rank non profits at https://sprawozdaniaopp.niw.gov.pl/

Scrap the page for .pdfs (done 10.09.2022) -> get the relevant data from the .pdf -> save the relevant data in a new file -> publish the information as interactive chart/table

Scrapper:
I use Selenium for that. File web_scrapper.py scrapes the website and downloads 3 earliest statements from every nonprofits that published at least 3 statements.     
If a nonprofit published only 2 statements, you guessed it - it will download just 2. Only 1 statement published? Only 1 will be downloaded.       
If there are no statements published, name of the nonprofit will be stored in a file for a later analysis.
