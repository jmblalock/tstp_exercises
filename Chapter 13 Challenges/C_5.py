#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:45:29 2019

@author: emilybregger
"""

class Horse():
    def __init__(self, 
                 name,
                 breed,
        owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name
        
justin = Rider("Justin Blalock")
emily = Horse("Scootcher",
              "Thoroughbred",
              justin)

print(emily.owner.name)