# -*- coding: utf-8 -*-
from __future__ import division

n = int( input ('insira um valor para n:'))

a=[]

for i in range (0,n,1):
    a.append(input('insira um valor para lista:'))
    
cont=0
cont2=0

for i in range (0,len(a)-1,1):
    if a[i]-a[i+1]<0:
        cont=(a[i]-a[i+1])*(-1)
        
    else:
        cont=a[i]-a[i+1]
        
    if cont>cont2:
        cont2=cont
        
print cont2