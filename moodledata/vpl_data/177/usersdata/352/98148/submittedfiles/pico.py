# -*- coding: utf-8 -*-

def pico(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i+1]>lista[i]:
            return (i)

def decrescente (lista_2):
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            return (True)
        else:
            return (False)
lista_2=lista[pico:]

n = int(input('Digite a quantidade de elementos da lista: '))
lista=[ ]

for i in range(0,n,1):
    valor=int(input('Digite os valores da lista: '))
    lista.append(valor)
    
if decrescente(lista[pico: ]):
    print('S')
else:
    print('N')