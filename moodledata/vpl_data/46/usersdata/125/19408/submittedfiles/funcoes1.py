# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
            
    if cont!=0:
        return False
    else:
        return True
            
def decrescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
            
    if cont!=0:
        return False
    else:
        return True
        
def consecutivos (lista):
    cont=0
    for i in range(0,(lista),1):
        if i==0:
            if lista[0]==lista[1]:
                con=cont+1
        elif i==0(len(lista)-1):
            if lista[len(lista)-1]==lista[len(lista)-2]:
                cont=cont+1
    if cont>0:
        return False
    else:
        return True
            
        
n=int(input('Digite uma quantidade de termos:'))
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('Digite um valor de a:'))
for i in range(0,n,1):
    b.append(input('Digite um valor de b:'))
for i in range(0,n,1):
    c.append(input('Digite um valor de c:'))

if crescente(a):
    print ('S')
else:
    print ('N')
if decrescente(a):
    print ('S')
else:
    print ('N')
if consecutivos(a):
    print ('S')
else:
    print ('N')
    
if crescente(b):
    print ('S')
else:
    print ('N')
if decrescente(b):
    print ('S')
else:
    print ('N')
if consecutivos(b):
    print ('S')
else:
    print ('N')

if crescente(c):
    print ('S')
else:
    print ('N')
if decrescente(c):
    print ('S')
else:
    print ('N')
if consecutivos(c):
    print ('S')
else:
    print ('N')
    
    
