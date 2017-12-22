# -*- coding: utf-8 -*-
while(True):
    n = int(input('Digite a dimensão da matriz quadrada: '))
    if n >= 3:
        break
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input('Digite o elemento %d de %d: '%((j+1),(i+1)))))
    matriz.append(linha)
linha = 0
for i in range(n):
    for j in range(n):
        if sum(matriz[i]) != sum(matriz[j]):
            linha = i
            break
        break
diferente_col = []
col = 0
for i in range(n):
    soma = 0
    for j in range(n):
        soma = soma + matriz[j][i]
    if soma == sum(diferente_col):
        diferente_col = []
    elif soma != sum(diferente_col):
        if sum(diferente_col) != 0:
            continue
        for l in range(n):
            diferente_col.append(matriz[l][i])
            col = i
lista = []
for i in range(n):
    lista.append(sum(matriz[i]))
lista = sorted(lista)
print(matriz[linha][col] +(lista[1] - sum(matriz[linha])))
print(matriz[linha][col])
