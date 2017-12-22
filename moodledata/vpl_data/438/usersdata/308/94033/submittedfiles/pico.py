# -*- coding: utf-8 -*-

def pico(lista):
    contagem = 0
    for i in range (0, len(lista)-2):
        if lista[i]<lista[i+1]:
            contagem += 1
            print('1: %d' % contagem)
    for i in range (contagem, len(lista)-2):
        if lista[i]<lista[i+1]:
            contagem += 1
            print('2: %d' % contagem)
    if contagem == len(lista)-1:
        return 'S'
    else:
        return 'N'
    

n = input('Digite a quantidade de elementos da lista: ')
lista = [1, 2, 3, 2, 1]
print(pico(lista))
lista = [2, 2, 3, 2, 1]
print(pico(lista))
lista = [1, 2, 3, 2, 2]
print(pico(lista))