# -*- coding: utf-8 -*-
n = int(inpu('informe o valor do tamamnho da matriz: '))

matriz = []
for i in range (n):
    linhas = []
    for j in range(n):
        linhas.append(int(input('informe os elementos : ')))

#soma de linhas
k = 0 
for i in range (n):
    s = 0
    for j in range (n):
        s = s matriz[i][j]
    if k < s:
        k = s 
        
        
