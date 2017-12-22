# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de linhas:'))
n=int(input('Digite a quantidade de colunas:'))
mt=[]
for i in range(m,0,-1):
    linhas=[]
    for j in range(n,0,-1):
        linhas.append(float(input('Adicione:')))
    mt.append(linhas)
print(mt)

