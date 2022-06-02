from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
import pandas as pd
import time

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe",options=options)

url = 'https://www.imdb.com/title/tt0325980/reviews?ref_=tt_urv'

driver.get(url)
rating=[]
movie=[]
heading=['Movie','rating']
element = driver.find_element_by_class_name("ipl-load-more__button")
element.click()
time.sleep(10)
element = driver.find_element_by_class_name("ipl-load-more__button")
element.click()
time.sleep(10)
element = driver.find_element_by_class_name("ipl-load-more__button")
element.click()
time.sleep(10)
element= driver.find_element_by_class_name("parent")
elements = driver.find_elements_by_class_name("rating-other-user-rating")
for i in elements:
    rating.append(i.text)
    movie.append(element.text)
print(rating)
df = pd.DataFrame(list(zip(movie,rating)),columns=heading)
df.to_csv("rating5.csv",index=False)
driver.quit()