# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaLinha(a,x):
    Soma = 0
    for i in range (0,n,1):
        Soma= Soma + a[x,i]
    return Soma
    
def somaColuna(a,y):
    Soma=0
    for i in range (0,n,1):
        Soma = Soma + a[i,y]
    return Soma
    
def peso(a,x,y):
    peso = somaLinha(a,x) + somaColuna(a,y) - 2*(a[x,y])
    return peso
    
n = input ('Digite a dimensão:')
x = input ('Digite o valor da linha:')
y = input ('Digite o valor da coluna:')
a = np.zeros((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        a[i,j] = input ('Digite um número:')
print (peso (a,x,y))