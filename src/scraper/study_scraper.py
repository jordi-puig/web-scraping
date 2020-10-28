# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:18:49 2020

@author: jpuig
"""

from study import Study

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
      study.condition = self.get_text_by_title('Condition')
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
          th = self.browser.find_element_by_xpath("//th[contains(text(), '" + title + "')]") 
          tr = th.find_element_by_xpath("./..");
          td = tr.find_element_by_xpath(".//td[1]")
      except:
          print("not exists element: ", title)
      return None if td is None else td.text

    
  def get_header(self):
      header = []
      header.append('NCT Number')
      header.append('Brief Title')
      header.append('Official Title')
      header.append('Brief Summary')
      header.append('Detailed Description')
      header.append('Start Date')
      header.append('Completion Date')
      header.append('Condition')
      header.append('Intervention')
      header.append('Study Type')
      header.append('Study Population')      
      header.append('Study Groups/Cohorts')
      header.append('Phase')      
      header.append('Ages')
      header.append('Sex/Gender')
      header.append('Eligibility Criteria')
      header.append('Estimated Enrollment')       
      return header   
 