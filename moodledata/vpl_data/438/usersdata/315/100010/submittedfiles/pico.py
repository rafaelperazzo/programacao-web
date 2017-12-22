# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    anterior = lista[0]
    atual = lista[1]
    if atual>anterior:
        pico = True
        crescente = True
    else:
        pico = False
        
    anterior = atual
    i = 2
    while i<n:
        atual = lista[i]
        if anterior < atual:
            if not crescente:
                pico = False
        else:
            crescente = False
        anterior = atual
        i+=1
    if crescente:
        pico = False
    if pico:
        print('S')
    else:
        print('N')
        
        

n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
lista = []

for i in range(0,n,1):
    lista.append(int(input('digite valor: ')))

pico(lista)

