# -*- coding: utf-8 -*-
import numpy as np

n = int(input('Digite a quantidade de linhas que é igual a de colunas'))
linhas = n
colunas = n
a = np.zeros ((linhas, colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = float(input('Digite o elemento da matriz: '))
        


soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0

cont = 1

for i in range (0,a.shape[0],1):
    if i == 0:
        for j in range (0,a.shape[1],1):
            soma1 = soma1 + a[i,j]
            
    else: 
        for j in range (0,a.shape[1],1):
            soma2 = soma2 + a[i,j]
        if soma2 == soma1:
            cont = cont + 1
        soma2 = 0
        
print (cont)

for i in range (0,a.shape[1],1):
    for j in range (0,a.shape[1],1):
        soma3 = soma3 + a[i,j]
        if soma3 == soma1:
            cont = cont + 1
        soma3 = 0
print (cont)

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if i == j:
            soma4 = soma4 + a[i,j]
            if soma4 == soma1:
                cont = cont + 1
            soma4 = 0
print (cont)

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        
        if i + j == n - 1:
            soma5 = soma5 + a[i,j]
            if soma5 == soma1:
                cont = cont +1
            soma5 = 0
print (cont)

if cont == (2*n) + 2:
    print ('S')
else:
    print ('N')