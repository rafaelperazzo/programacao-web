# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    for i in range(0,len(lista),1):
         if a[i]<a[i+1]:
             return True
         else:
             return False
             
def decrescente (lista):
    for i in range(0,len(lista),1):
         if a[i]>a[i+1]:
             return True
         else:
             return False
             
def consecutivos(lista):
    for i in range(0,n,1):
        if a[i]==a[i+1]:
            return True
        else:
            return False

#escreva as demais funções




n=input('Digite a quantidade de termos em cada uma das listas:')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Acrescente Valores a lista:'))

for i in range(0,n,1):
    b.append(input('Acrescente Valores a lista:'))
    
if crescente(lista):
    print('S')
else:
    print('N')
    
    
if decrescente(lista):
    print('S')
else:
    print('N')
    
    
if consecutivos(lista):
    print('S')
else:
    print('N')
#escreva o programa principal
