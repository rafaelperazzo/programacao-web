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
                return(i)


#PROGRAMA
print(primeiraL(A))
'''
b=A[x0:xn,y0:yn]
'''