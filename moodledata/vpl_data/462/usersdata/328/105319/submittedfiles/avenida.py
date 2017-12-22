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
        l.append (int(input('Insira valores entre 1 e 100000000 de reais:')))
    mn.append(l)
mt
for i in range(n):
    l=[]
    for j in range(m):
        l.append (mn[j][i])
som=1000
for i in range (n):
    if sum(mn[i])< som:
        som=sum(mn[i])

print (som)

