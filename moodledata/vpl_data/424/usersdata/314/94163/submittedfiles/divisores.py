# -*- coding: utf-8 -*-
import math

n = int(input('Digite o valor de n: '))
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

for i in range(1, n, 1):
    if (a%i == 0) or (b%i == 0):
        
