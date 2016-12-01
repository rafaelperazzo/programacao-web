# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n:')
while n<2:
    n=input('Digite a quantidade n correta!:')
a=[]
for i in range(1,n+1,1):
    a.append(input('Digite um valor:'))
m=a[1]-a[0]
if m>=0:
    maior=m
else:
    maior=m*-1
for j in range(0,len(a)-1,1):
    d=a[j+1]-a[j]
    if d>=0:
        degrau=d
    else:
        degrau=d*-1
    if degrau>maior:
        maior=degrau
    else:
        maior=maior
print maior