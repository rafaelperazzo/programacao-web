# -*- coding: utf-8 -*-
n = int(input('Digite a ordem da matriz n x n: '))

matriz=[]
for i in range (0, n, 1):
    linha=[]
    for u in range (0, n, 1):
        linha.append(int(input('Digite um elemento da matriz: ')))
    matriz.append(linha)
    
comp=[]
for i in range (0, n, 1):
    if matriz[i][i]>sum(matriz[i]):
        comp.append(True)
    if nor matriz[i][i]>sum(matriz[i]):
        comp.append(False)

cont=0        
for k in range (0, len(comp), 1):
    if comp[k]==True:
        cont+=0
    if comp[k]==False:
        cont+=1

if cont==0:
    print('S')
if not cont==0:
    print('N')
    
