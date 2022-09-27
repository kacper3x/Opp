# Opp
Code to rank non profits at https://sprawozdaniaopp.niw.gov.pl/

Scrap the page for .pdfs (done 10.09.2022) -> get the relevant data from the .pdf -> save the relevant data in a new file -> publish the information as interactive chart/table

Scrap the page for .pdfs:
I use Selenium for that. File web_scrapper.py scrapes the website and downloads 3 earliest statements from every nonprofits that published at least 3 statements.     
If a nonprofit published only 2 statements, you guessed it - it will download just 2. Only 1 statement published? Only 1 will be downloaded.       
If there are no statements published, name of the nonprofit will be stored in a file for a later analysis.


Make the .pdfs readable and gather interesting data:
There is a tool called ocrmypdf, which converts the .pdf into image, and feeds that into the Tesseract OCR engine. After trial and error, I decided to try OCR tool, since .pdf reading libraries could not deal with files that I am handling (encoding errors/tables/Polish language). ocrmypdf does a great job, I will only need to verify if the result is 100% the same as the original.
