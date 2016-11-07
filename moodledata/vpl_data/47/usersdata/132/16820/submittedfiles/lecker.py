# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    c=0    
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                c=c+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                c=c+1
        else:
            if lista[i]>lista[i+1] and lista[i] > lista[i-1]:
                c=c+1
    if c==1:
        return True
    else:
        return False
a=[]
b=[]
n=input('digite a quantidade de termos das listas:')
for i in range(0,n,1):
    a.append(input('digite o valor de a:'))
for i in range(0,n,1):
    b.append(input('digite o valor de b:'))
if lecker(a):
    print('s')
else:
    print('n')
if lecker(b):
    print('s')
else:
    print('n')
    