# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

n = input('Digite o tamanho do tabuleiro: ')
c = input('Digite a casa que deseja saber o peso: ')

soma = 0
a = np.zeros((n,n))
x = c-1

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Valor da casa do tabuleiro: ')

for k in range(0,c,1):
    soma = soma+a[k,x]

for l in range(0,c,1):
    soma = soma+a[x,k]

soma = soma - 2*a[x,x]

print soma












































