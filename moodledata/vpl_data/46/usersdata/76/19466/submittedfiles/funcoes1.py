# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont = 0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont = cont + 1
            
        if cont!=0:
            return False
        else:
            return True
            
def decrscente (lista):
    cont = 0
    for i in range (0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont = cont + 1
            
        if cont!=0:
            return False
        else:
            return True
            
n = int(input('Digite o valor de n:' ))
a = []
b = []
c = []

for i in range (0,n,1):
    a.append(input('Digite o valor da lista a:' ))
for i in range (0,n,1):
    b.append(input('Digite o valor da lista b:' ))
for i in range (0,n,1):
    c.append(input('Digite o valor da lista c:' ))

if crescente(a):
    print ('S')
else:
    print ('N')

if decrescente(a):
    print ('S')
else:
    print ('N')

if consecutivo(a):
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

if consecutivo(b):
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

if consecutivo(c):
    print ('S')
else:
    print ('N')
    #escreva o código da função crescente aqui


#escreva as demais funções





#escreva o programa principal
