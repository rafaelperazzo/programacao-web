# -*- coding: utf-8 -*-
n=int(input(''))
while n<3:
    print('erro')
    n=int(input(''))
matriz=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    matriz.append(linha)
#soma para cada elemento
somas=[]
for i in range(0,n,1):
    auxi=[]
    for j in range(0,n,1):
        auxi.append(matriz[i][j])
        auxi.append(matriz[j][i])
    somas.append(auxi)
print(somas)
