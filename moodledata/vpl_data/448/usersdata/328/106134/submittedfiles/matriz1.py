# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de linhas:'))
n=int(input('Digite a quantidade de colunas:'))
m=[]
for i in range(m):
    linhas=[]
    for j in range(n):
        linhas.append(float(input('Adicione:')))
    m.append(linhas)
print(m)

