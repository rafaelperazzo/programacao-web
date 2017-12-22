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
soma = 0

cont = 0
cont1 = 0
cont2 = 0
magico = 0

for i in range (0,a.shape[0],1):
    if i == 0:
        for j in range (0,a.shape[1],1):
        soma1 = soma1 + a[i,j]

    else: 
        for j in range (0,a.shape[1],1):
        soma2 = soma2 + a[i,j]
        if soma2 == soma1:
            cont = cont + 1

for i in range (0,a.shape[1],1):
    if i == 0:
        for j in range (0,a.shape[0],1):
        soma3 = soma3 + a[i,j]

    else: 
        for j in range (0,a.shape[1],1):
        soma4 = som4 + a[i,j]
        if som3 == soma4:
            cont1 = cont1 + 1
    
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if i == j:
            soma = soma + a[i,j]
            cont2 = cont2 + 1
            
        
if cont == a.shape [1]:
    magico = magico + 1

elif cont1 == a.shape [0]:
    magico == magico + 1
    
elif cont2 == a.shape [0]:
    magico == magico + 1
    
if magico == 3:
    print ('S')
else:
    print ('N')