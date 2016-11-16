# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
            
    if cont!=0:
        return False
    else:
        return True
        
def descrescente (lista):
    cot=0
    if i in range (0, len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
            
     
    if cont!=0
        return False
    else:
        return True
        
a=[]
b=[]
c=[]

n = input('Digite o valor de n:')
for i in range (0,n,1):
    a.append (input('Digite o valor de a:'))
for i in range (0,n,1):
    b.append (input('Digite o valor de b:'))
for i in range (0,n,1):
    c.append (input('Digite o valor de c:'))

if crescente(a):
    print ('S')
else:
    print ('N')
    
if decrescente(a):
    print ('S')
else:
    print('N')
    
if igual(a):
    print ('S')
else:
    print('N')
    
if crescente(b):
    print ('S')
else:
    print ('N')
    
if decrescente(b):
    print ('S')
else:
    print('N')
    
if igual(b):
    print ('S')
else:
    print('N')
    
if crescente(c):
    print ('S')
else:
    print ('N')
    
if decrescente(c):
    print ('S')
else:
    print('N')
    
if igual(c):
    print ('S')
else:
    print('N')






