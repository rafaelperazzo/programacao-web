# -*- coding: utf-8 -*-
from __future__ import division

def iguais(l1,l2):
    cont=0
    for j in range (0,len(l1),1):
        for i in range (0,len(l2),1):
            if l2[i]==l1[j]:
                cont=cont+1
                
    return cont 
    
n = input ('insira a quantidade de elementos da primeira lista:') 
m = input ('insira a quantidade de elementos da segunda lista:')
a=[]
b=[]

for i in range (0,n,1):
    a.append(input('insira um valor para a primeira lista:')) 
for i in range (0,m,1):
    b.append(input('insira um valor para a segunda lista:'))

print iguais(a,b)
