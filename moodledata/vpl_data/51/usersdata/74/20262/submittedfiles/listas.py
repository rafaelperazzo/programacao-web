# -*- coding: utf-8 -*-
from __future__ import division

def maiord(lista):
    i = 0
    maior = lista[i+1]-lista[i]
    
    while (len(lista)-1)>i:
        const = lista[i+1]-lista[i]
        if const>maior:
            maior = const
        i = i+1
    
    return maior

n = input('Digite o tamanho do vetor: ')

x = 1
a=[]

while n>=x:
    a.append(input('Digite os valores do vetor: '))
    x = x+1

maiord(a)