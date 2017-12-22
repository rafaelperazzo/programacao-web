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

for i in range (0, len(matriz), 1):
    cont=0
    for k in range (0, len(matriz[i]), 1):
        if matriz[i][k]==0:
            cont+=0
        if not matriz[i][k]==0:
            cont+=1
    if cont==0:
        continue
    if not cont==0:
        limsup=i
        break

for i in range (len(matriz)-1, -1, -1):
    cont=0
    for k in range (0, len(matriz[i]), 1):
        if matriz[i][k]==0:
            cont+=0
        if not matriz[i][k]==0:
            cont+=1
    if cont==0:
        continue
    if not cont==0:
        liminf=i
        break
    
for i in range (0, m, 1):
    for j in range (0, n, 1):
        if matriz[j][i]==0:
            continue
        if not matriz[j][i]==0:
            limesq=i
            break

for i in range (m-1, -1, -1):
    for j in range (0, n, 1):
        if matriz[j][i]==0:
            continue
        if not matriz[j][i]==0:
            limdir=i
            break

for i in range (n-1, -1, -1):
    if i>liminf:
        del matriz[i]
    if not i>liminf:
        break

for i in range (m-1, -1, -1):
    if i>limdir:
        for j in range (0, len(matriz), 1):
            del matriz[j][i]
    if not i>limdir:
        break

for i in range (len(matriz)-1, -1, -1):
    if i<limsup:
        del matriz[i]
    if not i<limsup:
        break
    
h=len(matriz[0])
for i in range (h-1, -1, -1):
    if i<limesq:
        for j in range (0, len(matriz), 1):
            del matriz[j][i]
    if not i<limesq:
        break

print(matriz)