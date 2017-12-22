# -*- coding: utf-8 -*-
teste1 = False
teste2 = False 
teste3 = False
dim = int(input('Informe a dimensão da matriz: '))
matriz = []
for i in range (dim):
    matriz.append([])
    for j in range(dim):
        matriz[i].append(int(input('Informe o elemento %d,%d: ' % (i, j))))
atual = 0
anterior = atual
for i in range (dim):
    print(matriz[i])
    anterior = atual
    if anterior == atual:
        teste1 = True
    atual = sum(matriz[i])
atual = 0
for i in range (dim):
    anterior = atual
    if anterior == atual:
        teste2 = True
    soma = 0
    for j in range (dim):
        soma += matriz[dim][j]
    atual = soma
        
    
if teste1 and teste2:
    print('S')
else:
    print('N')
