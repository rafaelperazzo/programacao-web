# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[1]:
                cont=cont+1
        if i==(len(lista)-1):
            if lista[len(lista)-1] >lista[len(lista)-2]:
                cont=cont+1
        else: 
            if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
                cont=cont+1
                
    if cont==1:
        return true
    else:
        return false
        

            

            

