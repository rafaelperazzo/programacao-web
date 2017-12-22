# -*- coding: utf-8 -*-
def transposta (matriz):
    
    
    
n = int(input('Digite a quantidade de linhas da matriz: '))
m = int(input('Digite a quantidade de colunas da matriz: '))

matriz=[]
for l in range (0, n, 1):
    linha=[]
    for i in range (0, m, 1):
        linha.append(int(input('Digite um elemento para a matriz: ')))
    matriz.append(linha)

for i in range (len(matriz)-1, -1, -1):
    cont=0
    for k in range (0, len(matriz[i]), 1):
        if matriz[i][k]==0:
            cont+=0
        if not matriz[i][k]==0:
            cont+=1
    if cont==0:
        del matriz[i]
    if not cont==0:
        break

comp=[]
for i in range (len(matriz)-1, -1, -1):
    cont=0
    for k in range (0, len(matriz[i]), 1):
        if matriz[i][k]==0:
            cont+=0
        if not matriz[i][k]==0:
            cont+=1
    if cont==0:
        comp.append(i)
    if not cont==0:
        continue

for t in range (0, len(comp), 1):
    h=comp[t]
    del matriz[h]


    
print(matriz)
    











