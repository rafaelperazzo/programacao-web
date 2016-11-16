# -*- coding: utf-8 -*-
from __future__ import division

n=inmput('Digite a quantidade de elementos da lista:')
a=[]
def pico(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
            if cont>0:
                return True
            else:
                return False
            print(i)