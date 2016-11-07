# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    contador=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i-1]:
                contador=contador+1
        elif i==len(lista)-1:
            if lista[len(lista)-1]>lista[len(lista)-2]:
                contador=contador+1
        else:
            if lista[i]>lista[i+1]:
                contador==1
                    
        return True
    else:
        return False

a=[]
b=[]

n = input ('Digite o valor de n:')
for i in range (0,n,1):
    a.append (input('Digite o valor de a:'))
for i in range (0, n, 1):
    b.append (input('Digite o valor de b:'))
    
if lecker(a):
    print ('S')
else:
    print ('N')

if lecker(b):
    print ('S')
else:
    print ('N')




