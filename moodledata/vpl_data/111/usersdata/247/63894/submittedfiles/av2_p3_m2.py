# -*- coding: utf-8 -*-
import numpy as np
def linha(a):
    b=[ ]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
    return b
def coluna(a):
    d=[ ]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        d.append(soma)       
    return d
n=int(input('dimensao: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('x: '))
x=linha(a)
y=coluna(a)
r=0
t=0
soma=0
for i in range(0,len(x),1):
    for j in range(0,len(x),1):
        if i!=j:
            if x[i]==x[j]:
                soma=soma+1
    if soma==0:
        r=x.index(x[i])
        break
    else:
        soma=0
for i in range(0,len(y),1):
    for j in range(0,len(y),1):
        if i!=j:
            if y[i]==y[j]:
                soma=soma+1
    if soma==0:
        t=y.index(y[i])
        break
    else:
        soma=0
if t!=0:
    k=((y[t+1]-y[t])+a[r,t])
else:
    k=((y[t+1]-y[t])+a[r,t])
print(k)
print(a[r,t])