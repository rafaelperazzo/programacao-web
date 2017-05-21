# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número:'))
soma=0
if n<0:
    n=n*(-1)
    for i in range(0,n+1,1):
        soma=soma+((i+1)/(n))
    n=n-1
print(soma)

