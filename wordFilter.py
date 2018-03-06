# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 20:16:05 2018

@author: Stephenry
"""

badWords = []
fd = open("badWords.txt")

for line in fd:
    if " " not in line:
        badWords.append(line.replace("\n", ""))
        
print(str(badWords))