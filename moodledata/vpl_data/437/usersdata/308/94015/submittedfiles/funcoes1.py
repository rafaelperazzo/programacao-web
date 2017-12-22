# -*- coding: utf-8 -*-

def crescente (lista):
    crescente = 0
    decrescente = 0
    iguais = False
    for i in range(0, len(lista)):
        try:
            if lista[i]>lista[i-1]:
                crescente += 1
            if lista[i]<lista[i-1]:
                decrescente += 1
            if lista[i]== lista[i-1]
                iguais = True
    if crescente == len(lista):
        print('S')
    else:
        print('N')
    if decrescente == len(lista):
        print('S')
    else:
        print('N')
    if iguais:
        print('S')
    else:
        print('N')
#escreva as demais funções





#escreva o programa principal
