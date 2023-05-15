# -- coding: utf-8 --
"""
Created on Thu Apr 20 13:21:23 2023

@author:samuel-Oppong-Peprah
"""
#importing the necessary libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time

#fetch the chrome driver from source location
driver = driver = webdriver.Chrome('/Users/kobby/Desktop/chromedriver')

#/Users/kobby/Desktop/chromedriver_mac64
#fetch the sites to extract from
#We are using instagram site
driver.get('https://www.instagram.com/')

time.sleep(2)

#Obtaining the input tag and sending text into input box
#In this case, we providing the username into the input box
username = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('scrapetestwork')

#Obtaining the input tag and sending text into input box
#In this case, we providing the password into the input box
password =  driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('22cuma@ASU')

#grabbing the login button and actioning the click function
login_button = driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button')
login_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id,"mount")]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[1]/div/div')))

#grabbing the search button and actioning the click function
search_button = driver.find_element('xpath', '//*[contains(@id,"mount")]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[1]/div/div')
search_button.click()

# Business category variable that saves the search word
business_category = 'cosmetics gh'

##Obtaining the search input tag and sending text into input box
#In this case, we providing the type of business category into the input box
search = driver.find_element('xpath', '//*[contains(@id,"mount")]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/input')
search.send_keys(business_category)
time.sleep(2)

#Obtainig the source page using beautiful soup
soup = BeautifulSoup(driver.page_source)

#obtaining all search results 
search_results = soup.find_all('div', {'role':'none'})

#counting the number of search results

search_count = len(search_results)


#df  = pd.DataFrame({'business_name':[''], 'ig_username':[''], 'bio-link':[''], 'img':['']})

df = pd.DataFrame(columns=['business_name', 'ig_username', 'bio-link', 'img'])

#looping throup the search results and obtaining the relevant data
for result in search_results:
    
    link = result.find('a', class_='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm').get('href')
    full_link = 'https://www.instagram.com/'+link
    business_name = result.find('span', class_='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft').text
    try:
        ig_username = result.find('span', class_='x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj').text
        img_link = result.find('img', class_='x6umtig x1b1mbwd xaqea5y xav7gou xk390pu x5yr21d xpdipgo xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x11njtxf xh8yej3').get('src')
    except:
        pass
    
    
    
    new_row = {'business_name': business_name,
               'ig_username': ig_username,
               'bio-link': full_link,
               'img': img_link}
    
    
    
    df.loc[len(df)] = new_row


    #df = df.add({'business_name':business_name, 'ig_username':ig_username, 'bio-link':full_link, 'img':img_link })
    
    

#saving data to a csv file
df.to_csv('/Users/Kobby/Desktop/ig_business.csv')

