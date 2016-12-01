# -*- coding: utf-8 -*-
from __future__ import division

#entrada
m=input('altura do pino:')
n=input('quantidade de pinos:')
#código 
i=1
a=[]
while i<=n:
    a.append(input('tamanho do pino:'))
    i=i+1
j=0
cont=0
while j<(n-1):
    while a[j]>m and a[j+1]>m:
        a[j]=a[j]-1
        a[j+1]=a[j+1]-1
        cont=cont+1
    while a[j]<m and a[j+1]<m:
        
       a[j]=a[j]+1
       a[j+1]=a[j+1]+1
        cont=cont+1
    while a[j]>m:
        a[j]=a[j]-1
        cont=cont+1
    while a[j]<m:
        a[j]=a[j]+1
        cont=cont+1
    j=j+1
if a[j]!=m:
    while a[j]>m:
        a[j]=a[j]-1
        cont=cont+1
    while lista[j]<m:
        a[j]=a[j]+1
        cont=cont+1
print cont

            
        
    
