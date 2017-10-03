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
    soma= soma+ num/(n-i)
    num=num+1
    i=i+1
    contador=contador+1

print('%.5f' %soma)
