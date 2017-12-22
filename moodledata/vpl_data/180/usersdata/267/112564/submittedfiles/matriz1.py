# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Número de linhas: '))
m=int(input('Número de colunas: '))
a=input('Digite a Matriz como uma única linha: ')

#PREPARANDO A ENTRADA
A = np.fromstring(a, sep=' ').reshape(n, m)
print(A)
'''
#PROGRAMA
b=A[x0:xn,y0:yn]
'''