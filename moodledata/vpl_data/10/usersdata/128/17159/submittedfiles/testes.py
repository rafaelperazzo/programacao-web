# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

def soma(l1,l2):
    vaium=0
    l3=[]
    i=len(l2)-1
    while i>=0:
        numero=l1[i]=l2[i]+vaium
        if numero>9:
            numero=numero-10
            vaium=1
        else:
            vaium=0
        l3.insert(0,numero)
        i=i+1
    if vaium==1:
        l3.insert(0,1)
    return l3

n=input('N: ')
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite um termo: '))
    
for i in range (0,n,1):
    b.append(input('Digite um termo: '))

c=soma(a,b)
print c