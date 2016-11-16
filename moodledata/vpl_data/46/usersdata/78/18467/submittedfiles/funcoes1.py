# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
    cont=0
    for i in raange(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
def descrescente (lista):
    cont2=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont2=cont2+1
    cont3=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont3=cont3+1:
if cont==0:
    return True
else:
    return False
if cont2==0:
    return True
else:
    return False
if cont3==0:
    return True
else:
    return False
    
    
a=[]
b=[]
c=[]
n=input('digite a quantidade de elementos:')

for i in range(0,n,1):
    a.append(input('digite o valor do elemento')):
        
if crescente(a)==True and:
    print('S')
else:
    print('N')
fi decrescente(b)==True