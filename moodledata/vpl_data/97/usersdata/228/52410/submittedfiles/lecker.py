# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite o número de elementos:'))
lista1=[]
lista2=[]
 
for i in range (0,n,1):
    termo=int(input('digite o termo:'))
    termo.append(lista1)

 
for i in range (0,n,1):
    termo=int(input('digite o termo:'))
    termo.append(lista2)
    
def leker(a):
        
    cont=0
    if lista[0]>lista[1]:
       cont=cont+1
    
    elif lista[n]>lista[n-1]:
       cont=cont+1

    else:
        for i in range(lista[1],len(lista),1):
            if lista[i-1]<lista[i]<lista[i+1]:
            cont=cont+1
            if cont==1:
                return True
            else:
                return False
if leker(lista1):
    print('S')
elif leker(lista1)==False:
    print('N')
if leker(lista2):
    print('S')
elif leker(lista2)==False:
    print('N')
    
    
    
    
    