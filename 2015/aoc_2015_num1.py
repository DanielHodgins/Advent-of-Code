# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:18:37 2024

@author: danie
"""

i=0

bag=input()

for char in bag:
    if char=="(":
        i+=1
    if char==")":
        i-=1
print("i=", i)