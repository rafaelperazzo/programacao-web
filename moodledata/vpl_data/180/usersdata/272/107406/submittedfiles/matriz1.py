# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite o número de linhas: '))
m=int(input('Digite o número de colunas: '))
a=np.zeros( (n,m) )

linha_max=0
coluna_max=0
linha_min=n
coluna_min=m
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if a[i,j]==1:
            valorL=i
            valorC=j
        if (valorL>linha_max):
            linha_max=valorL
        if (valorC>coluna_max):
            coluna_max=valorC
        if (valorL<linha_min):
            linha_min=valorL
        if (valorC<coluna_min):
            coluna_min=valorC
print(a[linha_min:linha_max+1,coluna_min:coluna_max+1])



