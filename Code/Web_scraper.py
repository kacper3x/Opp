# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t

"""Selenium configuration"""
class WebScraper():  

    webdriver_service = Service("C:\Selenium\chromedriver.exe")                          # path to where you saved chromedriver.exe  
    chrome_options = Options()   

    def __init__(self) -> None:
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument('disable-notifications')
        self.chrome_options.add_argument("window-size=1280,720")
        self.prefs = {'download.default_directory' : 'C:\Selenium\some_folder'}          # where you want the files to be saved?
        self.chrome_options.add_experimental_option('prefs', self.prefs) 
        print("Configured new web scraper")

    def start(self) -> list:
        self.browser = webdriver.Chrome(service=self.webdriver_service, options=self.chrome_options)
        self.wait = WebDriverWait(self.browser, 20)   # you can wait for less if 20 seconds is too long for you
        self.url = 'https://sprawozdaniaopp.niw.gov.pl/'
        self.browser.get(self.url)
        self.wait.until(EC.element_to_be_clickable((By.ID, "btnsearch"))).click()
        links = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='dialog']")))
        print("Started new scrapper")
        return links
    
    def quit(self):               # I noticed that selenium gets slower the longer its opened, so I am restrating it every nth iteration
        self.browser.quit()
        print("Quitted the scraper")

"""Function that saves the content to the .txt files for later review"""
def append_to_file(name_of_file, content_to_append):
    with open(name_of_file, "a") as file:
        """I need to check if the argument is a list or int"""
        if type(content_to_append) == list:
            for i in content_to_append:
                file.writelines(str(i))
                file.writelines(("\n"))
            content_to_append.clear()
        if type(content_to_append) == int:
            file.writelines(str(content_to_append))
            file.writelines(("\n"))
            content_to_append = 0


def selenium_process():
    # function variables                                                
    organization_counter = 0                    # This needs to stay on track regardles of opening new instance of Selenium
    close_button_counter = 0                    # One needs to reset this button every time a new instance of Selenium is opened
    unregistered_orgs = []                      # List to track unregistered organizations, for a later review
    time_for_250_orgs = 0                       # I track the progres and reset Selenium for every 250th organizations, change this at will
    time_for_all_process = []                   # List with every single time_for_250_orgs
    # start the scraper
    Scraper = WebScraper()
    links = WebScraper.start(WebScraper)
    # start of looping through links
    for link in range(len(links)):                 
        time_start = t.time()
        links[organization_counter].click()   
        #print('clicked link', links[link].text)  
        try:
            statement = Scraper.wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Sprawozdanie merytoryczne")))
            for i in range(len(statement)):
                statement[i].click()
        # If the organisation does not have any statements to download, its name is saved to a variable
        except:
            #print("Nonprofit has no statements")
            unregistered_orgs.append(str(links[organization_counter].text))
        t.sleep(2)
        Scraper.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[class="ui-icon ui-icon-closethick"]')))[close_button_counter].click()
        print(f'closed the popup {organization_counter+1} of {len(links)}')
        organization_counter += 1
        close_button_counter += 1
        time_end = t.time()
        time_for_250_orgs += time_end-time_start
        if organization_counter % 250 == 0:                 # manipulate this to change how often should Selenium restart 
            time_for_all_process.append(int(time_for_250_orgs))
            append_to_file("czasomierz.txt", time_for_250_orgs)
            append_to_file("nie działa.txt", unregistered_orgs)
            # restart the browser and the scraping process
            t.sleep(30)
            close_button_counter = 0
            Scraper.quit()
            Scraper = WebScraper()
            links = WebScraper.start(WebScraper)
            if organization_counter == len(links):
                print("Finished successfully!")
                append_to_file("czasomierz.txt", time_for_all_process)
    print("To już jest naprawdę koniec :) Udało Ci się Kacper - skończyłeś pętle :)")

if __name__ == '__main__':
    selenium_process()
