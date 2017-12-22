# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    anterior = lista[0]
    atual = lista[1]
    if atual>anterior:
        pico = True
        subida = True
    else:
        pico = False
        
    anterior = atual
    i = 2
    while i<n:
        atual = lista[i]
        if anterior < atual:
            if not subida:
                pico = False
        else:
            subida = False
        anterior = atual
        i+=1
    if subida:
        pico = False
    if pico:
        print('S')
    else:
        print('N')
        
        
        
        
        
        
        
"""    
    for i in range (0,n-2,2):
        while lista[i+1]>lista[i] and lista[i+1]<lista[i+2):
            b = lista[i+1]
            j = i+2
        
            b
        
"""

n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
lista = []

for i in range(0,n,1):
    lista.append(int(input('digite valor: ')))

pico(lista)

