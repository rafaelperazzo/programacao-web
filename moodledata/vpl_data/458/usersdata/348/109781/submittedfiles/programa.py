# -*- coding: utf-8 -*-
while True :
    n = int(input('infome o tamanho da matriz: '))
    if n >= 2:
        break
    
#matriz principal
matriz = []
for i in range (n):
    linhas = []
    for j in range (n):
        linhas.append(int(input('informe os elementos: ')))
    matriz. append(linhas)
#matriz transposta 
mt = []
for i in range (n):
    linhas = []
    for j in range (n):
        linhas.append(matriz[j][i])
    mt.append(linhas)
    
soma = 0

for i in range (n):
    for j in range (n):
        if (sum(matriz[i]) -matriz[i][j]) - (sum(mt[j]) - matriz[i][j]) > soma:
            soma = (sum(matriz[i]) -matriz[i][j]) - (sum(mt[j]) - matriz[i][j])
print(soma)