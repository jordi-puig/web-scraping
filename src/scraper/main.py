# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:29:47 2020

@author: jpuig
"""

class Main:
   
  test = Scraper()
  print('scraping process starting...')  
  test.process_scraping()
  print('scraping process ended')  
  print('saving data to csv...')
  test.data_to_csv()
  print('data to csv saved')  
