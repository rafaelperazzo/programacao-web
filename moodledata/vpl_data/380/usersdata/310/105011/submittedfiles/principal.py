# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
m = input('Digite a quantidade de linhas:')

n = input('Digite a quantidade de colunas:')

matriz = []

for i in range(0,m,1):

    linha = []

    for j in range(0,n,1):

    linha.append(input('Digite um elemento: '))

    matriz.append(linha)