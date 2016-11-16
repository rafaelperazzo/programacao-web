# -*- coding: utf-8 -*-
from __future__ import division
#COMECE AQUI ABAIXO
def listas(a,b,c):
    for i in range (0, len(lista),1):
        if listas(i)-(listas(i)-1)>0:
            print 'Crescente'
            return True
        elif listas(i)-(listas(i)-1)<0:
            return False 
            print 'Decrescente'
        elif listas(i)-(listas(i)-1)==0:
            print 'Elementos iguais'
        
n = input ('Digite o tamanha da lista')
a = []
b = [] 
c = []
for i in range (0,n,1):
    a.append (input('Digite os elementos de A:'))
for i in range (0,n,1):
    b.append (input('Digite os elementos de B:'))
for i in range (0,n,1):
    c.append (input('Digite os elementos de C:'))
    