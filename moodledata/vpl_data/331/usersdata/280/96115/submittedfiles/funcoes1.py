# -*- coding: utf-8 -*-

def crescente (lista,n):
    cont = 0
    for i in range (0,n-1,1):
        if lista[i] < lista[i+1]:
            cont = cont + 1
    if cont == n-1:
        return(print("S"))
    else:
        return(print("N"))

def decrescente (lista,n):
    cont = 0
    for i in range (0,n-1,1):
        if lista[i] > lista[i+1]:
            cont = cont + 1
    if cont == n-1:
        return(print("S"))
    else:
        return(print("N"))

def iguais (lista,n):
    cont = 0
    for i in range (0,n-1,1):
        if lista[i] == lista[i+1]:
            cont = cont + 1
    if cont != 0:
        return(print("S"))
    else:
        return(print("N"))


#escreva as demais funções





#escreva o programa principal
