#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:24:26 2019

@author: emilybregger
"""

import re

line = "The ghost that says boo haunts the loo."

m = re.findall(".[o]o",
               line,
               re.IGNORECASE)

print(m)