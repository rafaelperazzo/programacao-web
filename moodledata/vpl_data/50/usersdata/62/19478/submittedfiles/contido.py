# -*- coding: utf-8 -*-
from __future__ import division

def contido(x,y):
    cont=0
    for i in range (0,len(y),1):
        if y[i] in x:
            cont=cont+1
        return cont
n=input('Digite a quantidade de termos: ')
m=input('Digite a quantidade de termos: ')

a=[]

for i in range (0,n,1):
    a.append(input('Digite os valores da lista a: ')
    
b=[]

for i in range (0,m,1):
    b.append(input('Digite os valores da lista b: ')

print contido(a,b)