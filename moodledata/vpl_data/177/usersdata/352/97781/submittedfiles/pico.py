# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    var=lista[0]
    for i in range(0,len(lista)-2,1):
        if lista[i]<lista[i+1]:
            var=i+1


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...

lista=[ ]

for i in range(0,n,1):
    valor=float(input('Digite os valores da lista: '))
    lista.append(valor)
