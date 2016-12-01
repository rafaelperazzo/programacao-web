# -*- coding: utf-8 -*-
from __future__ import division

x=input("Digite a quantidade de pinos na fechadura:")
z=input("Digite a altura em que eles devem ficar:")

a=[]

for i in range (0,n,1):
    a.append(input("Digite o tamanho de um pino:")
    
cont=0
k=0
while k<(n-1):
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

        