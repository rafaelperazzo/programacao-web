# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de pinos:')
m=input('digite a altura desejada para os pinos:')

a=[]
for i in range(0,n+1,1):
    a.append(input('digite a altura dos pinos:')

cont=0
for l in range(1,n,1):
    if a[l]>m and a[l+1]>m:
        a[l]=a[l]-1
        a[l+1]=a[l+1]-1
        cont=cont+1
    if a[l]<m and a[l+1]<m:
        a[l]=a[l]+1
        a[l+1]=a[l+1]+1
        cont=cont+1
    if a[l]<m:
        a[l]=a[l]+1
        cont=cont+1
    if a[l]>m:
        a[l]=a[l]-1
        cont=cont+1
        
print(cont)
    

