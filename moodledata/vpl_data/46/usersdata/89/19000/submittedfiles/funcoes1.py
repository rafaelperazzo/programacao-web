# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
   contador=0
   for i in range(0,len(lista),1):
       #if lista[i]<lista[i+1]:
            #cont = cont + 1
    
    if contador==len(lista)-1: #len(lista)-1
        return True
    else:
        return False


#escreva as demais funções
def decrescente(lista):
    contador=0
    for i in range(0,len(lista),1):
        #parecido com a função anterior! so muda o sinal!
    
    if contador==len(lista)-1: #len(lista)-1
        return True
    else:
        return False

def consecutivosiguais(lista):
    contador=0
    for i in range(0,len(lista),1):
        #Qual a condição para um elemento ser consecutivo a outro ?
    
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
    
#chamar a funcao crescente
if crescente(a):
    print('S')
else:
    print('N')
    
if crescente(b):
    print('S')
else:
    print('N')

if crescente(c):
    print('S')
else:
    print('N')
    
#chamar a funcao decrescente
if decrescente(a):
    print('S')
else:
    print('N')
    
if decrescente(b):
    print('S')
else:
    print('N')

if decrescente(c):
    print('S')
else:
    print('N')
    
#chamar a funcao consecutivosiguais
if consecutivosiguais(a):
    print('S')
else:
    print('N')
    
if consecutivosiguais(b):
    print('S')
else:
    print('N')

if consecutivosiguais(c):
    print('S')
else:
    print('N')
