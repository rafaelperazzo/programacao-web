# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[0]<lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]>lista[i-1] and lista[i]<lista[i+1]:
                cont=cont+1
    if cont==(len(lista)):
        return True
    else:
        return False
        

def decrescente(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]>lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]<lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]<lista[i-1] and lista[i]>lista[i+1]:
                cont=cont+1
                
    if cont==(len(lista)):
        return True
    else:
        return False
        
def consecutivo(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]==lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]==lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]==lista[i+1]:
                cont=cont+1
    if cont>0:
        return True
    else:
        return False
    
n=input('digite o valor de n:')
a=[]
b=[]
c=[]
            
for i in range(0,n,1):
    a.append(input('digite os elementos de a:'))
for i in range(0,n,1):
    b.append(input('digite os elementos de b:'))
for i in range(0,n,1):
    c.append(input('digite os elementos de c:'))
    
if crescente(a):
    print ('S')
else:
    print ('N')
    
if crescente(b):
    print ('S')
else:
    print ('N')

if crescente(c):
    print ('S')
else:
    print ('N')
    
    
    
if decrescente(a):
    print ('S')
else:
    print ('N')
    
if decrescente(b):
    print ('S')
else:
    print ('N')
    
if decrescente(c):
    print ('S')
else:
    print ('N')
    
if consecutivo(a):
    print ('S')
else:
    print ('N')
    
if consecutivo(b):
    print ('S')
else:
    print ('N')
    
if consecutivo(c):
    print ('S')
else:
    print ('N')