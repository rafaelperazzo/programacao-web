# -*- coding: utf-8 -*-
import numpy as np
def linhas (a,m):
    l=[]
    soma=0
    for i in range (0,m.shape[0],1):
        for j in range(0,m.shape[1],1):
            soma=0+m[i,j]
        l.append(soma)
        soma=0
    return (l)
    
def colunas (a,m):
    c=[]
    soma=0
    for j in range (0,m.shape[1],1):
        for i in range(0,m.shape[0],1):
            soma=0+m[i,j]
        c.append(soma)
        soma=0
    return(c)
    
    
h=int(input("Digite a dimensao da matriz: "))
x=int(input("Digite x"))
y=int(input("Digite y"))
q=np.zeros((h,h))
print(q)
for i in range(0,q.shape[0],1):
    for j in range(0,q.shape[1],1):
        q[i,j]=float(input("Digite o termo: "))
        
print(linhas(x,q))
print(colunas(y,q))

                

