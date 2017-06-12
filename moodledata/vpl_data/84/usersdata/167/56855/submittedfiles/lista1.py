# -*- coding: utf-8 -*-
def somaimpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==1:
            soma=soma+lista[i]
    return soma
def somapar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+lista[i]
    return soma
def qtimpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==1:
            soma=soma+1
    return soma
def qtpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+1
    return soma
A=[]
n=int(input('tamanho da lista:'))
for i in 



