# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            cont=cont+1
            
    elif i==0:
        if (lista[len(lista)-1]>lista[len(lista)-2]):
            cont=cont+1
            
    else:
        if lista[i]>(lista[i+]) and lista[i]>lista[lista[i-1]):
            cont=cont+1
    
    if cont==1:
        return True
      
     else:
         return False
         
n=input('digite n: ')

a=[]
b=[]
cont=0

for i in range(0,n,1):
    a.append(input('digite um elemento de a: '))
    
for i in range(0,n,1):
    b.append(input('digite um elemento de b: '))
    
if lecker(a):
    print('S')
else:
    print('N')
    
if lecker(b):
    print('S')
else:
    print('N')
    

    