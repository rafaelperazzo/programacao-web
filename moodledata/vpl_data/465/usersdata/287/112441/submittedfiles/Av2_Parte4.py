# -*- coding: utf-8 -*-
matriz=[]
n=int(input('digite n da matriz quadrada: '))
c=int(input('digite o valor de c: '))
while c<2:
c=int(input('digite o valor de c: '))
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input('digite os valores da matriz: ')))
    matriz.append(linha)
print(matriz)
in
