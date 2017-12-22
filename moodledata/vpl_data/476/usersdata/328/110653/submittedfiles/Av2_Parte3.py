# -*- coding: utf-8 -*-
qa=int(input('Quantidade de elementos de a:'))
qb=int(input('Quantidade de elementos de b:'))
a=[]
b=[]
for i in range(qa-1):
    lista=[]
    for j in range (qa):
        lista.append(float(input('Elementos de a:')))
    a.append(lista)
print(a)
b.append(float(input('Elementos de b:')))
