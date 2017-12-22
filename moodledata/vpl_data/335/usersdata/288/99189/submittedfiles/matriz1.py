# -*- coding: utf-8 -*-
matriz=[]
m=int(input('Digite a quantidade de linhas (m): '))
n=int(input('Digite a quantidade de colaunas (n): '))
for i in range (0,m,1):
    linha=[]
    for j in range (0,m,1):
        linha.append(int(input('Digite um binario[0,1] : '))
    matriz.append(linha)


indice_superior=m-1
indice_inferior=0
indice_direito=n-1
indice_esquerdo=0
    
for i in range (0,m,1):
    encontrou_na _linha = False 
    for j in range (0,n,1):
        if matriz[i][j] == 1:
            encontrou_na_linha = True
            if j<indice_esquerdo:
                indice_esquerdo = j
            if j>indice_direito:
                indice_direito = j
    if 
    
