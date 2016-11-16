# -*- coding: utf-8 -*-
from __future__ import division
def contido(a,b):
    cont=0
    for i in range(0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return cont

na=input('digite a quantidade de termos de a:')
nb=input('digite a quantidade de termos de b:')
a=[]
b=[]
for i in range(0,na,1):
    a.append(input('digite um elemento de a:'))

for i in range(0,nb,1):
    b.append(input('digite um elemento de b:'))

print contido(a,b)
    

    
