# -*- coding: utf-8 -*-
from __future__ import division



    
def somatorio(n):
    par=0
    impar=0
    for i in range(1,n,1):
        if n%i==0:
            par=par+1
        if n%i==1:
            impar=impar+1
        
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('Digite a lista:'))
    a.append(valor)
    
