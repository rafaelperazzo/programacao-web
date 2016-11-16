# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de elementos da lista A:')
m=input('Digite a quantidade de elementos da lista B:')
a=[]
b=[]
for i in range (0,n,1):
    a.append(input('Digite o elemento da lista A:'))
for i in range (0,m,1):
    b.append(input('Digite o elemento da lista B:'))
    
    
def elementosiguais(lista1,lista2):
    
    cont=0
    for i in range (0,len(lista1),1):
        for j in range (0,len(lista2),1):
            if a[lista1]==b[lista2]:
                cont=cont+1
                if cont>0:
                    return True
                else: 
                    return False
                    
if elementosiguais(a,b):
    print 'S'
else:
    print 'N'
