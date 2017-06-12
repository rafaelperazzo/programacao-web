# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    n=len(lista)
    if n==1:
        return False
    m=0
    if lista[0]>lista[1]:
        m+=1
    for i in range(1,n-1):
        if lista[i-1]<lista[i] and lsta[i]<lista[i+1]:
            m+=1
        if lista[n-1]>lista[n-2]:
            m+=1
            return m==1
print(lecker(2,5,10,46,25,12,7))

