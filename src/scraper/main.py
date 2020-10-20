# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:29:47 2020

@author: jpuig
"""

# Import the Selenium web driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Main:
    
  browser = webdriver.Chrome(ChromeDriverManager().install())
  path_to_web = 'https://clinicaltrials.gov/ct2/show/record/NCT04359303?cond=COVID&draw=3&rank=1&view=record'
  browser.get(path_to_web)

  studyScraper = StudyScraper(browser)
  study = studyScraper.get_study()
  print(str(study))  
  browser.close()

#class data2csv(self, data):
    
    __