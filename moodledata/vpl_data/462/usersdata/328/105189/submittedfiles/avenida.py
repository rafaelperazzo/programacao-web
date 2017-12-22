# -*- coding: utf-8 -*-
m=int(input('Digite M no sentido Norte-Sul:))
n=int(input('Digite N no sentido Leste-Oeste:))
mn=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(float(input('Insira valores:')))
    mn.append(l)
print (mn)