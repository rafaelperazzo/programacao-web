# -*- coding: utf-8 -*-
teste1 = False
teste2 = False 
teste3 = False
dim = int(input('Informe a dimensão da matriz: '))
matriz = []
for i in range (dim):
    for j in range(dim):
        matriz.append(int(input('Informe o elemento %d,%d: ' % (i, j))))
atual = 0
anterior = atual
for i in range (dim):
    anterior = atual
    if anterior == atual:
        teste1 = True
    atual = sum(matriz[i])

if teste1:
    print(atual)
'''
for i in range (dim):
    anterior = atual
    if anterior == atual:
        teste1 = True
'''