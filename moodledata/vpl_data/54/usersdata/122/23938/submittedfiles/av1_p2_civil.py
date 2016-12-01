# -*- coding: utf-8 -*-
from __future__ import division
import math
        
def fechadura (a):
    cont=0
    for i in range (0,len(lista)-1,1):
        if a[i]==m and a[i]+1==m:
            cont=cont+0
        elif a[i]=!m and a[i]+1==m:
            t=math.fabs(a[i]-m)
        elif a[i]==m and a[i]=!m:
            t=math.fabs((a[i]+1)-m)
    return cont
            
    
n=input('Digite a quantidade de pinos:')
m=input('Digite a altura dos pinos:')
a=[]
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
    
print fechadura(a)
            
            
