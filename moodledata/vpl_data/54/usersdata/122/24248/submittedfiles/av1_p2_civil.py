# -*- coding: utf-8 -*-
from __future__ import division
import math

i=0
cont=0

while i<n-1:
    while a[i]>m and a[i+1]>m:
        a[i]=a[i]-1
        a[i+1]=a[i+1]-1
        cont=con+1
    while a[i]<

n=input('Digite a quantidade de pinos:')
m=input('Digite a altura dos pinos:')

a=[]
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
    
print fechadura(a)