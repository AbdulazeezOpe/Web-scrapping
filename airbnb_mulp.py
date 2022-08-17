import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.com/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&date_picker_type=calendar&checkin=2022-08-14&checkout=2022-09-05&source=structured_search_input_header&search_type=autocomplete_click'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

df = pd.DataFrame({'Title': [''], 'Links': [''], 'Detail':[''], 'Price':[''], 'Ratings':['']})

while True:
    
    postings = soup.find_all('div', 'c4mnd7m dir dir-ltr')
    for post in postings:
        try:
            link = 'https://www.airbnb.com'+post.find('a', class_= 'ln2bl2p dir dir-ltr').get('href')
            price = post.find('span', class_= 'a8jt5op dir dir-ltr').text
            title = post.find('div', class_= 't1jojoys dir dir-ltr').text
            rating = post.find('span', class_= 'ru0q88m dir dir-ltr').text
            Details = post.find('div', class_= 'f15liw5s s1cjsi4j dir dir-ltr').text
            df = df.append({'Title': title, 'Links': link, 'Detail':Details, 'Price':price, 'Ratings':rating}, ignore_index=True)
        
        except:
            pass
    
    next_page = soup.find('a', {'aria-label': 'Next'}).get('href')
    next_pagefull = 'https://www.airbnb.com' + next_page
        
    url = next_pagefull
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
 
       
     df.to_csv('C:/Users/AZ/Desktop/Projects/air.csv')    
   