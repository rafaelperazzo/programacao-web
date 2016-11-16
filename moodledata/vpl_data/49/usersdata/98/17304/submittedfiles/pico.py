# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    #CONTINUE...
    contC=0
    contD=0
    contI=0
    c=0
    d=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            contC=contC+1
            c=c+contC
            ContD=0
            
        if lista[i]>lista[i+1]:
            contD=contD+1
            d=d+contD
            ContC=0
        if lista[i]==lista[i+1]:
            contI=contI+1
    if contC==c and contD==d and contI==0:
        return True
    else:
        return False

n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
a=[]
for i in range(0,n,1):
    a.append(input('Digite um valor: '))
    
if pico(a):
    print('S')
else:
    print('N')