# -*- coding: utf-8 -*-
import numpy as np

def linhas (a):
    soma=0
    m=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        m.append(soma)
        soma=0
    return (m)
    
def colunas (a):
    soma=0
    m=[]
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        m.append(soma)
        soma=0
    return (m)

n=int(input("Digite n: "))
p=np.zeros((n,n))
for i in range(0,p.shape[0],1):
    for j in range(0,p.shape[1],1):
        p[i,j]=float(input("Digite o termo: "))

o=linhas(p)
k=colunas(p)

soma=0
for i in range(0,len(o),1):
    for j in range(0,len(o),1):
        if i!=j:
            if o[i]==o[j]:
                soma=soma+1
    if soma==0:
        print(o[i])
    else:
        soma=0