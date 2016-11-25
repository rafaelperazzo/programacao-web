# -*- coding: utf-8 -*-
from __future__ import division

n=input("Entre com a quantidade de termos: ")
l=[]
for i in range(0,n,1):
    l.append(input("Digite o elemento: "))
degrau=0
for i in range(0,len(l)-1,1):
    d=(((l[i+1]-l[i])**2)**0.5)
    if d>degrau:
        degrau=d
print int(degrau)