# -*- coding: utf-8 -*-
m = int(input('insira a quantidade de linhas: '))
n = int(input('insira a quantidade de colunas: '))

matriz = []
for i in range (0,m,1):
    l = []
    for i in range (0,n,1):
        l.append(0)
    matriz.append(l)
    
for i in range (-1,m-1,-1):
    for i in range (-1,n-1,-1):
        matriz.append(int(input('digite valor: ')))
        
print (matriz)


