# -*- coding: utf-8 -*-
import numpy as np
def diagonal (a):
    for i in range (0,a.shape[0],1):
        slinhas=[0]
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        slinhas.append(soma)
    i=0
    j=a.shape[1]
    cont=1
    while j>=0:
        if a[i,j]>soma[i]:
            cont=cont+1
    if cont==a.shape[0]:
        return True
    else:
        return False
n=int(input('digite a quantidade de linhas:'))
a=np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('digite o elemento da sua matriz:'))
print(diagonal(a))        