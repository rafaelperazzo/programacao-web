# -*- coding: utf-8 -*-
def crescente(lista):
    soma = 0
    for i in range ( len(lista) ):
        if lista[i] > lista[i+1]:
            soma+=1
    if soma!= 0:
        print('N')
    else:
        print('S')
        
def decrescente(lista):
    soma = 0
    for i in range ( len(lista) ):
        if lista[i] < lista[i+1]:
            soma+=1
    if soma!= 0:
        print('N')
    else:
        print('S')







n = int(input('Digite a quantidade de elementos: '))
lista1 = []
lista2 = []
lista3 = []

for i in range(n):
    lista1.append(int(input('Digite valor: ')))
for i in range(n):
    lista2.append(int(input('Digite valor: ')))
for i in range(n):
    lista3.append(int(input('Digite valor: ')))









