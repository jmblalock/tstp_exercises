#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:56:06 2019

@author: emilybregger
"""

nums = [12,30,87]

while True:
    a = input("Please guess a number. Type q to quit: ")
    if a == 'q':
        break
    elif int(a) in nums:
        print("You guessed correctly")
    else:
        print("You guessed incorrectly")