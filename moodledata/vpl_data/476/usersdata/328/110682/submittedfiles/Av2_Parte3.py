# -*- coding: utf-8 -*-
qa=int(input('Quantidade de elementos de a:'))
qb=int(input('Quantidade de elementos de b:'))
a=[]
b=[]
for i in range(qa):
    lista=[]
    for j in range (qa):
        lista.append(float(input('Elementos de a:')))
    a.append(lista)
for i in range(qb-1):
    lista=[]
    for j in range (qb):
        lista.append(float(input('Elementos de b:')))
    b.append(lista)
print(a)
print(b)
