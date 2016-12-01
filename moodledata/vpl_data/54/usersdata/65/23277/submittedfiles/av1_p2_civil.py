# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:26:58 2016

@author: Jonathan Moreira
"""

from __future__ import division

#FUNÇÕES
def absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x

def maior(l):
    maior=l[0]
    for i in range(0,len(l),1):
        if l[i]>maior:
            maior=l[i]
    return maior

def menor(l):
    menor=l[0]
    for i in range(0,len(l),1):
        if l[i]<menor:
            menor=l[i]
    return menor

def altura(l,altura):
    soma=absoluto(maior(l)-altura)+absoluto(menor(l)-altura)
    return soma

#PRINCIPAL
n=input('Digite n: ')
m=input('Digite a altura:')

lista=[]
for i in range(0,n,1):
    lista.append(input('Digite um elemento da lista: '))

print ((altura(lista,m)))