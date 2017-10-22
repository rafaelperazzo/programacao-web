# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n: '))
i=1
soma=0
a=0
num=1
if (n<0):
    n=n*(-1)
else:
    n=n
while (i<=n):
    soma=soma+(num/(n+a))
    a=a-1
    i=i+1
    num=num+1
print('%.5f' %soma)

