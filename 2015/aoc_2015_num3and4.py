# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:36:47 2024

@author: danie
"""

bag=input()

apple = [list(map(int, bananna.split('x'))) for bananna in bag.splitlines()]

paper=0

for i in apple:
    paper+=2*(i[0]*i[1]+i[1]*i[2]+i[2]*i[0])+min(i[0]*i[1],i[1]*i[2],i[2]*i[0])

print("The elves need", paper, "square feet of paper" )

ribbon=0

for i in apple:
    wrap=2*(i[0]+i[1]+i[2])-2*max(i[0],i[1],i[2])
    bow=i[0]*i[1]*i[2]
    ribbon+=(bow+wrap)
    
print("The elves need", ribbon, "feet of ribbon" )