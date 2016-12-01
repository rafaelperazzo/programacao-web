# -*- coding: utf-8 -*-
from __future__ import division
import math

def fechadura (a):
    cont=0
    for i in range (0,len(a)-1,1):
        while a[i]>m and a[i+1]>m:
            a[i]=a[i]-1
            a[i+1]=a[i+1]-1
            cont=cont+1
            
        while a[i]<m and a[i+1]<m:
            a[i]=a[i]+1
            a[i+1]=a[i+1]+1
            cont=cont+1
        
        while a[i]>m:
            a[i]=a[i]-1
            cont=cont+1
            
        while a[i]<m:
            a[i]=a[i]+1
            cont=cont+1
        i=i+1
            
    if a[i]!=m:
        while[i]>m:
            a[i]=a[i]-1
            cont=cont+1
            
        while a[i]<m:
            a[i]=a[i]+1
            cont=cont+1
    
    return cont

n=input('Digite a quantidade de pinos:')
m=input('Digite a altura dos pinos:')

a=[]
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
    
print fechadura(a)