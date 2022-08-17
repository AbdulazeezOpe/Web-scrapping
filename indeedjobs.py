from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

driver =webdriver.Chrome('C:/Users/AZ/Desktop/Projects/Selenium/chromedriver_win32/chromedriver.exe')



driver.get('https://www.indeed.jobs/')
time.sleep(2)

job = driver.find_element(By.XPATH, '//*[@id="keyword-field"]')
job.send_keys('Data Analyst')
location = driver.find_element(By.XPATH, '//*[@id="location-field"]')
location.send_keys('Los Angeles')
button = driver.find_element(By.XPATH, '//*[@id="jobs-search"]/div/button')
button.click()
time.sleep(2)

df = pd.DataFrame({'Position': [''], 'Link':[''], 'Department':[''],'Location': [''], 'Remote':['']})
for x in range(1,7):
    next_pg = f'https://search.indeed.jobs/main/jobs?keywords=Data%20analyst&location=Los%20Angeles&stretch=10&stretchUnit=MILES&sortBy=relevance&page={x}'
    driver.get(next_pg)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    Job_av = soup.find_all(class_= 'mat-expansion-panel ng-tns-c73-18 search-result-item ng-star-inserted')
    
    for job in Job_av:
        link = 'https://search.indeed.jobs' + job.find('a').get('href')
        name = job.find('a').text
        Department = job.find('span', class_= 'categories label-value').text
        location = job.find('span', class_= 'label-value location_name').text
        Remote = job.find('span', class_= 'label-value tags5').text
        
        df = df.append({'Position': name, 'Link':link, 'Department': Department,'Location': location, 'Remote':Remote}, ignore_index= True)

    


