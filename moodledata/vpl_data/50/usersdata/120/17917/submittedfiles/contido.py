# -*- coding: utf-8 -*-
from __future__ import division
def contido(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return cont
#entrada
n=input('digite a quantidade de termos de a:')
n=input('digite a quantidade de termos de b:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('digite um elemento:'))

for i in range(0,n,1):
    b.append(input('digite um elemento:'))
#saida
print contido(a,b)
    

    
