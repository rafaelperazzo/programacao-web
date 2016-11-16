# -*- coding: utf-8 -*-
from __future__ import division

def termosIguais(a,b):
    
    cont=0
        
    for i in range (0,len(a),1):
        if a[i] in b:
            cont=cont+1
    
    return cont
    
a=[]
b=[]

n=input('Número de termos de A: ')
m=input('Número de termos de B: ')

for i in range (0,n,1):
    a.append(input('Digite um termo de A: '))

for i in range (0,m,1):
    b.append(input('Digite um termo de B: '))
    
print termosIguais(a,b)