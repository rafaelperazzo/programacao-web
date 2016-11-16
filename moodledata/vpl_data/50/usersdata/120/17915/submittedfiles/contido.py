# -*- coding: utf-8 -*-
from __future__ import division
def contido(a,b):
    cont=0
    for i in range(0,len(a),1):
        if b[i] in a:
            cont+=1
    return cont
#entrada
a=[]
n=input('digite a quantidade de termos de a:')
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
b=[]
n=input('digite a quantidade de termos de b:')
for i in range(0,n,1):
    b.append(input('digite um elemento:'))
#saida
print contido(a,b)
    

    
