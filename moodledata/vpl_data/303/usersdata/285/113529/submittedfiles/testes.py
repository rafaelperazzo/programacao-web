# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import numpy as np
mt=[]
m = int(input('insira a linha: '))
n = int(input('insira a coluna: '))
a = np.zeros((m,n))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('insira os termos da matriz: ')))
    mt.append(linha)
print(mt)

b=[]
for i in range(0,mt.shape[0],1):
    soma = 0
    for j in range(0,mt.shape[1],1):
        soma = soma + mt[i][j]
    b.append(soma)
print(b)        