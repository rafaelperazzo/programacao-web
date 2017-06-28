# -*- coding: utf-8 -*-
import numpy as np
def linhas (b,c):
    soma=0
    for i in range(0,c.shape[1],1):
        soma=soma+c[b,i]
    return(soma)
    
def colunas (b,c):
    soma=0
    for i in range(0,c.shape[0],1):
        soma=soma+c[i,b]
    return(soma)
    
d=int(input('digite a dimensão da matriz:'))
x=int(input('digite x:'))
y=int(input('digite y:'))
q=np.zeros((d,d))
print(q)
for i in range(0,q.shape[0],1):
    for j in range(0,q.shape[1],1):
        q[i,j]=float(input('digite o termo:'))
        
valor=(linhas(x,q)+colunas(y,q)-(2*q[x,y]))
print('%.d' %valor)