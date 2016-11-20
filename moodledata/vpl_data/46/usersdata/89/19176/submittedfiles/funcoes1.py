# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    contador=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]<lista[1]:
               contador = contador + 1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                contador=contador+1
        else:
            if lista[i]>lista[i-1] and lista[i]<lista[i+1]:
                contador=contador+1
      
    if contador==(len(lista)-1): 
        return True
    else:
        return False


#escreva as demais funções
def decrescente(lista):
    contador=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[1]:
               contador = contador + 1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]<lista[len(lista)-2]:
                contador=contador+1
                
        else:
            if lista[i]<lista[i-1] and lista[i]>lista[i+1]:
                contador=contador+1
        
    
    if contador==(len(lista)-1): 
        return True
    else:
        return False

def consecutivos(lista):
    contador=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]==lista[1]:
               contador = contador + 1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]==lista[len(lista)-2]:
                contador=contador+1
                
        else:
            if lista[i]==lista[i-1] or lista[i]==lista[i+1]:
                contador=contador+1
    
    if contador!=0:
        return True
    else:
        return False
        
#escreva o programa principal
n=input('digite a quantidade de elementos :')

a=[]
for i in range(0,n,1):
    a.append(input('digite um elemento:'))

b=[]
for i in range(0,n,1):
    b.append(input('digite um elemento:'))

c=[]
for i in range(0,n,1):
    c.append(input('digite um elemento:'))
    
#chamar a funcao para analisar a
if crescente(a):
    print('S')
else:
    print('N')
    
if decrescente(a):
    print('S')
else:
    print('N')

if consecutivos(a):
    print('S')
else:
    print('N')
    
#chamar a funcao para analisar b
if crescente(b):
    print('S')
else:
    print('N')
    
if decrescente(b):
    print('S')
else:
    print('N')

if consecutivos(b):
    print('S')
else:
    print('N')
    
#chamar a funcao para analisar c
if crescente(c):
    print('S')
else:
    print('N')
    
if decrescente(c):
    print('S')
else:
    print('N')

if consecutivos(c):
    print('S')
else:
    print('N')
