# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:14:27 2024

@author: danie
"""

import hashlib

bag = input()

t = 0

while True:
    t += 1
    message = bag+str(t)
    md5 = hashlib.md5(message.encode()).hexdigest()

    if md5[0:5] == '00000':
        print('The lowest integer is', t, 'where md5 is', md5)
        break

while True:
    t += 1
    message = bag+str(t)
    md5 = hashlib.md5(message.encode()).hexdigest()

    if md5[0:6] == '000000':
        print('The lowest integer is', t, 'where md5 is', md5)
        break