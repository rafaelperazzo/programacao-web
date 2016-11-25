# -*- coding: utf-8 -*-
from __future__ import division

def maiordegrau(lista):
    listadegraus=[]
    for i in range(0,len(lista)-1,1):
        degrau=lista[i]-lista[i+1]
        if degrau<0:
            degrau=degrau*(-1)
        listadegraus.append(degrau)
    maior=0
    for i  in range(0,len(listadegraus),1):
        if listadegraus[i]>maior:
            maior=listadegraus[i]
        
    return maior    
n=input('Digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um valor: '))
x=maiordegrau(a)
print(x)