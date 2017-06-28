# -*- coding: utf-8 -*
import numpy as np
n=int(input('Digite a Dimensão da Matriz:'))
ind1=int(input('Digite o indice x:'))
ind2=int(input('Digite o indice y:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um valor:'))
print(a)
    