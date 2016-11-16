# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if i==0:
            if lista[i]<lista[1]:
                cont=cont+1
        
        if i==(len(lista)-1):
            if lista[len(lista)-1]<lista[len(lista)-2]:
                cont=cont+1
        
        else:
            if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
                cont=cont+1
            
            if lista[i]>lista[i-1] and lista[i]<lista[i+1]:
                cont=cont+1
                
    if cont==(len(lista)-1):
        return True
    else:
        return False
    

n= input('Digite a quantidade de elementos da lista:')

while n<3:
    n= input('Digite a quantidade de elementos da lista:')

a=[]

for i in range (0,n,1):
    a.append(input('Digite os termos da lista:'))
    
    
if pico(a):
    print ('S')
else:
    print ('N')
