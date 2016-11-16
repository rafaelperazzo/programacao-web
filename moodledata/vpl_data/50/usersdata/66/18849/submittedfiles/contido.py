# -*- coding: utf-8 -*-
from __future__ import division

def contido (a,b):
    cont=0
    for i in range (0,len(b),1):
        if b[i]in a:
            cont=cont +1
            
    return cont
        
        
n=input('digite a quantidade  de termos da lista:')
m=input('digite a quantidade de termos da lista:')

a= []
b= []
for i in range (0,n,1):
    a.append(input('digite os valores da lista a:'))


for i in range (0,m,1):
    b.append(input('digite os valores da lista b:'))

        
        

print contido(a,b)