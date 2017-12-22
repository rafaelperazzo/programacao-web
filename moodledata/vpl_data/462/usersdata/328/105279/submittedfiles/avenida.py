# -*- coding: utf-8 -*-
m=int(input('Digite M no sentido Norte-Sul:'))
while not 2<=m<=100:
    m=int(input('Digite M no sentido Norte-Sul:'))
n=int(input('Digite N no sentido Leste-Oeste:'))
while not 2<=n<=100:
    n=int(input('Digite N no sentido Leste-Oeste:'))
mn=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append (float(input('Insira valores entre 1 e 100000000 de reais:')))

menor=0


for i in range (m):
    som=0
    for j in range (m):
        menor= menor + m[i][j]
        som.append(menor)
print (som)

