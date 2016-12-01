# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de pinos:')
m=input('Digite a altura dos pinos:')

def fechadura (a):
    cont=0
    t=0
    for i in range (0,len(a)-1,1):
        if a[i]=!m and a[i+1]==m:
            t=t+math.fabs(a[i]-m)
            cont=cont+t
    return cont
    
            
    

a=[]
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
    
print fechadura(a)
            
            
