# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:49:22 2024

@author: danie
"""

bag=input()

bag1=bag[::2]
bag2=bag[1::2]

santa=[[0,0]]
robosanta=[[0,0]]


for i in bag1:
        if ">"==i:
            santa.append([santa[-1][0]+1,santa[-1][1]])
        if "<"==i:
            santa.append([santa[-1][0]-1,santa[-1][1]])
        if "v"==i:
            santa.append([santa[-1][0],santa[-1][1]-1])
        if "^"==i:
            santa.append([santa[-1][0],santa[-1][1]+1])        
for i in bag2:
        if ">"==i:
            robosanta.append([robosanta[-1][0]+1,robosanta[-1][1]])
        if "<"==i:
            robosanta.append([robosanta[-1][0]-1,robosanta[-1][1]])
        if "v"==i:
            robosanta.append([robosanta[-1][0],robosanta[-1][1]-1])
        if "^"==i:
            robosanta.append([robosanta[-1][0],robosanta[-1][1]+1])      


carrot=[]

for apple in santa:
    if not apple in carrot:
        carrot.append(apple)
for apple in robosanta:
    if not apple in carrot:
        carrot.append(apple)

print("Santa visited", len(carrot), "houses!")