# -*- coding: utf-8 -*-
import math
n = int(input('n: '))
i = int(input('n: '))
j = int(input('n: '))
'''multi = 0
multj = 0
cont = 0
while cont < n:
    if multi < multj and:
        print(multi)
        multi += i
    elif multj < multi:
        print(multj)
        multj += j
    else:
        print(multj)
        multi += i
        multj += j
    cont += 1
'''
cont = 0
cm = 0
while cont < n:
    if cm%i == 0 or cm%j == 0:
        print(cm)
        cont += 1
    cm += 1