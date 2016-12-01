# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de pinos da fechadura:')
m=input('Digite a altura para desbloqueio dos pinos:')

a=[]

for i in range (0,n,1):
    a.append(input('Digite a altura de cada pino:'))
    
print altura(lista,m):
    
def valorAbs(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
def maior(lista):
    maior=a[0]
    for i in range (0,len(lista),1):
        if lista[i]>maior:
            maior=lista[i]
            
    return maior
    
def menor(lista):
    menor=lista[0]
    for i in range (0,len(lista),1):
        if lista[i]<menor:
            menor=lista[i]
            
    return menor
    
def altura(lista,altura):
    soma=valorAbs(maior(lista)-altura)+valorAbs(menor(lista)-altura)
    
    return soma
        
        