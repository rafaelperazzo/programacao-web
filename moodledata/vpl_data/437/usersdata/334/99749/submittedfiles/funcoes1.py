# -*- coding: utf-8 -*-

def crescente (lista):
    if [i]<[i+1]:
        return 'S'

#escreva as demais funções
def decrescente (lista):
    if [i]>[i-1]:
        return 'N'

#escreva o programa principal
n = int(input('Número de elementos: '))
lista1 = []
for i in range (0,n,1):
    lista1.append(int(input('Valores da lista 1: ')))
lista2 = []
for i in range (0,n,1):
    lista2.append(int(input('Valores da lista 2: ')))
lista3 = []
for i in range (0,n,1):
    lista2.append(int(input('Valores da lista 3: ')))

print(crescente(lista1))
print(decrescente(lista1))

print(crescente(lista2))
print(decrescente(lista2))

print(crescente(lista3))
print(decrescente(lista3))