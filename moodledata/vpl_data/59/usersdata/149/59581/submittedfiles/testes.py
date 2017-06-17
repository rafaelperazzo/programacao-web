# -*- coding: utf-8 -*-
import itertools 
n=int(input('digíte a quantidade de números:'))
z=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento desta lista:'))
    z.append(lista)
    
permut=list(itertools.permutations(z))
print(permut)
    

    
    
    
    
    
    
    
    

    