# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:18:49 2020

@author: jpuig
"""

import csv 

from  study_scraper import StudyScraper
from browser import Browser

class Scraper:
    
    def __init__(self):
        self.lines = []

    def process_scraping(self):
        current_path = 'https://clinicaltrials.gov/ct2/show/record/NCT04359303?cond=COVID&draw=3&rank=1&view=record'
                
        browser = Browser(current_path)
        browser.start()
        
        while (len(self.lines) < 5):
            print('process page:', len(self.lines) +1)
            study_scraper = StudyScraper(browser.get_current_page())
            study = study_scraper.get_study()
            self.lines.append(study)
            print('page:', study.id, 'processed')
            
            browser.navigate()

        browser.stop()
        
    def data_to_csv(self):
        file_name = 'studies.csv'
        file = open(file_name, 'w', encoding='utf-8', newline='')
        writer = csv.writer(file, delimiter=';')
        with file:
            for study in self.lines:
                writer.writerow([study.id, study.title, study.official_title])
                
    