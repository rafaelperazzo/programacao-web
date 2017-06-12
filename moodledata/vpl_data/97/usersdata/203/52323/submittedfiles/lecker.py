# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista1):
    cont1=0
    for i in range(0,len(lista1),1):
        if i==0:
            if lista1[i]>lista1[i+1]:
                cont1=cont1+1
        elif i==(len(lista1)-1):
            if lista1[i]>lista1[i-1]:
                cont1=cont1+1
        else:
            if lista1[i]>lista1[i+1] and lista1[i]>lista1[i-1]:
                cont1=cont1+1
    if cont1==1:
        return true
    else:
        return false
                
            