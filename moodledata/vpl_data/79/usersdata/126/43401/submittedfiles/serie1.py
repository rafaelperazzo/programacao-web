# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade de termos a serem calculados:'))

i=1
soma=0
d=1
for i in range(1,n+1,1):
    if i%2!=0:
        d=i**2
        soma=soma+i/d
    elif i%2==0:
        d=i**2
        soma=soma-i/d
print(soma)