# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de linhas:'))
n=int(input('Digite a quantidade de colunas:'))
mt=[]
for i in range(m):
    linhas=[]
    for j in range(n):
        linhas.append(int(input('Adicione:')))
    mt.append(linhas)
print(mt)

