# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>=lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
        
def decrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<=lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False

def igual(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont>0:
        return true
    else:
        return false
    
    
    
    
    
    
a=[] 
n=input('Digite o valor de n:')
for i in range(0,n,1):
    a.append(input('Digite um elemnteo de a:'))
if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if igual(a):
    print('S')
else:
    print('N')


#escreva o programa principal
