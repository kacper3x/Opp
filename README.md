# Opp
Create a ranking of nonprofits listed at https://sprawozdaniaopp.niw.gov.pl/
There is around 96 thousand files, I would like to combine those into 1 file with clear structure accessible at (ADD HERE ULR ADDRESS). 

1. Scrap the webpage for the .pfds to download
2. Extract text from .pdfs using OCR tool
3. Analyze and clense the text looking for interesting values
4. Publish the result on the internet (20.10 still need to prepare the page) (24.01 on page, but hosted excel file with first iteration on pomocfundacji.com)

1). Scrap the page for .pdfs (done on 50 files on 10.09.2022). The data is there free of charge, but is unorganised. Data is held in yearly statements of nonprofit. Considering there is around 13 500 nonprofits registered on the page I think there is around 40 thousand files that I will need to download - some of the nonprofits did not publish any files.
I use Selenium for that. File web_scrapper.py scrapes the website and downloads 3 earliest statements from every nonprofits. If there is less than 3 statements, it downloads them. If there is no statement, Selenium does not download anything, but the name of the nonprofit is written to the persistant list.

2). Make the .pdfs into .txt format.
There is a tool called OCRmyPDF, which converts the .pdf into image, and feeds that into the Tesseract OCR engine. After trial and error, I decided to try OCR tool, since .pdf reading libraries could not deal with files that I am handling (encoding errors were the major issues, although my .pdfs also had inconvences like tables and Polish language special characters). OCRmyPDF does a great job, meaning it is able to OCR .pdf to .txt file.

3). Analyze the text and cleanse the values that are interesting.
Even with the top OCR tool available on the market, there are little mistakes with the location of the text within the string. In some files, some part of the text within the .pdf will not be recognized as having characters, and therefore will not be extracted into .txt file. Sometimes slightly different name of the nonprofit will be given, when those two are in fact for the same organisation. In some files there will be different word order in the string that has the interesting data, or unnecessary sentence will be thrown into it.
Initially I wanted to deal with that using REGEX, and after 1 week of not getting the results I wanted I decided to try a different approach. It must be noted that it was my first time with trying out REGEX, perhaps if I was using that earlier I would be able to get the results I wanted. With Python built in functions for string manipulation I managed to specify the interesting strings, and extract the interesting data out of them. 

4). Publish the result on the Internet
Program is writing the data into Excel file. Then Excel file is formatted and made good looking and intuitive to use. Excel file is shared via OneDrive on a page. All disclarimers are in place. Page can be accessed via public URL, it is a WordPress page (ADD HERE ULR ADDRESS).
