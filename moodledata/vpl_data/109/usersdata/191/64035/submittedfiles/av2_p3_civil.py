# -*- coding: utf-8 -*-
import numpy as np

def linhas(a,b):
    soma=0
    for c in range(0,b.shape[1],1):
        soma=soma+b[a,c]
    return(soma)
    
def colunas(a,b):
    soma=0
    for d in range(0,b.shape[0],1):
        soma=soma+b[d,a]
    return(soma)
    
tm=int(input('dimensao da matrix:'))
x1=int(input('digite o valor de a1:'))
y1=int(input('digite o valor de b2:'))
q=np.zeros((tm,tm))
print(q)
for i in range(0,q.shape[0],1):
    for j in range(0,q.shape[1],1):
        q[i,j]=float(input('termo:'))
nmr=(linhas(x1,q)+colunas(y1,q)-(2*q[x1,y1]))
print('%.d'%nmr)




