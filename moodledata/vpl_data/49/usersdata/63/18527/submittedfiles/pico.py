# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    posicao=0
    for i in range(0,len(lista)-1,1):
        if a[i]>a[i+1]:
            posicao=i
            break
    cont=0
    fr i in range(posicao, len(lista)-1,1):
        if a[i]<=a[i+1]:
            cont=cont+1
    if cont==0 and posicao!=0:
        return True
    else:
        return False
    


n = input('Digite a quantidade de elementos da lista: ')
a=[]

