# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range (0,lista[i],1):
        if lista[0]>lista[0+1]:
            cont=cont+1
        if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
            cont=cont+1
        if lista[n]>lista[n-1]:
            cont=cont+1    
    if cont==1:
        return True
    else:
        return False
        

n=input('Digite n:')
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite a lista a:'))
    
for i in range (0,n,1):
    b.append(input('Digite a lista b:'))
    
if lecker True:
    print('S')
    
else:
    print('N')