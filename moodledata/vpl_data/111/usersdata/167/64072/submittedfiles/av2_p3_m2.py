# -*- coding: utf-8 -*-
import numpy as np
def n(a):
    s1=0
    s2=0
    s3=0
    for i in range (0,b.shape[0],1):
        s1=s1+b[i,0]
        s2=s2+b[i,1]
        s3=s3+b[i,2]
    if s1==s2:
        n=s1
    else:
        n=s3
    return n
def lE(b,n):
    lista=[]
    for i in range(0,b.shape[0],1):
        s=0
        for i in range(0,b.shape[1],1):
            s=s+b[i,j]
        lista.append(s)
    for i in range(0,len(lista),1):
        if lista[i]!=n:
            return i
def cE(b,n):
    lista=[]
    for j in range(0,b.shape[0],1):
        s=0
        for i in range(0,b.shape[0],1):
            s=s+b[i,j]
        lista.append(soma)
    for i in range(0,len(lista),1):
        if lista[i]!=m:
            j=i
        return j
def vC(b,x,y,n):
    s1=0
    s2=0
    for i in range(0,b.shape[0],1):
        s1=s1+b[i,y]
    for j in range(0,b.shape[1],1):
        s2=s2+b[x,j]
    z=s1+s2-(2*b[x,y])
    valor=n-(z/2)
    return valor
n=int(input('digite o tam da matriz:'))

w=np.zeros((n,n))
for i in range(0,w.shape[0],1):
    for j in range(0,w.shape[1],1):
        r[i,j]=int(input('digite o el:'))
        n=n(w)
        x=lE(w,n)
        y=cE(w,n)
        resultado=vC(w,x,y,n)

print('%.f'%resultado)
print('%.f'%r[x,y])



