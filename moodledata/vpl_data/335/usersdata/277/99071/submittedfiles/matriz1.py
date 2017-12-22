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
indice_inferior = 0
indice_esquerdo = 0
indice_direito = 0

for i in range(0,m,1):
    encontrou_na_linha = False
    for j in range(0,n,1):
        if matriz[i][j] == 1:
            encontrou_na_linha = True
            if j<indice_esquerdo :
                indice_esquerdo = j
            if j>indice_direito :
                indice_direito = j
    if encontrou_na_linha :
        if i<indice_superior:
            indice_superior = i
        if i>indice_inferior:
            indice_inferior = i
            
print(indice_superior)
print(indice_inferior)
print(indice_esquerdo)
print(indice_direito)