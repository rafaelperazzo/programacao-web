# -*- coding: utf-8 -*-
from __future__ import division

def comparar(lista):
    cont=0
    if a[0]>a[1]:
        cont=cont+1
    if a[n-1]>a[n-2]:
        cont=cont+1
    for i in range(0,len(lista),1):
    if a[i]!=a[0] and a[i]!=a[n-1]:
        if a[i]>a[i+1] and a[i]>a[i-1]:
            cont=cont+1
a=[]
b=[]
n= int(input('Digite o valor de n: '))

for i in range(0,n,1):
    a.append(input('Digite o termo de a: '))
for i in range(0,n,1):
    b.append(input('Digite o termo de b: '))