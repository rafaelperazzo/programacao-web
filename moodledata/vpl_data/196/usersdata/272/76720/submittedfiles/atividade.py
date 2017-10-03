# -*- coding: utf-8 -*-
import math

n= int(input('Digite o valor de n: '))
soma=0
contador=0
num=1
i=0
if (n<0):
    n=n*(-1)
else:
    n=n
while (contador<n):
    soma= soma+(num/(n-i))
    contador=1
    num=num+1
    i=i+1

print(soma)
