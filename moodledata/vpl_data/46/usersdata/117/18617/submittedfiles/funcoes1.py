# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]>lista[i-1] and lista[i]<lista[i+1]:
                cont=cont+1
    if cont==(len(lista)):
        return True
    else:
        return False

#escreva as demais funções        
def decrescente(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]>lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]<lista[len(lista)-2]:
                    cont=cont+1
        else:
            if lista[i]<lista[i-1] and lista[i]>lista[i+1]:
                    cont=cont+1 
                
    if cont==(len(lista)):
        return True
    else:
        return False
            

def consecutivo(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]==lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]==lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]==lista[i+1]:
                cont=cont+1
    if cont>0:
        return True
    else:
        return False 







#escreva o programa principal
