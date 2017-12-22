# -*- coding: utf-8 -*-
n=int(input('numero de linhas e colunas: '))

mp=[]
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input('numeros para a matriz: ')))
    mp.append(linha)
    
print(mp)
