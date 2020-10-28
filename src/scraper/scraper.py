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
        file = open(file_name, 'w', encoding='utf-8', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(self.study_scraper.get_header())
        with file:
            for study in self.lines:
                writer.writerow([study.id, 
                                 study.title, 
                                 study.official_title, 
                                 study.brief_summary,
                                 study.detailed_description,
                                 study.start_date,
                                 study.completion_date,
                                 study.condition,
                                 study.intervention,
                                 study.study_type,
                                 study.study_population,
                                 study.study_groups,
                                 study.phase,
                                 study.ages,
                                 study.sex_gender,
                                 study.eligibility_criteria,
                                 study.estimated_enrollment
                                ])



 
    
                
    