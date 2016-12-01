# -*- coding: utf-8 -*-
from __future__ import division

x=input("Digite a quantidade de pinos na fechadura:")
z=input("Digite a altura em que eles devem ficar:")

a=[]
i=1
while i<=x:
    a.append(input("Digite a altura de um pino:"))
    i=i+1
cont=0
k=0
while k<(x-1):
    while a[k]>z and a[k+1]>z:
        a[k]=a[k]-1
        a[k+1]=a[k+1]-1
        cont=cont+1
    while a[k]<z and a[k+1]<z:
        a[k]=a[k]+1
        a[k+1]=a[k+1]+1
        cont=cont+1
    while a[k]>z:
        a[k]=a[k]+1
        cont=cont+1
    while a[k]<m:
        a[k]=a[k]+1
        cont=cont+1
    k=k+1
    
if a[k]!=m:
    while a[k]>m:
        a[k]=a[k]-1
        cont=cont+1
    while a[k]<m:
        a[k]=a[k]+1
        cont=cont+1
print cont
print lista

        