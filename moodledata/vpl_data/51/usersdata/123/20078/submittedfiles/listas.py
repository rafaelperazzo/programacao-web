# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    d=0
    maior=0
    for i in range (0,len(a)-1,1):
        if a[i] > a[i+1]:
            d=a[i]-a[i+1]
        else:
            d=a[i+1]-a[i]
        if d> maior:
            maior=d
        d=0
    return maior
    
n=input('Insira a quantidade de termos:')
a=[]
for i in range(0,n,1):
    a[i]=a.append(input('Insira um termo:'))
print degrau(a)