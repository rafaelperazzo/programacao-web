# -*- coding: utf-8 -*-
from __future__ import division

def maior_grau(lista):
    for i in range (0,len(lista)-1,1):
        diferenca=lista[i]-lista[i+1]
        if diferenca<0:
            diferenca=(diferenca*(-1)
        
        
    return diferenca 
        
n=int(input('Digite a quantidade de termos da lista:'))

while n<2:
    n=int(input('Digite a quantidade de termos da lista:'))
    
a=[]

for i in range (0,n,1):
    a.append(input('Digite os elementos da lista:'))
    
print maior_grau(a)

    
    

    
            
    
            
 

