# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 23:29:47 2024

@author: danie
"""

bag=input()

apple = [list(bananna.split()) for bananna in bag.splitlines()]

nice=0

for seed in apple:
    a1 = False
    a2 = False
    
    seen = set()
    newseen = set()
    for i in range(len(seed[0]) - 1):
        pair = seed[0][i:i+2]
        if pair in seen:
            a1=True
        seen=seen.union(newseen)
        newseen.add(pair)
    
    for i in range(len(seed[0]) - 2):
        if seed[0][i] == seed[0][i + 2]:
            a2= True
    if a1 == a2 == True:
        nice+=1

print('There are', nice, 'nice strings')