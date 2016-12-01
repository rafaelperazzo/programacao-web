# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somatorio_linha (a,l):
    soma = 0
    for j in range (0, a.shape[1], 1):
        soma = soma + a[l,j]
    return soma
    
def somatorio_coluna (a,c):
    soma = 0
    for i in range (0, a.shape[0], 1):
        soma = soma + a[i,c]
    return soma
    
def somatorio_total (a,l,c):
    soma = somatorio_linha(a+l) + somatorio_coluna(a,c) - (2*a[l,c])
    return soma
    
n = input('Digite a dimensão da matriz: ')
x = input('Digite o indíce da posíção de x: ')
y = input('Digite o indíce da posição de y: ')

a = np.zeros((n,m))

for i in range (0, a.shape[0], 1):
    for j in range (0, a.shape[1], 1):
        a[i,j] = input('Digite um elemento da matríz: ')
        
print somatorio_total(a,x,y)