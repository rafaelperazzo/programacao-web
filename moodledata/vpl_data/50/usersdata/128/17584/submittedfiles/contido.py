# -*- coding: utf-8 -*-
from __future__ import division

def termosIguais(a,b):
    
    cont=0
        
    for i in range (0,len(a),1):
        for j in range (0,len(b),1):
            if a[i]==b[j]:
                cont=cont+1
    
    return cont
    
a=[]
b=[]

nA=input('Número de termos de A: ')
nB=input('Número de termos de B: ')

for i in range (0,nA,1):
    a.append(input('Digite um termo de A: '))

for i in range (0,nB,1):
    b.append(input('Digite um termo de B: '))
    
print termosIguais(a,b)