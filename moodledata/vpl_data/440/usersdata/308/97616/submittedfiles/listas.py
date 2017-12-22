# -*- coding: utf-8 -*-
lista = []
maximo = 0
tamanho = int(input('Insira a quantidade de valores: ')
for i in range (0, tamanho):
    lista.append(int(input('Insira o valor %d: ' % i+1)
for i in range (1, len(lista)):
    altura = abs(lista[i-1]-lista[i])
    if altura > maximo:
        maximo = altura
print(maximo)