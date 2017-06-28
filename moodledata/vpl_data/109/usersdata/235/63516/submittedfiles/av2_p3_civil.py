# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite o numero de n:'))
indice=float(input('digite o indice:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('digite os valores:'))
indiceh=indice//10
indicev=indice%10
soma=0
linha=indiceh
coluna=indicev

for i in range(0,a.shape[0],1):
    soma=soma+
    for j in range(0,a.shape[1],1):
    soma1=soma1+a[indicev,j]
print(a)
print(soma)
print(soma1)



