# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range (0,len(lista),1):
        if lista[i]<lista[i+1]:
            cont=cont+1
        else:
            cont=cont+1
    if cont==1:   
        return True
    else:
        return False
            
    
def decrescente (lista):
    cont=0
    for i in range (0,len(lista),1):
        if lista[i]>lista[i+1]:
            cont=cont+1
        else:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
        
def consecutivos (lista):
    for i in range (0,len(lista),1):
        if lista[i]==lista[i+1]:
            cont=cont+1
        else:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False

n=input('Digite a quantidade de elementos da lista:')
R=[]
S=[]
T=[]

for i in range(0,n,1):
    R.append(input('Digite um elemento da lista R:'))
    
for i in range(0,n,1):
    S.append(input('Digite um elemento da lista S:'))
    
for i in range(0,n,1):
    T.append(input('Digite um elemento da lista T:'))




if crescente(R):
    print('S')
else:
    print('N')
    
if decrescente(R):
    print('S')
else:
    print('N')
    
if consecutivos(R):
    print('S')
else:
    print('N')
    
if crescente(S):
    print('S')
else:
    print('N')
    
if decrescente(S):
    print('S')
else:
    print('N')
    
if consecutivos(S):
    print('S')
else:
    print('N')
    
if crescente(T):
    print('S')
else:
    print('N')
    
if decrescente(T):
    print('S')
else:
    print('N')
    
if consecutivos(T):
    print('S')
else:
    print('N')
    
    
    
