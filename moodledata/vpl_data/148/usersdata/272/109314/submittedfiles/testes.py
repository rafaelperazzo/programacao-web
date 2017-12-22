# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import numpy as np

linhas=int(input('Digite o número de linhas: '))
colunas=int(input('Digite o número de colunas: '))
a=np.zeros( (linhas,colunas) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('Digite um valor: '))

o=[]
soma=0
for k in range (0,a.shape[1],1):
        soma=soma+a[linhas-1,k]
        o.append((soma))

print(o)

    

