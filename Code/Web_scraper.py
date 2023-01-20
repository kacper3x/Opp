# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t


def selenium_process():
    # selenium configuration
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('disable-notifications')
    chrome_options.add_argument("window-size=1280,720")
    prefs = {'download.default_directory' : 'C:\Selenium\kek'}          # where you want the files to be saved?
    chrome_options.add_experimental_option('prefs', prefs)
    webdriver_service = Service("C:\Selenium\chromedriver.exe")         ## path to where you saved chromedriver.exe   
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    wait = WebDriverWait(browser, 20)   # you can wait for less if 20 seconds is too long for you
    url = 'https://sprawozdaniaopp.niw.gov.pl/'
    browser.get(url)
    wait.until(EC.element_to_be_clickable((By.ID, "btnsearch"))).click()
    links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='dialog']")))
    # function variables                                                
    org_counter = 0
    unregistered_orgs = []
    time_for_100_orgs = 0                                               # I tract the time on every 50th iteration of the function to check if the program gets slower as it goes. 
    time_for_all_process = [] 
    # start of looping through links
    for link in range(len(links)):                 
        time_start = t.time()
        links[org_counter].click()   
        #print('clicked link', links[link].text)  
        try:
            statement = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Sprawozdanie merytoryczne")))
            for i in range(len(statement)):
                statement[i].click()
        # If the organisation does not have any statements to download, its name is saved to a variable
        except:
            #print("Nonprofit has no statements")
            unregistered_orgs.append(str(links[org_counter].text))
        t.sleep(2)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[class="ui-icon ui-icon-closethick"]')))[org_counter].click()
        print(f'closed the popup {org_counter+1} of {len(links)}')
        org_counter += 1
        time_end = t.time()
        time_for_100_orgs += time_end-time_start
        # every 100 organizations,  would like to save the data about my progress (how long it takes and orgs with no statement) and restart the selenium browser
        # I noticed that selenium gets slower the longer its opened, so I am restrating it every nth iteration
        if org_counter % 100 == 0:
            # saving the time it takes to process 100 orgs.
            time_for_all_process.append(int(time_for_100_orgs))
            with open("czasomierz.txt", "a") as file:
                file.writelines(str(time_for_100_orgs))
                file.writelines(("\n"))
            time_for_100_orgs = 0
            # saving names of orgs with no statement
            with open("nie działa.txt", "a") as file:
                for i in unregistered_orgs:
                    file.writelines(str(i))
                    file.writelines(("\n"))
                unregistered_orgs.clear()
            # restart the browser and the scraping process
            browser.quit()
            print("quitted the selenium_process()")
            if org_counter != len(links):
                print("started the selenium_process()")
                selenium_process()                         
            else:
                print("Finished successfully!")
                with open("czasomierz.txt", "a") as file:
                    file.writelines(str(time_for_all_process))
    print("To już jest naprawdę koniec :) Udało Ci się Kacper - skończyłeś pętle :)")

selenium_process()
