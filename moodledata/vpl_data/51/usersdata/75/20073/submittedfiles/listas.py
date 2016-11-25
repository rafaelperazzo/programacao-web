# -*- coding: utf-8 -*-
from __future__ import division

def absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
def altura(lista):
    maior=absoluto(lista[0]-lista[1])
    for i in range(0,len(lista),1):
        if i==0:
            if absoluto((lista[i]-lista[i+1]))>maior:
                maior=absoluto(lista[i]-lista[i+1])
        elif i==len(lista)-1:
            if absoluto(lista[len(lista)-2]-lista[len(lista)-1])>maior:
                maior=absoluto(lista[len(lista)-2]-lista[len(lista)-1])
        else:
            if absoluto(lista[i]-lista[i+1])>maior:
                maior=absoluto(lista[i]-lista[i+1])
    
    return maior 
                
        
n=int(input('Digite a quantidade de termos da lista:'))

while n<2:
    n=int(input('Digite a quantidade de termos da lista:'))
    
a=[]

for i in range (0,n,1):
    a.append(input('Digite os elementos da lista:'))
    
print altura(a)

    
    

    
            
    
            
 

