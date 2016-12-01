# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaL(a,x):
    
    soma=0
    for j in range (0,a.shape[1],1):
        soma = soma+a[x,j]
        
    return soma

def somaC(a,y):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,y]
    return soma
        
def peso(a,x,y):
    peso=(somaL(a,x)+somaC(a,y))-(2*a[x,y])
    
    return peso

n = input ('Digite o valor de n:')
x = input ('Digite o valor de x:')
y = input ('Digite o valor de y:')

a = np.zeros ((n,n))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('Digite os elementos:')

peso=peso(a,x,y)

print('%d'%peso)
        
        