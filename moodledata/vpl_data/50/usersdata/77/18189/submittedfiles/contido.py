# -*- coding: utf-8 -*-
from __future__ import division

def contidos(a,b):
    contador=0
    for i in range(0,len(a),1):
        if a[i] in b:
            contador=contador+1
            
    return contador
    
nA=input('Digite a quantidade de elementos da lista de A:')
nB=input('Digite a quantidade de elementos da lista de B:')

a=[]
b=[]

for i in range(0,nA,1):
    a.append(input('Acrescente valores a lista A:'))
    
for i in range(0,nB,1):
    b.append(input('Acrescente valores a lista B:'))
    
print contidos(a,b)
