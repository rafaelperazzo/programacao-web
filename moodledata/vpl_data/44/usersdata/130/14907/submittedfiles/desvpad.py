# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
x=[]
for i in range(0,n,1):
    x.append(input('Digite um elemento:'))
print('%.2f'%x[0])
print('%.2f'%x[len(x)-1])
s=0
for i in range(0,n,1):
    s=s+x[i]
s=s/(len(x)) 
print('%.2f'%s)
i=0
s1=0
while i<=n-1:
    s1=s1+((x[i]-s)**2)
    i=i+1
D=(1/((n-1)*s1))**0.5
print('%.2f'%D)
