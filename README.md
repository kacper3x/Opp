# Opp
Code to rank non profits at https://sprawozdaniaopp.niw.gov.pl/

web_scrapper.py scrapes the website and downloads 3 earliest statements from every nonprofits that published at least 3 statements. 
If a nonprofit published only 2 statements, you guessed it - it will download just 2. Only 1 statement published? Only 1 will be downloaded.
If there are no statements published, name of the nonprofit will be stored in a file for a later analysis.
