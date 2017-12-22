# -*- coding: utf-8 -*-
import math
n = int(input('informe o numero 1 '))
x = int(input('informe o numero 2: '))

g = x + n 


while True:
    if (x%g == 0) and (n%g == 0):
        break
    else:
        g = g - 1
print(g)