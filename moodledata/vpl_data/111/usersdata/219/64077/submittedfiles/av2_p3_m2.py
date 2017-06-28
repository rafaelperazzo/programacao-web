# -*- coding: utf-8 -*-
import numpy as np

def linhas(a):
    soma=0
    y=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        y.append(soma)
        soma=0
    return (y)

def colunas (a):
    soma=0
    y=[]
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        y.append(soma)
        soma=0
    return (y)
    
n=int(input("Digite a quantidade n:"))
p=np.zeros((n,n))
for i in range(0,p.shape[0],1):
    for j in range(0,p.shape[1],1):
        p[i,j]=float(input("Digite o termo:"))

h=linhas(p)
u=colunas(p)
m=0
w=0

soma=0
for i in range(0,len(h),1):
    for j in range(0,len(h),1):
        if i!=j:
            if h[i]==h[j]:
                soma=soma+1
    if soma==0:
        m=h.index(h[i])
        break
    else:
        soma=0
        
soma=0
for i in range(0,len(u),1):
    for j in range(0,len(u),1):
        if i!=j:
            if u[i]==u[j]:
                soma=soma+1
    if soma==0:
        w=u.index(u[i])
        break
    else:
        soma=0
if w!=0:
    t=((u[w-1]-u[w])+p[m,w])
else:
    t=((u[w+1]-u[w])+p[m,w])
print(t)
print(p[m,w])
        
        

