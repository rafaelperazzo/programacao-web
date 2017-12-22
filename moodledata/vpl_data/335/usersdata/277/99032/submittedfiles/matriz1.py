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
print(matriz)