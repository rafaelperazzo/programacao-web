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
print(\n a)
