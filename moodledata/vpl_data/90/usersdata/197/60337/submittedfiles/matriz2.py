# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o numero de linhas e colunas:'))
a=np.zeros((n,n))
for i in range (0, a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('Digite o valor:'))
def somalinha (a):
    soma=0
    lista=[]
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            while j<=shape[1]:
                soma=soma+a[i,j]
                j=j+1
                lista.append(soma)
    retunr (lista)
print(somalinha(a))
            
    

    

