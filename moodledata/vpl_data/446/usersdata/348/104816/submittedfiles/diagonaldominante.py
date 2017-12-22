# -*- coding: utf-8 -*-
n = int(input('informe o tamanho da MATRIZ: '))

matriz = []
for i in range (n):
    linhas = []
    for j in range (n):
        linhas.append(int(input( 'informe os elementos: ')))
    matriz.append(linhas)

#diagonal principal
s = 0
for i in range (n):
    s = s + matriz[i][i]
    
#linhas

for i in range (n):
    n = 0
    for j in range (n):
        n = n + matriz[j][i]
    if n > s:
        print('NAO')
        exit()
print('SIM')
    
