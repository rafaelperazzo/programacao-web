# -*- coding: utf-8 -*-
import math

n=int(input('Digite um número:'))
soma=0
i=1

while n>0:
    if (i%2!=0):
        soma= soma + (i//(i**2))
        i=i+1
        n=n-1
    else:
        if (i%2==0):
            soma= soma - (i//(i**2))
            i=i+1
            n=n-1
print (soma)