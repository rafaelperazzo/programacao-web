# -*- coding: utf-8 -*-
tamanho = int(input('Digte o tamnha da matriz: '))



matriz=[]

for i in range(tamanho):
    linhas=[]
    for j in range(tamanho):
        linhas.append(int(input('Digite os elementos da linha: ')))
    matriz.append(linhas)
    

print(matriz)
