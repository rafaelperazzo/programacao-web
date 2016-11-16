# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range (1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont>0:
        return False 
    else:  
        return True 


def decrescente(lista2):
    cont=0
    for i in range (1,len(lista2),1):
        if lista2[i]>lista2[i-1]:
            cont=cont+1
    if cont>0:
        return False 
    else:
        return True 

def iguais(lista3):
    cont=0
    for i in range (0,len(lista3),1):
        if lista3[i]==lista3[i+1]:
            cont=cont+1
    if cont==0:
        return False 
    else: 
        return True 
        
    
n=input('insira o valor de n:') 
a=[]
b=[]
c=[]

for i in range (0,n,1):
    a.append(input('insira um valor para lista 1:'))
    
for i in range (0,n,1):
    b.append(input('insira um valor para lista 2:')) 
    
for i in range (0,n,1):
    c.append(input('insira um valor para lista 3:'))


if crescente(a):
    print ('S') 
else:
    print ('N') 

if decrescente(a):
    print('S')
else:
    print('N')
    
if iguais(a):
    print('S')
else:
    print('N')
    

if crescente(b):
    print ('S') 
else:
    print ('N') 
    
if decrescente(b):
    print('S')
else:
    print('N')
    
if iguais(b):
    print('S')
else:
    print('N')
    
    
if crescente(c):
    print ('S') 
else:
    print ('N') 
    
if decrescente(c):
    print('S')
else:
    print('N')
    
if iguais(c):
    print('S')
else:
    print('N')