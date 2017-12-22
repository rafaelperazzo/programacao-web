# -*- coding: utf-8 -*-
#CRIANDO A MATRIZ DO TABULEIRO QUADRADO
N = int(input("Digite a dimensão do tabuleiro quadrado: "))
while N<3:
    N = int(input("Digite a dimensão do tabuleiro quadrado: "))
matriz = []
for i in range (0,N,1):
    linha = []
    for j in range (0,N):
        linha.append(int(input("Digite um valor para o tabuleiro: ")))
    matriz.append(linha)
#SOMANDO OS ELEMENTOS DE CADA LINHA:
soma_L = []
for i in range (0,N,1):
    cont1 = 0
    for j in range (0,N,1):
        cont1 += matriz[i][j]
    soma_L.append(cont1)
#SOMANDO OS ELEMENTOS DE CADA COLUNA:
soma_C = []
for j in range (0,N,1):
    cont2 = 0
    for i in range (0,N,1):
        cont2 += matriz[i][j]
    soma_C.append(cont2)
#VERIFICANDO PESO MAXIMO (soma_total):
soma_total = 0
for i in range (0,N,1):
    for j in range (0,N,1):
        if soma_total < (soma_L[i] + soma_C[j] - 2*matriz[i][j]):
            soma_total = soma_L[i] + soma_C[j] - 2*matriz[i][j]
print (soma_total)





















