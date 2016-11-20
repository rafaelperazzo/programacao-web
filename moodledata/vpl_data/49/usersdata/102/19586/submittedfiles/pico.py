# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    posiçao=0
    for i in range(0,len(lista)-1,1):
        if a[i]>a[i+1]:
            posiçao=1
            break
        
    cont=0
    for i in range(posiçao,len(lista)-1,1):
        if a[i]<=a[i+1]:
            cont=cont+1
        
    if cont==0 and posiçao!=0:
        return true
    else:
        return false
        
    

    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
