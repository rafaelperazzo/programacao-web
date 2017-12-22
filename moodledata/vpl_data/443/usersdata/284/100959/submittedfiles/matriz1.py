# -*- coding: utf-8 -*-
a=[]
b=[]
m=int(input('digite o numero de linhas: '))
n=int(input('digite o numero de colunas: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite um valor: ')))
    a.append(linha)
for linha in matriz:
    linha.reverse()
matriz.reverse()
print(m)