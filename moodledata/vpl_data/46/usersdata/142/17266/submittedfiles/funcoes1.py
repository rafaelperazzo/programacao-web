# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range (0,(len(lista)-2),1):
        if lista[i]<lista[i+1]:
            cont=cont
        else:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False        
    #escreva o código da função crescente aqui


#escreva as demais funções

def decrescente(lista):
    cont=0
    for i in range(0,(len(lista)-2),1):
        cont=0
        for i in range(0,(len(lista)-2),1):
            if lista[i]>lista[i+1]:
                cont=cont
            else:
                cont=cont+1
        if cont==0:
            return True
        else:
            return False

def consecutivos(lista):
    cont=0
    for i in range (0,(len(lista)-2),1):
        if lista[i]==lista[i+1]:
            cont=cont+1
        else:
            cont=cont
    if cont!=0:
        return True
    else:
        return False

#escreva o programa principal
n=input('Digite um valor n:')
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('Digite um valor a:'))


if crescente(a):
    print 'S'
else:
    print 'N'

if decrescente(a):
    print 'S'
else:
    print 'N'

if consecutivos(a):
    print 'S'
else:
    print 'N'