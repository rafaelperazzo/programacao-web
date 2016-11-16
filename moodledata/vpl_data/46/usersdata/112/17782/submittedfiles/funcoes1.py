# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de números das listas:')
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append(input('Digite um valor da lista A:'))


def crescente(lista):
    p=0
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
            if lista[i]!=lista[i+1]:
            p=p+1
                if cont>0:
                    return True
                else:
                    return False
def decrescente(lista):
    d=0
    cont2=0
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont2=cont2+1
            if lista[i]!=lista[i+1]:
            d=d+1
                if cont2>0:
                    return True
                else: 
                    return False
def elementosiguais(lista):
    cont3=0
    for i in range (0,len(lista)-1,1):
        if lista[i]==lista[i+1] or lista[i]==lista[i-1]:
             cont3=cont3+1
             if cont3>0:
                 return True
            else:
                return False
            
if crescente(a):
    print 'S'
else:
    print 'N'

if decrescente(a):
    print 'S'
else:
    print 'N'
    
if elementosiguais(a):
    print 'S'
else:
    print 'N'