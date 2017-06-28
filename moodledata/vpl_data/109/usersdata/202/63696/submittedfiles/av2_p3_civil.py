# -*- coding: utf-8 -*-
import numpy as np
def linhas (x,y):
    soma=0
    for a in range (0,y.shape[1],1):
        soma=soma+y[x,a]
    return(soma)
    
def colunas (x,y):
    soma=0
    for b in range (0,y.shape[0],1):
        soma=soma+y[b,x]
    return(soma)
    
tm=int(input('tamanho da matriz:'))
x1=int(input('valor:'))
y1=int(input('valor:'))
q=np.zeros((tm,tm))
print(q)
for i in range (0,q.shape[0],1):
    for j in range (0,q.shape[1],1):
        q[i,j]=float(input('termo:'))
nmr=(linhas(x1,q)+colunas(y1,q)-(2*q[x1,y1]))
print('%d'%valor)
    