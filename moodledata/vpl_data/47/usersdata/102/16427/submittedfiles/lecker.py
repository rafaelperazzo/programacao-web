# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    contador=0
    
    for i in range (0,len(lista),1):
        if i==0:
            if listan[i]>lista[i-1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista [i]>lista[i-1]:
                cont=cont+1
        else:
            if (lista [i]>lista[i-1]) and (lista [i]>lista [i-1]):
                cont=cont+1
                
    if cont==1:
        return true
    else:
        return false

a=[]
b=[]
if lecker(a):
    print('s')
else:
    print('N')
if lecker(b):
    ptint('S')
else:
    print('N')

                

    

    