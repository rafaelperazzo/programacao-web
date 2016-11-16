# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    
    else:
        return False
        
def decrescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
   
    if cont==0:
        return True
    
    else:
        return False
        
def iguais(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
   
    if cont!=0:
        return True
    
    else:
        return False
        
n=input('digite a quantidade de elementos:')
X=[]
Y=[]
Z=[]

for i in range (0,n,1):
    X.append(input('digite o elemendo da lista X:'))
    
for i in range (0,n,1):
    Y.append(input('digite o elemendo da lista Y:'))
    
for i in range (0,n,1):
    Z.append(input('digite o elemendo da lista Z:'))
    
if crescente(X):
    print('S')
    
else:
    print('N')
    
if decrescente(X):
    print('S')
    
else:
    print('N')
    
if iguais(X):
    print('S')
    
else:
    print('N')

if crescente(Y):
    print('S')
    
else:
    print('N')
    
if decrescente(Y):
    print('S')
    
else:
    print('N')
    
if iguais(Y):
    print('S')
    
else:
    print('N')
    
if crescente(Z):
    print('S')
    
else:
    print('N')
    
if decrescente(Z):
    print('S')
    
else:
    print('N')
    
if iguais(Z):
    print('S')
    
else:
    print('N')
    
        
