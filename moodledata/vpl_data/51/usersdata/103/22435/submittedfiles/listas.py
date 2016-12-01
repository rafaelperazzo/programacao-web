# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de elementos da lista:')
while n<2:
    n=input('Digite a quantidade de elementos da lista:')
a=[]
for i in range (1,n+1,1):
    a.append(input('Insira um valor:')
m=a[2]-a[1]
if m>=0:
    maior=m
else:
    maior=m*-1
for i in range (1,len(a),1):
    d=a[i+1]-a[i]
    if d>=0:
        degrau=d
    else:
        degral=d*-1
    if degrau>maior:
        maior=degrau
    else:
        maior=maior
print maior