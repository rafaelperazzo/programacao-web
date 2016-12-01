# -*- coding: utf-8 -*-
from __future__ import division

n=input('Pinos de fechadura:')
m=input('Tamanho do pino pra destravar:')
a=[]
cont=0

for i in range(0,n,1):
    a.append(input('Tamanho do pino:'))

for j in range(0,(len(a)-1),1):
    while a[j]>m and a[j+1]>m:
        a[j]=a[j]-1
        a[j+1]=a[j+1]-1
        cont=cont+1
    while a[j]<m and a[j+1]+1<m:
        a[j]=a[j]+1
        a[j+1]=a[j+1]+1
        cont=cont+1
    while a[j]>m:
        a[j]=a[j]-1
        cont=cont+1
    while a[j]<m:
        a[j]=a[j]+1
        cont=cont+1
        
if a[len(a)-1]!=m:
    while a[len(a)-1]>m:
        a[len(a)-1]=a[len(a)-1]-1
        cont=cont+1
    while a[len(a)-1]<m:
        a[len(a)-1]=a[len(a)-1]+1
        cont=cont+1

print cont
        