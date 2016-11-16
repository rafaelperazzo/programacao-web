# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    contador = 0
    for i in range (0,len(lista)-1,1):
        if lista[i]>= lista[i+1]:
            contador = contador +1
            break
    if contador==0:
        return True
    else:
        return False

def descrescente(lista):
    contador = 0
    for i in range (0,len(lista)-1,1):
        if lista[i]<= lista[i+1]:
            contador = contador +1
            break
    if contador==0:
        return True
    else:
        return False

def iguais(lista):
    contador = 0
    for i in range (0,len(lista)-1,1):
        if lista[i] == lista[i+1]:
            contador = contador +1
            break
    if contador!=0:
        return True
    else:
        return False

n = input ('Digite a quantidade de termos:')
a =[]
b =[]
c =[]
for i in range (0,n,1):
    a.append (input ('Digite um valor para a lista a:'))
    b.append (input ('Digite um valor para a lista b:'))
    c.append (input ('Digite um valor para a lista c:'))

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

if iguais(a):
    print ('S')
else:
    print ('N')

if iguais(b):
    print ('S')
else:
    print ('N')
    
if iguais(c):
    print ('S')
else:
    print ('N')