# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite o numero de n:'))
indicel=float(input('digite o indice:'))
indicec=float(input('digite o indice:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=float(input('digite os valores:'))
        
        

coluna=indicec
soma=0
for i in range(0,a.shape[0],1):
    soma=soma+a[i,coluna]
    
    
linha=indicel
soma1=0
for j in range(0,a.shape[1],1):
    soma1=soma1+a[linha,j]

    
print(a)
print(soma)
print(soma1)



