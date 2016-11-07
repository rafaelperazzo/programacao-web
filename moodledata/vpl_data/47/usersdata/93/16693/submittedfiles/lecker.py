# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    if a[0]>a[1]:
        cont=cont+1
    if a[len(lista)-1]> a[len(lista)-2]:
        cont=cont+1
    for i in range(1,len(lista)-2,1):
        if a[i]>a[i+1] and a[i]>a[i-1]:
            cont=cont+1
    if cont==0:
        return cont
    else:
        return cont
a=[1,2,3,4,5,6]
lecker(a)

