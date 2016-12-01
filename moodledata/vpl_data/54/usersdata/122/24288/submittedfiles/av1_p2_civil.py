# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de pinos:')
m=input('Digite a altura dos pinos:')

a=[]
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
    

i=0
cont=0

while i<n-1:
    while a[i]>m and a[i+1]>m:
        a[i]=a[i]-1
        a[i+1]=a[i+1]-1
        cont=cont+1
    while a[i]<m and a[i+1]<m:
        a[i]=a[i]+1
        a[i+1]=a[i+1]+1
        con=cont+1
    while a[i]>m:
        a[i]=ai[i]-1
        cont=cont+1
    while a[i]<m:
        a[i]=a[i]+1
        cont=cont+1
    i=i+1
if a[i]!=m:
    while a[i]>m:
        a[i]=a[i]-1
        cont=cont+1
    while a[i]<m:
        a[i]=a[i]+1
        cont=cont+1

print cont
