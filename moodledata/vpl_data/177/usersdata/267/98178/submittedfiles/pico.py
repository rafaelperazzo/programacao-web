# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    maior=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            maior=i+1
    for i in range(0,maior,1):
        if lista[i]>lista[i+1]:
            return('N')
    for i in range(maior,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            return('N')
    return('S')

n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
