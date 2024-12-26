# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:18:37 2024

@author: danie
"""

i=0
p=0
t=0

bag=input()

for char in bag:
    if char=="(":
        i+=1
        p+=1
    if char==")":
        i-=1
        p+=1
    if t==0:
        if -1==i:
            print(p)
            t=1
print("i=", i)