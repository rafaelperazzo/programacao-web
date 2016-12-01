# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de elementos da lista:')
while n<2:
    n=input('Digite a quantidade de elementos da lista:')
a=[]
for i in range (1,n+1,1):
    a.append(input('Insira um valor:'))
m=a[1]-a[0]
if m>=0:
    maior=m
else:
    maior=m*-1
for j in range (1,len(a)+1,1):
    d=a[j]-a[j-1]
    if d>=0:
        degrau=d
    else:
        degrau=d*-1
    if degrau>maior:
        maior=degrau
    else:
        maior=maior
print maior