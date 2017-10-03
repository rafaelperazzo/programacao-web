# -*- coding: utf-8 -*-
import math

n = int(input('Digite o valor de n: '))
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
i = 1
contador = 1

while (contador<=n):
    multiploa = a*i
    multiplob = b*i
    if (multiploa == multiplob):
        print (multiploa)
        contador = contador + 1
    else:
        print(multiploa)
        print(multiplob)
        contador = contador + 2
    i = i+1
    
