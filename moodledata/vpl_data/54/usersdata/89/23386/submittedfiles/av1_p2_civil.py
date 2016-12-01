# -*- coding: utf-8 -*-
from __future__ import division

def modulo(x):
    if x<0:
        x=x*(-1)
    else:
        x=x*(1)
        
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
    total=modulo(maior(lista)-altura)+modulo(menor(lista)-altura)
    
    return total
    
    
#codigo principal
n=input('digite a quantidade n de pinos da fechadura:')
m=input('digite a altura m que os pinos devem ficar para a fechadura ser desbloqueada:')

listaYoko=[]

for i in range(0,n,1):
    listaYoko.append(input('digite um elemento da lista Yoko:'))
    
print('%.1d'%(altura(listaYoko,m)))