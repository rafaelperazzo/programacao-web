# -*- coding: utf-8 -*-
matriz=[]
n=int(input('digite n da matriz quadrada: '))
c=int(input('digite a quantidade de cidades: '))
while c<2:
    c=int(input('digite a quantidade de cidades: '))
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input('digite os valores da matriz: ')))
    matriz.append(linha)
print(matriz)
listaint=[]
for i in range (c):
    listaint.append(int(input('digite os intinerarios: ')))
print(listaint)

    
        
        
    
