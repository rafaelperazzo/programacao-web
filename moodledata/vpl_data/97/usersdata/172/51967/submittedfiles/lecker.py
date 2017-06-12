# -*- coding: utf-8 -*-
from __future__ import division
def lecker (lista):
    cont=0
    for i in range(1,len(lista+1),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=c+1
    if cont==1:
        return True
    else:
        return False
    
