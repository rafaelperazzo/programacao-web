# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import numpy as np
a=[]
m=int(input('Digite o numero de linhas: '))
n=int(input('Digite o numero de colunas: '))
m0 =np.zeros((m,n))

for i in range (0,m):
    linha=[]
    for j in range(0,n):
        linha.append(int(input('Digite os termos: ')))
    a.append(linha)
print(a)

SomaL=[]
for i in range (0,m0.shape[0]):
    soma=0
    for j in range (0,m0.shape[1]):
        soma+= a[i][j]
    SomaL.append(soma)
print (SomaL)

SomaC=[]
for j in range (0,m0.shape[1]):
    soma=0
    for i in range (0,m0.shape[0]):
        soma+= a[i][j]
    SomaC.append(soma)
print (SomaC)





