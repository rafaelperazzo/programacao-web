# -*- coding: utf-8 -*-
import math
n= int(input('Digite o valor de n: '))
a=0
s=0
i=1
numerador=1
if (n<0):
    n= n*(-1)
else:
    n=n
while (i<=n):
    s= (numerador)/(n+a)+s
    i=i+1
    a=a-1
    numerador= numerador + 1
print ('%.5f' %s)