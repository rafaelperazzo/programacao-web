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
a=[4,0,-1,2,2,3,8]
print (degrau(a))