# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:18:49 2020

@author: jpuig
"""

class Scraper:

  # Import the Selenium web driver
  from selenium import webdriver

  from webdriver_manager.chrome import ChromeDriverManager

  browser = webdriver.Chrome(ChromeDriverManager().install())
  path_to_web = 'https://clinicaltrials.gov/ct2/show/record/NCT04359303?cond=COVID&draw=3&rank=1&view=record'
  browser.get(path_to_web)
  
  # scrap page
  title = browser.find_element_by_xpath("//*[contains(text(), 'First Submitted Date')]")
  print(title.text)
  
  browser.close()
