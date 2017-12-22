# -*- coding: utf-8 -*-
import math
n = int(input('n: '))
i = int(input('n: '))
j = int(input('n: '))
multi = 0
multj = 0
cont = 0
for p in range (1,n,1):
    if multi < multj:
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