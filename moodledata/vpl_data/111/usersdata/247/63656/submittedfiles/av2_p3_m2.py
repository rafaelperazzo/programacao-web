# -*- coding: utf-8 -*-
import numpy as np
def linha(a):
    x=0
    b=[ ]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
    for i in range(0,len(b)-1,1):
        if b[i]!=b[i+1]:
            x=x+i
    return x
def coluna(a):
    d=[ ]
    y=0
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        d.append(soma)       
    for i in range(0,len(d)-1,1):
        if d[i]!=d[i+1]:
            y=y+i
    return y
n=int(input('dimensao: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('x: '))
x=linha(a)
y=coluna(a)
print(x,y)
