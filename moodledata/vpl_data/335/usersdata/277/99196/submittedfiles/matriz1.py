# -*- coding: utf-8 -*-
matriz = []
m = int(input('Digite a qtd de linhas: '))
n = int(input('Digite a qtd de colunas: '))
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input('Digite um binario[0,1]: ')))
    matriz.append(linha)

indice_superior = m-1
indice_inferior = 0
indice_esquerdo = 0
indice_direito = n-1

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
            
matriz_recorte = []            
            
for i in range(indice_superior,indice_inferior+1,1):
    linha_recorte = []
    for j in range(indice_esquerdo,indice_direito+1,1):
        linha_recorte.append(matriz[i][j])
    matriz_recorte.append(linha_recorte)

print(matriz_recorte)




