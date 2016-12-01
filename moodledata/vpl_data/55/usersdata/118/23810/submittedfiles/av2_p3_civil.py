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
n = input('Digite n:')
a = np.zeros((n,n))
i = input('Digite a posição i :')
j = input('Digite a posição j :')

for l in range(0,n,1):
    for o in range(0,n,1):
        a[l,o] = input('Valor:')

b = peso(a,i,j)
print(b)  
