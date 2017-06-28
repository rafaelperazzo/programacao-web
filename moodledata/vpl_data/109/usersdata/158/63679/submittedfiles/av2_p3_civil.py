# -*- coding: utf-8 -*-
import numpy as np
def linhas (x,y):
    soma=0
    for i in range(0,y.shape[1],1):
        soma=soma+y[x,i]
    return(soma)
def colunas (x,y):
    soma=0
    for i in range(0,y.shape[0],1):
        soma=soma+y[i,x]
    return(soma)
d=int(input('digite a dimensão da matriz:'))
a=int(input('digite a:'))
m=int(input('digite m:'))
q=np.zeros((d,d))
print(q)
for i in range(0,q.shape[0],1):
    for i in range(0,q.shape[1],1):
        q[i,j]=float(input('digite o termo:'))
        
print(linhas(a,q)+colunas(m,q)-(2*q[a,m])

    


