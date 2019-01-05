# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:57:06 2018

@author: soh.samy
"""

import os
import csv

file_name = 'data_store.csv'

# send data as dict object 
def store_csv(data , file_name=file_name):
    is_file_exist = os.path.exists(file_name)

    with open(file_name ,'a') as csvfile:

        field_names = list(data.keys())
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        if not is_file_exist:
            writer.writeheader()

        writer.writerow(data)
