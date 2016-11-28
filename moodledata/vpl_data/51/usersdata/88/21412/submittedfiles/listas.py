# -*- coding: utf-8 -*-
from __future__ import division

def maior_degrau(a):
    maior=0
    for i in range (0,len(a)-1,1):
        degrau=a[i]-a[i+1]
        if degrau<0:
            degrau=degrau*(-1)
        if degrau>maior:
            maior=degrau
    return maior

a=[]
n=input ('digite n:')

for i in range (0,n,1):
    a.append(input('digite um elemento:'))
print maior_degrau(a)