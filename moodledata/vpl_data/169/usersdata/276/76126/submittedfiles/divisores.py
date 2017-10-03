# -*- coding: utf-8 -*-
import math

n = int(input('Digite o valor de n: '))
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
i = 1
contador = 1

while (contador<=n):
    if (a*i == b*i):
        print (a*i)
    else:
        print(a*i)
        print(b*i)
    i = i+1
    contador = contador + 2
