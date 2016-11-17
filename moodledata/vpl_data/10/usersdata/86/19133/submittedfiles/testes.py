# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
def degrau(lista):
    maior=0
    for i in range(0,len(lista)-1,1):
        s=(a[i]-a[i+1])*(-1)
        if s>=maior:
            maior=s
            return maior
a=[4,0,-1,2,2,3,8]
print (degrau(a))