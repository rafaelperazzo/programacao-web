# -*- coding: utf-8 -*-
import sort
n=int(input('Digite a quantidade de termos da lista1:'))
lista1=[]
for i in range(0,n,1):
    lista1.append(int(input('Digite um termo:')))

x= lista1.sort()
print(lista1)
print(x)
