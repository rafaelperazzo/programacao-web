# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    contd=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            contd=contd+1
    if (contd)==len(lista)-1:
        return true
    else:
        return false
def decrescente (lista):
    #código da função decrescente
    contc=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            contc=contc+1
    if contc==len(lista)-1:
        return true
    else:
        return false
def consecutivos (lista):
    #código da função de elementos consecutivos
    cont = 0
    for i in range(len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return true
    else:
        return false
        
#escreva as demais funções





#escreva o programa principal
