# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if (lista[i]>lista[i-1]) and (lista[i]>lista[i+1]):
                cont=cont+1
    if cont==1:
        return True
    else:
        return False

s=[]
m=[]
n=input('Digite o numero de elementos: ')

for j in range(0,n,1):
    s.append(input('Digite um numero: '))
for k in range(0,n,1):
    m.append(input('Digite um numero: '))
    
if lecker(s):
    print ('S')
else:
    print ('N')
if lecker(m):
    print ('S')
else:
    print ('N')



