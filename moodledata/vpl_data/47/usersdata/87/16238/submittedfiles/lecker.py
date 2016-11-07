# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if x[i]>x[i+1]:
                cont=cont+1
            if x[i]<x[i+1]>x[i+2]:
                cont=cont+1
            if x[i+1]<x[i+2]>x[i+3]:
                cont=cont+1
            if x[i+2]<x[i+3]:
                cont=cont+1
        if cont==1:
            return true
        else:
            return false
        
a=[]
b=[]
n=input("digite a quantidade de elementos:")
for i in range(0,n,1):
    a.append(input("digite elemento:"))
for i in range(0,n,1):
    b.append(input("digite elemento:"))


if lecker(a):
    print("S")
else:
    print("N")
if lecker(b):
    print("S")
else:
    print("N")