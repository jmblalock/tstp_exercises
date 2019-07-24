#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:40:55 2019

@author: emilybregger
"""

import csv

list_of_lists = [["Top Gun", "Risky Business", "Minority Report"],
                 ["Titanic", "The Revenant", "Inception"],
                 ["Training Day", "Man on Fire", "Flight"]]

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    
    w.writerow(list_of_lists[0])
    w.writerow(list_of_lists[1])
    w.writerow(list_of_lists[2])