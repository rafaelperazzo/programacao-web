# -*- coding: utf-8 -*-
m = int(input('Digite a qtd de colunas: '))

n = int(input('Digite a qtd de linhas: '))

M = []

for i in range(1,m+1,1):

    L = []

    for j in range(1,n+1,1):

        L.append(int(input('Digite um valor: ')))

    M.append(L)

for i in range(0,m,1):

    for j in range(0,n,1):

        if M[i][j]>10:

            print (M[i][j])