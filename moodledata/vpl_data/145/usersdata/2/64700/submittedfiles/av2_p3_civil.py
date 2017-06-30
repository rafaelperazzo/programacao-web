# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de termos: '))
lista = []

j = 1
soma = 0
for i in range(0,n,1):
    soma = soma + j
    lista.append(soma)
    j = j + 1

print(lista)
