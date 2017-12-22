# -*- coding: utf-8 -*-

import numpy as np

soma = 0 
pesos  []
a = np.zeros ((dimensao,dimensao))

dimensao = int (input('Digite a dimensão do tabuleiro:'))

for i in range  (0,dimensao,1):
    for j in range (0,dimensao,1):
        a[i,j] = int (input('Digite o elemento da matriz:'))
        
for i in range  (0,dimensao,1):
    for j in range (0,dimensao,1):
        soma = soma + a[i,j] + a[j,i]
        pesos.append (soma)
    soma = 0

indice_maior = pesos.index (max(pesos))

cont = 0

for i in range (0,dimensao,1):
    for j in range (0,dimensao,1):
        valor = a[i,j]
        cont = cont + 1
        if cont == indice_maior:
            break
        
print ((max(pesos)-valor))