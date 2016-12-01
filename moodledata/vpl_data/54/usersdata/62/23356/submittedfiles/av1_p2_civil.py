# -*- coding: utf-8 -*-
from __future__ import division

def modulo(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
def maiornumero(lista):
    ma=lista[0]
    for i in range (0,len(lista),1):
        if lista[i]>ma:
            ma=lista[i]
    return ma
    
def menornumero(lista):
    me=lista[0]
    for i in range (0,len(lista),1):
        if lista[i]<me:
            me=lista[i]
    return me
    
def altura(lista):
    soma=modulo(maiornumero(lista)-m)+modulo(menosnumero(lista)-m)
    return soma
    
n=input('Digite o valor de n: ')
m=input('Digite a altura: ')

lista=[]
for i in range (0,n,1):
    lista.append(input('Digite um elemento: '))

movimentos=altura(lista)
print ('%.d'%movimentos)