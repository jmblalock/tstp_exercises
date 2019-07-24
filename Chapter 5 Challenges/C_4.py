#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:13:38 2019

@author: emilybregger
"""

aboutme = {"height":"6'4",
           "weight":"240",
           "favorite color": "blue",
           "favorite author": "Orwell"}

q = input("What would you like to know about me?  ")
if q in aboutme:
    stats = aboutme[q]
    print (stats)
else:
    print("Not found.")