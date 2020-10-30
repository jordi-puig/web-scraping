# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:18:49 2020

@author: jpuig
"""
from  study_scraper import StudyScraper
from browser import Browser
from data2csv import Data2CSV

class Scraper:
    
    def __init__(self):
        self.lines = []
        self.study_scraper = None

    def process_scraping(self):
        current_path = 'https://clinicaltrials.gov/ct2/show/record/NCT04359303?cond=COVID&draw=3&rank=1&view=record'
                
        browser = Browser(current_path)
        browser.start()
        
        more_pages = True
        while (more_pages and len(self.lines) < 5):
            try:    
                print('processing page:', len(self.lines) +1, ' ...')
                self.study_scraper = StudyScraper(browser.get_current_page())
                study = self.study_scraper.get_study()
                self.lines.append(study)
                print('page:', study.id, 'processed')
                
                browser.navigate()
            except:
                print('no more pages to scrap')
                more_pages = False
            
        browser.stop()
        
    def data_to_csv(self):
        file_name = 'studies.csv'
        header = self.study_scraper.get_header()
        data2csv = Data2CSV(file_name, header, self.lines)      
        data2csv.data_to_csv()



 
    
                
    