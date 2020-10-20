# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:18:49 2020

@author: jpuig
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class StudyScraperExample:
  
  def getTextByTitle(browser, title):
      th = browser.find_element_by_xpath("//*[contains(text(), '" + title + "')]") 
      tr = th.find_element_by_xpath("./..");
      td = tr.find_element_by_xpath(".//td[1]")
      return td.text
  
  def getTextByTitle(browser, title):
      th = browser.find_element_by_xpath("//*[contains(text(), '" + title + "')]") 
      tr = th.find_element_by_xpath("./..");
      td = tr.find_element_by_xpath(".//td[1]")
      return td.text
      
  text = getTextByTitle(browser, 'NCT Number')  
  print(text)
  
  browser = webdriver.Chrome(ChromeDriverManager().install())
  path_to_web = 'https://clinicaltrials.gov/ct2/show/record/NCT04359303?cond=COVID&draw=3&rank=1&view=record'
  browser.get(path_to_web)
  
  
  
  # scrap page
  th = browser.find_element_by_xpath("//*[contains(text(), 'NCT Number')]")
  print(th.text) 
  tr = th.find_element_by_xpath("./..");
  td = tr.find_element_by_xpath(".//td[1]")
  print(td.text)
  
  th = browser.find_element_by_xpath("//*[contains(text(), 'First Submitted Date')]")
  print(th.text) 
  tr = th.find_element_by_xpath("./..");
  td = tr.find_element_by_xpath(".//td[1]")
  print(td.text)
  

  
  browser.close()