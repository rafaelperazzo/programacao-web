# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    i=1
    while 1<len(lista):
        if lista[i]<lista[i+1]:
            return(1)
        i=i+1
    return(2)
#escreva as demais funções
def decrescente (lista):
    i=1
    while 1<len(lista):
        if lista[i]>lista[i+1]:
            return(1)
    return(2)
        i=i+1
def consecutivo(lista):
    i=1
    while 1<len(lista):
        if lista[i]==lista[i+1]:
            return(1)
    return(2)
        i=i+1
#escreva o programa principal
n=int(input('digite o tamanho das listas:'))
a=[]
b=[]
c=[]
i=0
while i<n:
    num=int(input('digite o tamanho das listas:'))
    a.append(num)
    i=i+1