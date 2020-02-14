# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:18:37 2019

@author: Ayush
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests, sys, webbrowser, bs4


driver=webdriver.Chrome(r"C:\chromedriver")
driver.get('https://play2048.co/')
html_elem = driver.find_element_by_tag_name('html')
flag= True
a = 10
buttons = ["UP", "RIGHT", "DOWN", "LEFT"]
int(a)
while flag:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)
    try:
        driver.find_element_by_xpath("div[class='game-message game-over']")
        score = driver.find_element_by_xpath("div[class='score-container']")
        print(score.text)
        break
    except:
        flag = True
        
    
