# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input('Digite quantas dimensões terá a matriz:')

x=input('Digite o indíce da linha do elemento que se deseja descobrir o peso:')
y=input('Digite o indice da coluna do elemento que se deseja descobrir o peso:')
        
        
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz a:')

        
def Somal(a):
    t=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        t.append(soma)
    return t
    
def SomaC(a):
    t=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        t.append(soma)
    return t
    



