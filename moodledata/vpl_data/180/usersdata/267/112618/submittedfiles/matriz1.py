# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Número de linhas: '))
m=int(input('Número de colunas: '))
a=input('Digite a Matriz como uma única linha: ')

#PREPARANDO A ENTRADA
A = np.fromstring(a, sep=' ').reshape(n, m)

#FUNÇÕES
def primeiraL(x):
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]>0:
                return(i+1)

def primeiraC(x):
    for j in range(0,x.shape[1],1):
        for i in range(0,x.shape[0],1):
            if x[i,j]>0:
                return(j+1)

def finalL(x):
    final=0
    for i in range(0,x.shape[0],1):
        for j in range(0,x.shape[1],1):
            if x[i,j]>0:
                final=(i+1)
    return(final)

def finalC(x):
    for j in range(0,x.shape[1],1):
        for i in range(0,x.shape[0],1):
            if x[i,j]>0:
                final=(j+1)
    return(final)


#PROGRAMA
print(A)
print('PRIMEIRA LINHA: ')
print(primeiraL(A))
x0=(primeiraL(A))
print('PRIMEIRA COLUNA: ')
print(primeiraC(A))
xn=(primeiraC(A))
print('ÚLTIMA LINHA: ')
print(finalL(A))
y0=(finalL(A))
print('ÚLTIMA COLUNA: ')
print(finalC(A))
yn=(finalC(A))

b=A[x0:xn,y0:yn]
print('NOVA MATRIZ: ')
print (b)