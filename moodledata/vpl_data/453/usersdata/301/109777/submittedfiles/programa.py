# -*- coding: utf-8 -*-
import numpy as np
m=[]
n=int(input('digite o tamanho da matriz:  '))
while not n>=3:
    n= int(input('digite o tamanho da matriz:  '))
for i in range(0,n,1):
    linhas=[]
    for j in range(0,n,1):
        linhas.append(int(input(digite os valores da matriz: ')))
    m. append(linhas)
ntrans=np.empty([n,n])
for j in range(0,n,1):
    for i in range(0,n,1):
        ntrans[j][i]=m[i][j]
soma=sum(m[0])+sum(ntrans[0]) -2*(m[0][0])
for i in range(0,n,1):
    for j in range(0,n,1):
        if soma>sum(m[i])+sum(ntrans[j]) -2*(m[i][j]):
            soma =soma
    else:
        soma=sum(m[i])+sum(ntrans[j]) -2*(m[i][j]):
print(int(soma))

