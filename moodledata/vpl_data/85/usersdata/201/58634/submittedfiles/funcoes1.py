# -*- coding: utf-8 -*-

def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def consecutivos (lista):
    for i in range(0, len(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
        if cont==0:
            return(False,cont)
        else:
            return(False,cont)

n=int(input('Digite o número de termos:'))
lista1=[]
lista2=[]
lista3=[]























