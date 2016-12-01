# -*- coding: utf-8 -*-
from __future__ import division

def modulo(a):
    if a<0:
        a=a*(-1)
    return a

def maior_elemento(lista):
    maior=lista[0]
    for i in range (0,len(lista),1):
        if lista[i]>maior:
            maior=lista[i]
    return maior

def menor_elemento(lista):
    menor=lista[0]
    for i in range (0,len(lista),1):
        if lista[i]<menor:
            menor=lista[i]
    return menor

def movimentos (lista,altura):
    soma=modulo(maior_elemento(lista)-altura)+modulo(menor_elemento(lista)-altura)
    return soma
    
n=input('Digite a quantidade de elementos da lista:')
altura=input('Digite a altura:')
lista=[]

for i in range (0,n,1):
    lista.append (input('Digite os elementos da lista:'))

mov=movimentos (lista,altura)

print ('%d' %mov)
