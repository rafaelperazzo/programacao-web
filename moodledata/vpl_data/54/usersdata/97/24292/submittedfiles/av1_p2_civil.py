# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de pinos:')
m=input('digite a altura desejada para os pinos:')

i=0
a=[]
while i<=n:
    a.append(input('digite a altura dos pinos:')

l=0
cont=0
while l<(n-1):
    while a[l]>m and a[l+1]>m:
        a[l]=a[l]-1
        a[l+1]=a[l+1]-1
        cont=cont+1
    while a[l]<m and a[l+1]<m:
        a[l]=a[l]+1
        a[l+1]=a[l+1]+1
        cont=cont+1
    while a[l]<m:
        a[l]=a[l]+1
        cont=cont+1
    while a[l]>m:
        a[l]=a[l]-1
        cont=cont+1
while a[l]!=m:
    if a[l]>m:
        a[l]=a[l]-1
        cont=cont+1
    if a[l]<m:
        a[l]=a[l]+1
        cont=cont+1

print(cont)
    

