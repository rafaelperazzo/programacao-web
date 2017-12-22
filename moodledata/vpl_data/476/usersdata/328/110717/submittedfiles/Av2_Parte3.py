# -*- coding: utf-8 -*-
n=int(input('Quantidade de elementos de a:'))
m=int(input('Quantidade de elementos de b:'))
a=[]
b=[]
for i in range(n-1):
    lista=[]
    for j in range (n-1):
        lista.append(float(input('Elementos de a:')))
    a.append(lista)
for i in range(m-1):
    lista=[]
    for j in range (m-1):
        lista.append(float(input('Elementos de b:')))
    b.append(lista)
print(a)
print(b)
