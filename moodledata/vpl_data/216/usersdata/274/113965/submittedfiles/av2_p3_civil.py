# -*- coding: utf-8 -*-
import numpy as np
L=int(input("Quantidade de Linhas: "))
C=L
a=np.zeros((L.C))

x=int(input("Linhas: "))
y=int(input("Colunas: "))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input("Valor da Linha: "))

soma1L=0
for i in range(x,C-y,1):
    soma1L=soma1L+a[x,i+1]
    
soma2L=0
for i in range(x,y,1):
    soma2L=soma2L+a
    
soma1C=0
for i in range(x,C-y,1):
    soma1C=soma1C+a[x,i+1]
