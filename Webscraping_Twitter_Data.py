from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd



driver = webdriver.Chrome('D:/Web Scraping/chromedriver_win32/chromedriver.exe')
driver.get('https:www.google.com')

google_input = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
google_input.send_keys('twitter')
google_input.send_keys(Keys.ENTER)


twitter_input = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')

username = 'twitter_username'
password = 'twitter_password'

twitter_input.send_keys(username)
twitter_input.send_keys(Keys.ENTER)

twitter_password_input = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')

twitter_password_input.send_keys(password)
twitter_password_input.send_keys(Keys.ENTER)


celebrity_name = 'Rock'

search_input = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search_input.send_keys(celebrity_name)
search_input.send_keys(Keys.ENTER)


celeb_page = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span').click()


tweets = []

soup = BeautifulSoup(driver.page_source,'lxml')
postings = soup.find_all('div',class_='css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')

while True:
    for post in postings:
        tweets.append(post.text.strip())
        
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    soup = BeautifulSoup(driver.page_source,'lxml')
    postings = soup.find_all('div',class_='css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    final_tweet = list(set(tweets))
    if len(final_tweet) > 50:
        break
    
        

































