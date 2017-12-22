# -*- coding: utf-8 -*-
matriz = []
m = int(input('Digite a qtd de linhas: '))
n = int(input('Digite a qtd de colunas: '))
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input('Digite um binario[0,1]: ')))
    matriz.append(linha)
# teste
#print(matriz)
matriz_recorte = []

indice_superior = 0
indice_inferior = m-1
indice_esquerdo = 0
indice_direito = n-1

for i in range(0,m,1):
    encontrou_na_linha = False
    for j in range(0,n,1):
        if matriz[i][j] == 1:
            encontrou_na_linha = True