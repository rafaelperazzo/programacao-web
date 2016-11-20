# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
        
    if cont==len(lista)-1:
        return True
    else:
        return False


#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    
    if cont==len(lista)-1:
        return True
    else:
        return False
        
def consecutivo (lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
            
    if cont==0:
        return False
    else:
        return True
    


#escreva o programa principal
n=input('Digite a quantidade de elementos na lista: ')
a=[]
b=[]
c=[]

for i in range (0,n,1):
    a.append(input('Digite os valore de a: '))
    
for i in range (0,n,1):
    b.append(input('Digite os valore de b: '))
    
for i in range (0,n,1):
    c.append(input('Digite os valore de c: '))
    

if crescente (a):
    print ('S')
else:
    print ('N')
    
if crescente (b):
    print ('S')
else:
    print ('N')

if crescente (c):
    print ('S')
else:
    print ('N')
    
    
if decrescente (a):
    print ('S')
else:
    print ('N')

if decrescente (b):
    print ('S')
else:
    print ('N')

if decrescente (c):
    print ('S')
else:
    print ('N')


if consecutivo (a):
    print ('S')
else:
    print ('N')

if consecutivo (b):
    print ('S')
else:
    print ('N')
    
if consecutivo (c):
    print ('S')
else:
    print ('N')