# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 23:00:12 2024

@author: danie
"""

bag=input()

apple = [list(bananna.split()) for bananna in bag.splitlines()]

nice=0

for seed in apple:
    a1 = False
    a2 = False
    a3 = False
    
    if all(worms not in seed[0] for worms in ('ab', 'cd', 'pq', 'xy')):
        a1=True
    vnum=0
    for letter in seed[0]:
        if any(vowel in letter for vowel in ('a','e','i','o','u')):
            vnum+=1
        if vnum>=3:
            a2=True    
    for i in range(len(seed[0]) - 1):
        if seed[0][i] == seed[0][i + 1]:
            a3= True
    if a1 == a2 == a3 == True:
        nice+=1

print('There are', nice, 'nice strings')