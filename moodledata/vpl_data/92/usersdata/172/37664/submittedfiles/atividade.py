# -*- coding: utf-8 -*-
import math
n=int(input('Digite um valor: '))
if  n<0:
    n*(-1)
s=0
i=1
d=n
while   i==n:
    s=(s+1)/d
    i=i+1
    d=d-1
print('%.5f'%s)
