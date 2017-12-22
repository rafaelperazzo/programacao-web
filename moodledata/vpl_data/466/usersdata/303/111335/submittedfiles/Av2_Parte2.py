# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de termos da lista1:'))
lista1=[]
for i in range(0,n,1):
    lista1.append(int(input('Digite um termo:')))

x1= lista1.sort(reverse(lista1))
print(lista1)
print(x1)
