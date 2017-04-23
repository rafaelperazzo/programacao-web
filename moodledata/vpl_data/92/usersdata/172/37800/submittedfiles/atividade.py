# -*- coding: utf-8 -*-
import math
n=int(input('Digite um valor: '))
if  n<0:
    n*(-1)
s=0
i=1
while   i<=n:
    s=(s+1)/n
    i=i+1
    n=n-1
print('%.5f'%s)
