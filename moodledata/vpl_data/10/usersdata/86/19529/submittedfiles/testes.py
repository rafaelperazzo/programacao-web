# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
def degrau(lista):
    maior=0
    for i in range(0,len(lista)-1,1):
        s=(a[i]-a[i+1])
        if s>=maior and s>0:
            maior=s
            return maior
        elif s>=maior and s<0:
            maior=s*-1
            return maior
n=input('n:')
a=[]
for i in range(0,n,1):
    a.append(input(''))
print degrau(a)
