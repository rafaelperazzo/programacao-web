# -*- coding: utf-8 -*-
import math
n = int(input('Digite a quantidade de repetições: '))
a = int(input('Digite um inteiro: '))
b = int(input('Digite um inteiro: '))

if (a < b):
    i = a
else :
    i = b
    
while (n > 0) :
    if (i%a == 0) or (i%b == 0):
        print(i)
        n -= 1
    i += 1