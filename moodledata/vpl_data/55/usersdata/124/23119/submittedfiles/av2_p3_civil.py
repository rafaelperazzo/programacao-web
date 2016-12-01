# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def xadrez(l, c, a):
    sl = 0
    sc = 0
    for i in range (0, a.shape[0], 1):
        sc = sc + a[i,c]
    for j in range (0, a.shape[1], 1):
        sl = sl + a[l,j]
    peso = sl + sc - 2*a[l,c]
    return peso
n = input('Digite o número de linhas e de colunas da matriz: ')
l = input('Digite a linha do número que deve ter o peso descoberto: ')
c = input('Digite a coluna do número que deve ter o peso descoberto: ')
a = np.zeros( (n,n) )
for i in range (0, a.shape[0], 1):
    for j in range (0, a.shape[1], 1):
        a[i,j] = input('Digite um valor para a matriz: ')
print xadrez(l, c, a)