# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite o valor de n:'))
l=[]

for i in range (0,n,1):
    l.append(input('Digite os elementos da lista:'))

soma=0

for i in range (0,n,1):
    soma=soma+l[i]
    
    media=soma/n
    
    
print l[0]
    
print l[n-1]

print (media)

print l[n]


    



    
    


    


