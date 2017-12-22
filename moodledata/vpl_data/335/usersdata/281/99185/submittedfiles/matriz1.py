# -*- coding: utf-8 -*-
m=int(input('Digite o número de linhas: '))
n=int(input('Digite o número de colunas: '))
matriz=[]
for i in range(0,m,1):
    linha=[]
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

