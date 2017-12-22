# -*- coding: utf-8 -*-
matriz=[]
cont=0
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)    
    
#linha
for i in range(1,len(matriz)-1,1):
    if sum(matriz[i-1])==sum(matriz[i]):
        cont+=0
    else:
        cont+=1
#coluna
coluna=[]
for i in range(0,len(matriz)-1,1):
    for j in range(0,len(matriz)-1,1):
        coluna[i].append(matriz[j])
print(coluna)
'''
for i in range(1,len(coluna)-1,1):
    if sum(coluna[i-1])==sum(coluna[i]):
        cont+=0
    else:
        cont+=1
#diagonais
diagonalp=[]
for i in range(0,n,1):
    diagonalp.append(matriz[i][i])
diagonal2=[]
for i in range(0,n,1):
    diagonal2.append(matriz[i][len(matriz)-1-i])
if sum(diagonalp)==sum(diagonal2):
    cont+=0
else:
    cont+=1
if cont==0:
    print('S')
else:
    print('N')'''