# -*- coding: utf-8 -*-
matriz=[]
m=int(input('casa na horizontal: '))
n=int(input('casa na vertical: '))
for i in range(0,m,1):
    bairro=[]
    for j in range(0,n,1):
        bairro.append(int(input('valor da casa: ')))
    matriz.append(bairro)
print(matriz)