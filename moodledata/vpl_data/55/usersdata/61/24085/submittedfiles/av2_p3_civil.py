# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somal(f,l,c):
    soma=0
    for j in range(0,f.shape[1],1):
        soma=soma+f[l,j]
    return soma
        
def somac(f,l,c):
    soma=0
    for i in range(0,f.shape[0],1):
        soma=soma+f[i,c]
    return soma
        
def somat(f,l,c):
    sl=somal(f,l,c)
    sc=somac(f,l,c)
    soma=sl+sc
    return soma
    
d=input("Digite a ordem da matriz: ")
l=input("Digite o índice i: ")
c=input("Digite o índice j: ")
f=np.zeros((d,d))
for i in range(0,n,1):
    for j in range(0,n,1):
        f[i,j]=input("Digite um número: ")
peso=somat(f,l,c)
print peso       
        
        