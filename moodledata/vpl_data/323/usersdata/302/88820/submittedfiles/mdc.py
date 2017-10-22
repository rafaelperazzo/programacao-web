# -*- coding: utf-8 -*-
import math
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

for i in range (1000000,0,-1):
    if a%i == 0 and b%i == 0:
        print(i)
        break



