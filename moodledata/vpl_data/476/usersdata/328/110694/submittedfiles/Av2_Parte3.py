# -*- coding: utf-8 -*-
n=int(input('Quantidade de elementos de a:'))
m=int(input('Quantidade de elementos de b:'))
a=[]
b=[]
for i in range(n):
    lista=[]
    for j in range (n):
        lista.append(float(input('Elementos de a:')))
    a.append(lista)
#for i in range(qb-1):
    lista=[]
    for j in range (qb):
        lista.append(float(input('Elementos de b:')))
    b.append(lista)
print(a)
print(b)
