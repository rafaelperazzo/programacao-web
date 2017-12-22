# -*- coding: utf-8 -*-
matriz=[]
m=int(input('digite a quantidade de linhas:'))
n=int(input('digite a quantidades de colunas: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('digite os valores:')))
    matriz.append(linha)


i_s=m-1
i_i=0
i_e=0
i_d=n-1

for i in range(0,m,1):
    encontrou_na_linha=False
    for j in range(0,n,1)


