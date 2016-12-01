# -*- coding: utf-8 -*-
from __future__ import division

N=input('digite a quantidade de pinos:')
m=input('digite a altura desejada para os pinos:')

i=0
a=[]
while i<=N:
    a.append(input('digite a altura dos pinos:')
    i=i+1

k=0
cont=0

while k<(N-1):
    while a[k]>m and a[k+1]>m:
        a[k]=a[k]-1
        a[k+1]=a[k+1]-1
        cont=cont+1
    while a[k]<m and a[k+1]<m:
        a[k]=a[k]+1
        a[k+1]=a[k+1]+1
        cont=cont+1
    while a[k]<m:
        a[k]=a[k]+1
        cont=cont+1
    while a[k]>m:
        a[k]=a[k]-1
        cont=cont+1
        k=k+1
while a[k]!=m:
    if a[k]>m:
        a[k]=a[k]-1
        cont=cont+1
    if a[k]<m:
        a[k]=a[k]+1
        cont=cont+1

print(cont)
    

