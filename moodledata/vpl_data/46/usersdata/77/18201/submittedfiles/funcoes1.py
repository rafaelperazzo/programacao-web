# -*- coding: utf-8 -*-
from __future__ import division

#funçãoCrescente

def crescente (lista):
    contador=0
    for i in range(0,len(lista),1):
         if i==0:
            if lista[0]<lista[1]:
                contador=contador+1
                
         elif i==len(lista)-1:
             if lista[len(lista)-1]>lista[len(lista)-2]:
                 contador=contador+1
                 
         else:
             if lista[i]<lista[i+1] and lista[i]>lista[i-1]:
                contador=contador+1
                 
                 
    if contador==len(lista):
        return True
    else:
        return False

#funçãoDecrescente

def decrescente(lista):
    contador=0
    for i in range(0,len(lista),1):
         if i==0:
            if lista[0]>lista[1]:
                contador=contador+1
                
         elif i==len(lista)-1:
             if lista[len(lista)-1]<lista[len(lista)-2]:
                 contador=contador+1
                
         else:
             if lista[i]>lista[i+1] and lista[i]<lista[i-1]:
                contador=contador+1
                

    if contador==len(lista):
        return True
    else:
        return False
 
 
#funçãoConsecutivos

def consecutivos(lista):
    contador=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]==lista[1]:
                contador=contador+1
                
        elif i==len(lista)-1:
            if lista[len(lista)-1]==lista[len(lista)-2]:
                contador=contador+1
                
        else :
            if lista[i]==lista[i+1]:
                contador=contador+1
                
                
    if contador>0:
        return True
    else:
        return False





n=input('Digite a quantidade de termos em cada uma das listas:')
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('Acrescente Valores a lista A:'))

for i in range(0,n,1):
    b.append(input('Acrescente Valores a lista B:'))
    
for i in range(0,n,1):
    c.append(input('Acrescente Valores a lista C:'))
    
#listaA

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
    
#listaB

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
    
#listaC

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