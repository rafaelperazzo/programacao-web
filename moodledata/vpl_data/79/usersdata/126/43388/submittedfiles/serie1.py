# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade de termos a serem calculados:'))

i=0
soma=0
for i in range(1,n+1,1):
     d=i**2
    if i%2==1:
        soma=soma+(i/d)
        i=i+1
    elif i%2==0:
        soma=soma-(i/d)
print(soma)