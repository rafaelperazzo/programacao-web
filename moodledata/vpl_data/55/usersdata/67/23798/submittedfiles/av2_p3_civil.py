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
    for j in range (0,a.shape[0],1):
        if i==x:
            soma = soma  + a[i,j]

soma1=0
for j in range (0,a.shape[0],1):
    for i in range (0,a.shape[1],1):
        if j==y:
            soma1 = soma1  + a[i,j]


somat=soma+soma1

print (a[x,y])    
print somat
print a

 
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    