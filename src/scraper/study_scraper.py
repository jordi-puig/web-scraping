# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:18:49 2020

@author: jpuig
"""

# Import the Selenium web driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import csv

class Scraper:
    
    def __init__(self):
        self.lines = []

    def process_scraping(self):
        current_path = 'https://clinicaltrials.gov/ct2/show/record/NCT04359303?cond=COVID&draw=3&rank=1&view=record'
        
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)

        options = Options()
        options.add_argument(f'user-agent={user_agent}')                
        
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.get(current_path)
        
        while (len(self.lines) < 10):
            study_scraper = StudyScraper(browser)
            study = study_scraper.get_study()
            self.lines.append(study)
            
            navigator = NavigatorScraper(browser)
            navigator.get_next_link()

        browser.close()
        
    def data_to_csv(self):
        file_name = 'studies.csv'
        file = open(file_name, 'w', encoding='utf-8', newline='')
        writer = csv.writer(file, delimiter=';')
        with file:
            for study in self.lines:
                writer.writerow([study.id, study.title, study.official_title])

class NavigatorScraper:
  def __init__(self, browser):          
      self.browser = browser
      
  def get_next_link(self):
      class_name = 'tr-next-link'
      next_link = self.browser.find_element_by_class_name(class_name)
      next_link.click()

  def get_previous_link(self):
      class_name = 'tr-prev-link'
      previous_link = self.browser.find_element_by_class_name(class_name)
      previous_link.click()      
                
class StudyScraper:
    
  def __init__(self, browser):          
      self.browser = browser
      
  def get_study(self):
      study = Study()   
      study.id = self.get_text_by_title('NCT Number')
      study.title = self.get_text_by_title('Brief Title')
      study.official_title = self.get_text_by_title('Official Title')
      study.brief_summary = self.get_text_by_title('Brief Summary')
      study.detailed_description = self.get_text_by_title('Detailed Description')
      study.start_date = self.get_text_by_title('Start Date')
      study.completion_date = self.get_text_by_title('Completion Date')
      study.condition = self.get_text_by_title('Condition  ICMJE')
      study.intervention = self.get_text_by_title('Intervention')
      study.study_type = self.get_text_by_title('Study Type')
      study.study_population = self.get_text_by_title('Study Population') 
      study.study_groups = self.get_text_by_title('Study Groups/Cohorts') 
      study.phase = self.get_text_by_title('Phase')
      study.ages = self.get_text_by_title('Ages')
      study.sex_gender = self.get_text_by_title('Sex/Gender')
      study.eligibility_criteria = self.get_text_by_title('Eligibility Criteria')
      study.estimated_enrollment = self.get_text_by_title('Estimated Enrollment')       	
      return study

  def get_text_by_title(self, title):
      td = None
      try:
          th = self.browser.find_element_by_xpath("//*[contains(text(), '" + title + "')]") 
          tr = th.find_element_by_xpath("./..");
          td = tr.find_element_by_xpath(".//td[1]")
      except:
          print("not exists element: ", title)
      return None if td is None else td.text


class Study():    
  def __init__(self):
     pass
     
  def id(self):
      return self.id

  def title(self):
      return self.title    

  def official_title(self):
      return self.official_title   