# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    c=[]
    for i in range(0,len(a)-1,1):
        b=a[i+1]-a[i]
        if(b<0):
            b=(-1)*b
        c.append(b)
    return c
    
def maiordegrau(c):
    maior=0
    for i in range(0,len(c)-1,1):
        if c[i]>c[i+1]:
            maior=c[i]
        if maior<c[i+1]:
            maior=c[i+1]
    return maior
        
n=input("Digite um número: ")
a=[]
for i in range (0,n,1):
    a.append(input("Digite um número: "))
c=degrau(a)
m=maiordegrau(c)
print m
