# -*- coding: utf-8 -*-
m = int(input('insira a quantidade de linhas: '))
n = int(input('insira a quantidade de colunas: '))

matriz = []
for i in range (0,m,1):
    l = []
    for i in range (0,n,1):
        v = int(input('insira os elementos da matriz: '))
        l.append(v)
    matriz.append(l)
    
print (matriz)


