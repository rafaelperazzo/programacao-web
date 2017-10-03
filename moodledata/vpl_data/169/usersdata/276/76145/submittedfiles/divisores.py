# -*- coding: utf-8 -*-
import math

n = int(input('Digite o valor de n: '))
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
i = 1
contador1 = 1
contador2 = 0

while (contador<=n):
    multiploa = a*i
    multiplob = b*i
    if (multiploa == multiplob):
        print (multiploa)
        contador1 = contador1 + 1
    else:
        print(multiploa)
        print(multiplob)
        contador2 = contador2 + 2
    i = i+1
    
