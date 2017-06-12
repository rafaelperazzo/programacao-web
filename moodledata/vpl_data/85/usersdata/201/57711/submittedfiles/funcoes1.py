# -*- coding: utf-8 -*-
n=int(input('Digite o número de termos:'))
lista1=[]
lista2=[]
lista=[]
def crescente (lista):
    #escreva o código da função crescente aqui
    
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

#escreva as demais funções

def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def quantidade (lista,x):
    cont=0
    for i in range(0,lrn(lista),1):
        if lista[i]==x:
            cont=cont+1
    return (cont)

#escreva o programa principal

