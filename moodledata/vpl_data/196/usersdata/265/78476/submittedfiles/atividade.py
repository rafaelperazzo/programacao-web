# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n: '))
i=1
soma=0
if (n<0):
    n=n*(-1)
else:
    n=n
while (i<n):
    soma=(i/(n))
    n=n-1
    i=i+1
print(soma)

