# -*- coding: utf-8 -*-
def lista_comuns (lista1, lista2)
    lista_comuns=[i for i in lista1 if i in lista2]
    return lista_comuns
    
n=int(input('Digite o número de elementos da lista 1: '))
m=int(input('Digite o número de elementos da lista 2: '))

a=[]
for i in range (0, n, 1):
    a.append(int(input('Digite um elemento para a lista 1: ')))

b=[]
for i in range (0, m, 1):
    b.append(int(input('Digite um elemento para a lista 2: ')))
    
lista3=lista_comuns (a, b)
print(len(lista3))