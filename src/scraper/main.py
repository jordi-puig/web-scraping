# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:29:47 2020

@author: jpuig
"""

from scraper import Scraper

class Main:
   
  scraper = Scraper() 
  print('scraping process starting...')  
  scraper.process_scraping()
  print('scraping process ended')  
  print('saving data to csv...')
  scraper.data_to_csv()
  print('data to csv saved')  