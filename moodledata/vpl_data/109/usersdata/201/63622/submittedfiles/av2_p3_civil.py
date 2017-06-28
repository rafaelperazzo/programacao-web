# -*- coding: utf-8 -*-
import numpy as np
def Linhas(x,y):
    soma=0
    for r in range(0,y.shape[1],1):
        soma=soma+y[x,r]
    return(soma)
    
def colunas(x,y):
    soma=0
    for p in range(0,y.shape[0],1):
        soma=soma+y[p,x]
    return(soma)
    
t=int(input('Informe o tamanho da matriz:'))
x1=int(input('Informe um valor:'))
y1=int(input('Informe um valor:'))
q=np.zeros((t,t))
print(q)
for i in range(0,q.shape[0],1):
    for j in range(0,q.shape[1],1):
        q[i,j]=float(input('Digite o termo:'))
        
print('%d' (Linhas(x1,q)+colunas(y1,q)-(2*q[x1,y1]))


