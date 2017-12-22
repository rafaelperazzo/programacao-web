# -*- coding: utf-8 -*-
import numpy as np

n= int(input('digite a quantidade de linhas e colunas: '))

m=n

a=np.zeros((n,m))

for i in range(0,n,1):
    for j in range(0,m,1):
        a[i,j]=float(input('digite os elemntos: '))
        
soma=0
cont=0

for i in range(0,n,1):
    for j in range(0,m,1):
        soma=soma+a[i,j]
    
    if soma-a[i,j]<a[i,i]:
        cont=cont+1
    soma=0
if cont==n:
    print('SIM')
else:
    print('NAO')