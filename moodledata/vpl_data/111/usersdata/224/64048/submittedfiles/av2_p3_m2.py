# -*- coding: utf-8 -*-
import numpy as np

def L(A):
    L=[]
    for i in range(0,A.shape[0],1):
        soma=0
        for j in range(0,A.shape[1],1):
            soma=soma+A[i,j]
        L.append(soma)
    return(L)

def C(A):
    C=[]
    for j in range(0,A.shape[1],1):
        soma2=0
        for i in range(0,A.shape[0],1):
            soma2=soma2+A[i,j]
    return(C)

def TERMO(c):
    for i in range(0,len(c),1):
        contador=0
        for j in range(0,len(c),1):
            if c[i]==c[j]:
                contador=contador+1
        if contador==1:
            return i

def numeroo(Lista,Termo):
    for i in range(0,len(Lista),1):
        if i!=Termo:
            numeroo=Lista[Termo]-Lista[i]
            return (Numeroo)
n=int(input('Dimensão da matriz A: '))
A=np.zeros((n,n))
for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1],1):
        A[i,j]=int(input('TERMO: '))
L=L(A)
C=C(A)

v=Termo(L)
w=Termo(C)

h=A[v,w]
m=h-(numeroo(L,v))
print('%.d' %m)
print('%.d' %h)

