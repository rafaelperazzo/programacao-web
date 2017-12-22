# -*- coding: utf-8 -*-

n = int(input('Digite a quantidade de elementos: '))
lista = []
for i in range(n):
    lista.append(int(input('Digite o valor: ')))
lista_impar = []
lista_par = []
for i in range (n):
    if lista[i]%2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])
print(sum(lista_impar))
print(sum(lista_par))
print(len(lista_impar))
print(len(lista_par))
print(lista)
