# -*- coding: utf-8 -*-
from __future__ import division

def iguais(l1,l2):
    cont=0
    for j in range(0,len(l1),1):
        for i in range(0,len(l2),1):
            if l2[i]==l1[j]:
                cont=cont+1
    return cont

a=[]
b=[]
n=input("valor de n:")
m=input("valor de m:")
for i in range (0,n,1):
    a.append(input("digite elementos:"))
for i in range (0,m,1):
    b.append(input("digite elementos:"))
    
print(iguais(a,b))