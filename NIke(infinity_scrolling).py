from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time


driver =webdriver.Chrome('C:/Users/AZ/Desktop/Projects/Selenium/chromedriver_win32/chromedriver.exe')

driver.get('https://www.nike.com/w/sale-3yaep')

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_ht = driver.execute_script('return document.body.scrollHeight')
    
    if new_ht == last_height:
        break
    last_height = new_ht


soup = BeautifulSoup(driver.page_source, 'lxml')

product_card = soup.find_all('div', class_= 'product-card__body')

df = pd.DataFrame({'Name': [''], 'Link': [''], 'Description': [''], 'Price': [''], 'Sale Price': ['']})

for prod in product_card:
    try:
        link = prod.find('a', class_= 'product-card__link-overlay').get('href')
        name = prod.find('div', class_= 'product-card__title').text
        subt = prod.find('div', class_= 'product-card__subtitle').text
        full_pr = prod.find('div', class_= 'product-price is--striked-out css-0').text
        sale_pr = prod.find('div', class_= 'product-price is--current-price css-1ydfahe').text
        df = df.append({
            'Name': name, 'Link': link, 'Description': subt, 'Price': full_pr, 'Sale Price': sale_pr},
            ignore_index = True)
        
    except:
        pass
    
df.to_csv('C:/Users/AZ/Desktop/Projects/nike.csv')
    
        
        
        
        
        
        