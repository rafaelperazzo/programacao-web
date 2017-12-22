# -*- coding: utf-8 -*-
i=0
j=0
M= int(input('Digite o número de linhas: '))
N= int(input('Digite o número de colunas: '))
m=[]
for i in range(0,M,1):
    m[i][j] = float(input('Digite: ' % ((j+1),(i+1))))
    for j in range(0,N,1):
        m.append(float(input('digite: ')))