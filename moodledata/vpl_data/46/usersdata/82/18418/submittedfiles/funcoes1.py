# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]<lista[i+1]:
                cont=cont+1
                
        elif i==(len(lista)-1):
            if lista[len(lista)-1]:
                if lista[len(lista)]>lista[len(lista)-1]:
                    cont=cont+1
        else:
            if lista[i]==lista[i+1]:
                cont=cont+1

    if cont==0:
        return True
    else:
        return False

n = input('Digite o valor de n:')

a=[]
b=[]
c=[]

for i in range (0,n,1):
    a.append (input('Digite o valor de a:'))
for i in range (0,n,1):
    b.append (input('Digite o valor de b:'))
for i in range (0,n,1):
    c.append (input('Digite o valor de c:'))

if crescente(a):
    print ('S')
else:
    print ('N')
    
if decrecente(a):
    print ('S')
else:
    print('N')
    
if igual(a):
    print ('S')
else:
    print('N')
    
if crescente(b):
    print ('S')
else:
    print ('N')
    
if decrecente(b):
    print ('S')
else:
    print('N')
    
if igual(b):
    print ('S')
else:
    print('N')
    
if crescente(c):
    print ('S')
else:
    print ('N')
    
if decrecente(c):
    print ('S')
else:
    print('N')
    
if igual(c):
    print ('S')
else:
    print('N')






