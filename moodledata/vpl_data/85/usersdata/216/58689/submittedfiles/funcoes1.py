# -*- coding: utf-8 -*-

def crescente (lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            return True
    return False

#escreva as demais funções
def decrescente(lista):
    for i in range(0,(lista)-1,1):
        if lista[i]>lista[i+1]:
            return True
    return False
    
def numiguais(lista):
    for i in range(0,(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
    return False




#escreva o programa principal
