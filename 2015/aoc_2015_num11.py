# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 23:45:58 2025

@author: danie
"""

import numpy as np


apple = np.zeros((1000, 1000))


bag=input()

for lizards in range(len(bag.splitlines())):
    command = bag.splitlines()[lizards]
    parts = command.split()
    if parts[0]=='toggle':
        start_coords = list(map(int, parts[1].split(',')))
        end_coords = list(map(int, parts[3].split(',')))

        # Perform the action on the grid
        for i in range(start_coords[0], end_coords[0] + 1):
            for j in range(start_coords[1], end_coords[1] + 1):
                apple[i][j] +=1
        for i in range(1000):
            for j in range(1000):
                if apple[i][j]==2:
                    apple[i][j]=0
    if parts[0]=='turn':
        start_coords = list(map(int, parts[2].split(',')))
        end_coords = list(map(int, parts[4].split(',')))

        # Perform the action on the grid
        for i in range(start_coords[0], end_coords[0] + 1):
            for j in range(start_coords[1], end_coords[1] + 1):
                if parts[1] == "on":
                    apple[i][j] = 1
                if parts[1] == "off":
                    apple[i][j] = 0
lights=0
for i in range(1000):
    for j in range(1000):
        lights+=apple[i][j]
print('There are', lights, 'lights on')