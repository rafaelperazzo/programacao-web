# -*- coding: utf-8 -*-
import math
n = int(input('n: '))
i = int(input('n: '))
j = int(input('n: '))
cont = 0
cm = 1
while cont < n:
    if cm%i == 0 or cm%j == 0:
        print(cm)
        cont += 1
    cm += 1
    