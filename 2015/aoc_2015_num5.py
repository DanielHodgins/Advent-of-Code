# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:24:08 2024

@author: danie
"""

bag=input()



houses=[[0,0]]

for i in bag:
    if ">"==i:
        houses.append([houses[-1][0]+1,houses[-1][1]])
    if "<"==i:
        houses.append([houses[-1][0]-1,houses[-1][1]])
    if "v"==i:
        houses.append([houses[-1][0],houses[-1][1]-1])
    if "^"==i:
        houses.append([houses[-1][0],houses[-1][1]+1])

carrot=[]

for apple in houses:
    if not apple in carrot:
        carrot.append(apple)

print("Santa visited", len(carrot), "houses!")