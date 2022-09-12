from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time as t

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument("download.default_directory=D:\Pobieranie\Opp")
chrome_options.add_argument("window-size=1280,720")

prefs = {'download.default_directory' : 'D:\Pobieranie\Opp'}         # where you want the files to be saved?
chrome_options.add_experimental_option('prefs', prefs)

webdriver_service = Service("D:\SeleniumDriver\chromedriver.exe")   ## path to where you saved chromedriver.exe

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
wait = WebDriverWait(browser, 20)   # you can wait for less if 20 seconds is too long for you
url = 'https://sprawozdaniaopp.niw.gov.pl/'
browser.get(url)
wait.until(EC.element_to_be_clickable((By.ID, "btnsearch"))).click()
links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[class='dialog']")))
counter = 0
unregistered_orgs = []

for link in links[:50]:             # starting with 50 first links, you can remove the limitation
    link.click()
    print('clicked link', link.text)
    try:
        statement = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Sprawozdanie merytoryczne")))
        for i in range(len(statement)):
            statement[i].click()
            if i == 2:
                break
    except:
        print("No such org in the system")
        unregistered_orgs += link.text
    t.sleep(1)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[class="ui-icon ui-icon-closethick"]')))[counter].click()
    print('closed the popup')
    counter += 1
    
# saves the list of orgs with no statement
with open("nie działa.txt", "w") as file:
    file.write(str(unregistered_orgs))
    


