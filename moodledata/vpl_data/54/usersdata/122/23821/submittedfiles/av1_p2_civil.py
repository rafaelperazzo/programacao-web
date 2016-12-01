# -*- coding: utf-8 -*-
from __future__ import division
import math
        
def fechadura (lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if a[i]==a[i]+1:
            cont=cont+0
        elif a[i]!=a[i]+1:
            t=math.fabs(a[i]-a[i]-1)
            cont=cont+t
    return cont
    
n=input('Digite a quantidade de pinos:')
m=input('Digite a altura dos pinos:')
a=[]
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
    
print fechadura(a)
            
            
