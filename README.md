# Opp
Create a ranking of nonprofits listed at https://sprawozdaniaopp.niw.gov.pl/

Scrap the page for .pdfs (done on 50 files on 10.09.2022) There is around 40 thousand files that I will need to download

Scrap the page for .pdfs:
I use Selenium for that. File web_scrapper.py scrapes the website and downloads 3 earliest statements from every nonprofits that published at least 3 statements. If there is less than 3 statements, it downloads them. If there is no statement, Selenium does not download anything, but the name of the nonprofit is added to the list.


Make the .pdfs readable and gather interesting data:
There is a tool called ocrmypdf, which converts the .pdf into image, and feeds that into the Tesseract OCR engine. After trial and error, I decided to try OCR tool, since .pdf reading libraries could not deal with files that I am handling (encoding errors/tables/Polish language). ocrmypdf does a great job, I will only need to verify if the result is 100% the same as the original.

There are little mistakes with the location of the text within the string - that can be fixed with regular expressions. I would give it 99.9% accuracy.
