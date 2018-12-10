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
import re
import regex
import errno, os, stat, shutil


path = "D:/xrvision/xrvision_dataset/CAR dataset/sgcarmart_by_models"
os.chdir(path)

from selenium import webdriver
chrome_path = r"C:\Users\default.LAPTOP-2CI68M4P\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)


for x in range(0, 1200,60):
    
    url = "https://www.sgcarmart.com/new_cars/newcars_pastcars.php?BRSR={}&PCM=1".format(x)
    driver.get(url)
    sleep(randint(5,20))
    
    page = requests.get(url).content
    soup = BeautifulSoup(page)
    
    model_name = ""
    dirs_name = soup.find_all("img", src=re.compile("https://i.i-sgcm.com/new_cars/cars"))
    for names in dirs_name:
        model_name = names.get('alt')
        model_name =  model_name.replace(":", "")
        generation = names.findNext('span').text
        generation = generation.replace("(", "")
        generation = generation.replace(")", "")
        
        if not os.path.exists(model_name):
            os.makedirs(model_name)        
        
        os.chdir(model_name)   
        if not os.path.exists(generation):
            os.makedirs(generation)  
        
        os.chdir(path)    

            
driver.close()    
