# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:03:08 2020

@author: jpuig
"""
import csv 

class Data2CSV:
  def __init__(self, name, header, lines):          
      self.name = name
      self.header = header
      self.lines = lines
      
  def save_csv(self):
        file_name = self.name
        file = open(file_name, 'w', encoding='utf-8', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(self.header)
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