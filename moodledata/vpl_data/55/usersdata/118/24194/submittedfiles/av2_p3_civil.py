# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

# Funções
def peso(a,i,j):
    c = sum(a[i,:])
    l = sum(a[:,j])
    p = (l+c)-(2*a[i,j])
    return p
    
#Programa Principal   
#Entrada
n = input('Digite n:')
i = input('Digite a posição i :')
j = input('Digite a posição j :')
a = np.zeros((n,n))

for l in range(0,n,1):
    for o in range(0,n,1):
        a[l,o] = input('Valor:')

#Saída
b = peso(a,i,j)
print(int(b))  
