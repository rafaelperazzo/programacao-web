# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    d=0
    b=0
    c=0
    maior=0
    for i in range (0,len(a)-1,1):
        b= a[i]
        c= a[i+1]
        d=b+c
        if d<0:
            d= d *(-1)
        if d> maior:
            maior=d
            d=0
        else:
            d=0    
    return maior
    
n=input('Insira a quantidade de termos:')
x=[]
for i in range(0,n,1):
    x[i]=x.append(input('Insira um termo:'))
print degrau(x)