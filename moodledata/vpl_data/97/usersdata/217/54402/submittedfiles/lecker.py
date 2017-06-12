# -*- coding: utf-8 -*-
from __future__ import division
def lecker(2,5,10,46,25,12,7):
    cont=0
    for i in range(1,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                def lecker(lista):
                    cont=cont+1
    if cont==1:
        return(true)
    else:
        return(false)

