# -*- coding: utf-8 -*-
from __future__ import division

def comp(a):
    cont=0
    if a[0]>a[1]:
        cont=cont+1
    if a[len(a)-1]>a[len(a)-2]:
        cont=cont+1
    for i in range (1,len(a)-1,1):
        if a[i]>a[i+1] and a[i]>a[i-1]:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
        
        
a=[]
b=[]
n=int(input("Digite um valor: "))
for i in range (0,n,1):
    a.append(input("Digite os valores da lista: "))
for i in range (0,n,1):
    b.append(input("Digite os valores da lista: "))
    
if comp(a):
    print ("S")
else:
    print ("N")
if comp(b):
    print ("S")
else:
    print ("N")
    
