# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
            
    if cont!=0:
        return false
    else:
        return true
            
def descrecente (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
            
    if cont!=0:
        return false
    else:
        return true
        
        
n=input('Digite uma quantidade de termos:')
a=[]
b=[]
c=[]

for i in range(0,n,1):
    a.append(input('Digite um valor de a:'))
for i in range(0,n,1):
    b.append(input('Digite um valor de b:'))
for i in range(0,n,1):
    c.append(input('Digite um valor de c:'))

if crescente(a):
    print ('S')
else:
    print ('N')
if decrescente(a):
    print ('S')
else:
    print ('N')
    


