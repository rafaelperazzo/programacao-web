# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite o número de elementos:'))
lista1=[]
lista2=[]
 
for i in range (0,n,1):
    termo1=int(input('digite o termo:'))
    lista1.append(termo1)

 
for i in range (0,n,1):
    termo2=int(input('digite o termo:'))
    lista2.append(termo2)
    
def leker(a):
        
    cont=0
    if a[0]>a[1]:
       cont=cont+1
    
    elif a[n]>a[n-1]:
       cont=cont+1

    else:
        for i in range(a[1],len(a),1):
            if a[i-1]<a[i]<a[i+1]:
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
    
    
    
    
    