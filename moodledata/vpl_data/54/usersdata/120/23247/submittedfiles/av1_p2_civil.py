# -*- coding: utf-8 -*-
from __future__ import division
def absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
def maior(lista):
    maior=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]>maior:
            maior=lista[i]
    return maior        
         
def menor(lista):
    menor=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]<menor:
            menor=lista[i]
    
    return menor   
    
def altura(lista,m):
    soma=(absoluto(maior(lista)-m))+(absoluto(menor(lista)-m))
    return soma
    
#entrada    
n=int(input('digite o tamanho da lista:'))
m=input('digite o valor da altura:')
lista=[]
for i in range(0,n,1):
    lista.append(input('digite o elemento da lista:'))

#saida
print ('%.d'%(altura(lista,m)))