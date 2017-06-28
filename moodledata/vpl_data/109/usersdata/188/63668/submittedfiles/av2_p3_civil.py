# -*- coding: utf-8 -*-
import numpy as np
def linhas (l,c):
    soma=0
    for i in range(0,c.shape[1],1):
        soma=soma+c[l,i]
    return(soma)
    
def colunas (l,c):
    soma=0
    for i in range(0,c.shape[0],1):
        soma+soma+c[i,l]
    return(soma)
    
d=int(input('Digite a dimensão da matriz:'))
x=int(input('Digite X:'))
y=int(input('Digite Y:'))
t=np.zeros((d,d))
print(t)
for i in range(0,t.shape[0],1):
    for j in range(0,t.shape[1],1):
        t[i,j]=float(input('Digite o valor:'))
        
print(linhas(x,t)+colunas(y,t)-(2*t[x,y]))

