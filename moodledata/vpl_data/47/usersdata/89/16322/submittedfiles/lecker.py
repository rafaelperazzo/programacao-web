# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    contador=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]>lista[1]:
                contador=contador+1
        if i==(len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                contador=contador+1
        else:
            if lista[i]>lista[i-1] and  lista[i]>lista[i+1]:
                contador=contador+1
    if contador==1:
        return True
    else:
        return False
a=[]
b=[]
n=input('digite a quantidade de elementos:')

for i in range(0,n,1):
    a.append(input('digite um elemento:'))
for i in range(0,n,1):
    b.append(input('digite um elemento:'))

if lecker(a):
    print('S')
else:
    print('N')
    
if lecker(b):
    print('S')
else:
    print('N')


    

