# -*- coding: utf-8 -*-
import numpy as np

def linhas (a):
    soma=0
    m=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=0+a[i,j]
        m.append(soma)
        soma=0
    return (m)
    
def colunas (a):
    soma=0
    m=[]
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=0+a[i,j]
        m.append(soma)
        soma=0
    return (m)

n=int(input("Digite n: "))
p=np.zeros((n,n))
for i in range(0,p.shape[0],1):
    for j in range(0,p.shape[1],1):
        p[i,j]=float(input("Digite o termo: "))
    
print(linhas(p))
print(colunas(p))
