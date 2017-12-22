# -*- coding: utf-8 -*-
def soma(lista, resto):
    soma = 0
    for i in lista:
        if i%2==resto:
            soma+= i
    return soma

def quant(lista, resto):
    soma = 0
    for i in lista:
        if i%2==resto:
            soma+= 1
    return soma

qnt = int(input(''))
lista = []
for j in range(qnt):
    lista.append(int(input('')))
print(soma(lista,1))
print(soma(lista, 0))
print(quant(lista, 1))
print(quant(lista, 0))
print(lista)

