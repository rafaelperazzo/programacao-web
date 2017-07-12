# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de termos: '))
lista = []
i=1
a=1
while len(lista)<=n:
    lista.append(a)
    i=i+1
    a=a+i
print(lista)
