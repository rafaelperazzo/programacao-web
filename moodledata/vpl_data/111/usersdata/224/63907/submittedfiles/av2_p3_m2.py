# -*- coding: utf-8 -*-
import numpay as np
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
def termoNumero(c):
    for i in range(0,len(c),1):
        contador=0
        for j in range(0,len(c),1):
            if c[i]==c[j]:
                contador=contador+1
        if contador==1:
            return i
def numeroOriginal(lista,termoNumero):
    for i in range(0,len(lista),1):
        if i!=termoNumero:
            numeroOriginal=lista[termoOriginal]-lista[i]
            return NumeroOriginal
n=int(input('Dimensão da matriz A: '))
A=np.zeros((n,n))
for i in range(0,A.shape[0],1):
    for j in range(0,A.SHAPE[1],1):
        A[i,j]=int(input('TERMO: '))
Linhas=L(A)
Colunas=C(A)

v=termoNumero(Linhas)
w=TermoNumero(Colunas)

h=[v,w]
m=h-(numeroOriginal(Linhas,v))
print('%.d'%m)
print('%.d'%h)

