# -*- coding: utf-8 -*-
from __future__ import division

#Funções
def modulo(x):
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
    
def altura(lista,altura):
    soma=modulo(maior(lista)-altura)+modulo(menor(lista)-altura)
    return soma
    
#CódigoPrincipal

n=input('Digite o valor de n:')
m=input('Digite o valor de m:')

a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento de a:'))
    
print('%.d'%(altura(a,m)))
    






