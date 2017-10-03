# -*- coding: utf-8 -*-
import math

n=int(input('Digite o valor de n:'))
if n<0:
    n=n*(-1)
s=0
i=0
for numerador in range (1,n+1,1):
    s=s+numerador/(n-i)
    i=i+1
print('%.5f' %s)

