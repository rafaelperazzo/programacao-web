# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n=input("Digite a dimensão da matriz:")
x=input("Digite a cordenada i para calcular o peso da peça:")
y=input("Digite a cordenada j para calcular o peso da peça:")

    
linha=n
coluna=n
a=np.zeros ((linha,coluna))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input("Digite um elemento para a matriz:")
        
soma = 0

for i in range (0,a.shape[1],1):
    soma = soma + a[x,:]
    
print soma

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    