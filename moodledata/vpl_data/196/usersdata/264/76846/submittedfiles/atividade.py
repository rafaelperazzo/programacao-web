# -*- coding: utf-8 -*-
import math
n= int(input('Digite o valor de n:'))
s=0
i=0
numerador=0
if (n<0):
    n*(-1)
else:
    n*1
while (i<=n):
    s= numerador+1/(n)
    numerador= numerador+1
    n= n-1
print (s)