# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de linhas:'))
n=int(input('Digite a quantidade de colunas:'))
mt=[]
for i in range(m):
    linhas=[]
    for j in range(n):
        linhas.append(int(input('Adicione:')))
    mt.append(linhas)

clone = []
for i in range(m):
    clone.append([])
    for j in range(n):
        clone[i].append(mt[m-1-i][n-1-i])
        
print(clone)
