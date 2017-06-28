# -*- coding: utf-8 -*-
import numpy as np
def linhas(a,m):
    soma=0
    for i in range(0,m.shape[1],1):
        soma=soma+m[a,i]
    return(soma)
    
def colunas(a,m):
    soma=0
    for i in range(0,m.shape[0],1):
        soma=soma+m[i,a]
    return(soma)
h=int(input('digite a dimensão da matriz:'))
x=int(input('digite x:'))
y=int(input('digite y:'))
q=np.zeros((h,h))
print(q)
for i in range(0,q.shape[0],1):
    for j in range(0,q.shape[1],1):
        q[i,j]=float(input('digite o termo:'))
print(linhas(x,q)+colunas(y,q)-(2*q[x,y]))

