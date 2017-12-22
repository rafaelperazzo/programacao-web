# -*- coding: utf-8 -*-
matriz=[]
cont=0
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)    
# analisar linhas
for i in range(1,len(matriz)-1,1):
    if sum(matriz[i-1])==sum(matriz[i]):
        cont+=0
    else:
        cont+=1
        break
# analisar colunas
'''c=[]
for k in range(0,n,1):
    primeira=[]
    for i in range(0,n,1):
        segunda=[]
        for j in range(0,n,1):
            segunda.append(matriz[i][j])
        primeira.append(segunda)
    c.append(primeira)
for i in range(1,len(c)-1,1):
    if sum(c[i-1])==sum(c[i]):
        cont+=0
    else:
        cont+=1
        break'''
#diagonais
diagonalp=[]
for i in range(0,n,1):
    diagonalp.append(matriz[i][i])
    
diagonal2=[]
for i in range(0,n,1):
    diagonal2.append(matriz[i][len(matriz)-1-i])

if diagonal2==diagonalp:
    cont+=0
else:
    cont+=1
    
if cont==0:
    print('S')
else:
    print('N')




