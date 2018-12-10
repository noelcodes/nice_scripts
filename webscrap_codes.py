import numpy as np
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import re
from time import sleep
import os
import urllib
import requests
from random import randint
import os
import random
from urllib.request import urlopen
import urllib.request

from selenium import webdriver
chrome_path = r"C:\Users\default.LAPTOP-2CI68M4P\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
year = ""
dirs_name = ""
joburl_last = ""
x_done = []
#for x in random.sample(range(0, 28400,100), 142):
for x in range(24100, 28400,100):
    if x in x_done:
        continue
    else:
            
        url = "https://www.sgcarmart.com/used_cars/listing.php?BRSR={}&RPG=100".format(x)
        x_done.append(x)
        print(url)   
    ####################################    
        
        driver.get(url)
        sleep(randint(5,20))
        
        html_ = driver.page_source
        html_ = BeautifulSoup(html_, 'lxml')
        
        for item in html_.find_all("a", href=re.compile("info.php?")):
            print("Getting new joburl")
            joburl = item.get('href')
        
            if joburl == joburl_last:
                print("match")
                continue
            else:
                print("unmatch")
                joburl_last = joburl
        
        ####################################
                producturl = "https://www.sgcarmart.com/used_cars/" + joburl
                print(producturl)
                page = requests.get(producturl).content
                soup = BeautifulSoup(page)
                print("Random Sleeping 5 - 20 sec............")
                
                try:
                    dirs_name = soup.find('a', {"class": "link_redbanner"}).text
                    dirs_name = dirs_name.replace("/", "")
                except:
                    dirs_name = '8888'
                    pass
                
                
                
                try:
                    year = soup.find(text='Manufactured').findNext('td').text
                except:
                    year = '8888'
                    pass
                
                new_dir = "D:/xrvision/xrvision_dataset/sgcarmart_dataset/" + year + "_" + dirs_name + "/"
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                
                
#                sleep(randint(1,15))
                print("Wake up............")
                
            
                for pro in soup.find_all("img", src=re.compile("cars_used")):
                    pic_url = pro.get('src')
                    big_url = pic_url[:-4] + 'b.jpg'
                    new_big_url = new_dir + big_url[38:]
                    print(new_big_url)
            ####################################
                    try:
                        urllib.request.urlretrieve(big_url, new_big_url)
                        print("Saved file = " + new_big_url)
                    
                    except urllib.error.HTTPError as err:
                       pass
         


driver.close()
