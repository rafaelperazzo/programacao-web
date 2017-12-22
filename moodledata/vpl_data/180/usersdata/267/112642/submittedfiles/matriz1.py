# -*- coding: utf-8 -*-
import numpy as np


n=int(input('Número de linhas: '))
m=int(input('Número de colunas: '))
a=np.zeros((n,m))
for i in range(0,n,1):
    for j in range(0,m,1):
        a[i,j]=input('Digite o elemento A%d%d: ' %(i,j))

#PREPARANDO A ENTRADA
#A = np.fromstring(a, sep=' ').reshape(n, m)

#FUNÇÕES
def primeiraL(x):
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]>0:
                return(i)

def primeiraC(x):
    for j in range(0,x.shape[1],1):
        for i in range(0,x.shape[0],1):
            if x[i,j]>0:
                return(j)

def finalL(x):
    final=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]>0:
                final=(i)
    return(final)

def finalC(x):
    for j in range(0,x.shape[1],1):
        for i in range(0,x.shape[0],1):
            if x[i,j]>0:
                final=(j)
    return(final)


#PROGRAMA
print(A)
print('PRIMEIRA LINHA: ')
print(primeiraL(A))
x0=(primeiraL(A))
print('PRIMEIRA COLUNA: ')
print(primeiraC(A))
y0=(primeiraC(A))
print('ÚLTIMA LINHA: ')
print(finalL(A))
xn=(finalL(A))
print('ÚLTIMA COLUNA: ')
print(finalC(A))
yn=(finalC(A))

b=A[x0:xn+1,y0:yn+1]
print('NOVA MATRIZ: ')
print (b)