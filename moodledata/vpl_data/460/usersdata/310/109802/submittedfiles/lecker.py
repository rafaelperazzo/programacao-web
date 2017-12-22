# -*- coding: utf-8 -*-
def lecker(lista):
    soma = 0
    if lista[0] > lista[1]:
        soma+=1
    if lista[len(lista)-1] > lista[len(lista)-2]:
        soma+=1
    for i in range (n-2):
        if lista[i] < lista[i+1] and lista[i+1] > lista[i+2]:
            soma+=1
    if soma==1:
        print('S')
    else:
        print('N')

n = int(input('Digite a quantidade de elementos: '))
lista1 = []
lista2 = []
for i in range(n):
    lista1.append(int(input('Digite o valor: ')))
for i in range(n):
    lista2.append(int(input('Digite o valor: ')))
lecker(lista1)
lecker(lista2)

