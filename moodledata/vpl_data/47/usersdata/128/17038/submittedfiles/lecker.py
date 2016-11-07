# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    for i in range (0,len(lista),1):
        if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
            cont=cont+1
        if cont=1:
            return True
        else:
            return False

a=[]
b=[]
n=input('Digite a quantidade de termos: ')

for i in range (0,n,1):
    a.append(input('Digite um termo de A: ')
    
for i in range (0,n,1):
    b.append(input('Digite um termo de B: ')

if lecker(a):
    print ('S')
else:
    print ('N')