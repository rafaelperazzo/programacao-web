# -*- coding: utf-8 -*-
import numpy as np
def soma(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return(soma)
    
linhas=int(input('digite a quantidade de linhas: '))
a=np.zeros((linhas,linhas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('digite os valores da matriz: '))
i=linhas
print(a)
print(soma(linhas,i))