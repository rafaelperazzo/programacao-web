# -*- coding: utf-8 -*-
from __future__ import division

def contido(a,b):
    cont=0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont=cont+1
    return cont
a=[]
b=[]
x=input('entre com o tamanho a: ')
y=input('entre com o tamanho b: ')

for i in range (0,x,1):
    a.append(input('entre com os valores de a: '))
for i in range (0,y,1):
    b.append(input('entre com os valores de b: '))
    
print contido(a,b)