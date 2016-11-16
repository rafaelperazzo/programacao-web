# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    contador=0
    for i in range(0,len(lista),1):
         if a[i]<a[i+1]:
             contador=contador+1
             break
    if contador!=0:
        return True
    else:
        return False

def decrescente (lista):
    contador=0
    for i in range(0,len(lista),1):
         if a[i]>a[i+1]:
            contador=contador+1
            break
    if contador!=0:
        return True
    else:
        return False
        
def consecutivos(lista):
    contador=0
    for i in range(0,len(lista),1):
        if a[i]==a[i+1]:
            contador=contador+1
            break
    if contador!=0:
        return True
    else:
        return False

#escreva as demais funções




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