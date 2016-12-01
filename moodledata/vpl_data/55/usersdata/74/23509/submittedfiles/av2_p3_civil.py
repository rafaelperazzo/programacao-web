# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n = input('Digite o tamanho nxn do tabuleiro : ')
x = input('A casa na contagem horizontal: ')
y = input('A casa na contagem vertical: ')

i = 0
j = 0
l = 0
m = 0
u = x-1
v = y-1
soma = 0
a = np.zeros((n,n))

while (n-1)>=i:
    while (n-1)>=j:
        a[i,j] = input('O valor dessa casa é: ')
        j = j+1
    i = i+1
    j = 0
    
while (n-1)>=l:
    soma = soma+a[u,l]
    l = l+1

while (n-1)>=m:
    soma = soma+a[m,v]
    m = m+1
    
soma = soma - 2*a[u,v]

print soma