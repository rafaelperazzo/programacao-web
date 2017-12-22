# -*- coding: utf-8 -*-
import math
x = int(input('Digite um número inteiro positivo: '))
y = int(input('Digite um número inteiro positivo: '))
while y != 0:
    n = x % y
    x = y
    y = n
print(x)

    
    
