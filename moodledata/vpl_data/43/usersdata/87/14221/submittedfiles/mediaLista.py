# -*- coding: utf-8 -*-
from __future__ import division

n=int(input("digite valor de n:"))
a= []
i=0
media=0
for i in range (0,n,1):
    a.append(input("digite o elemento:"))
for i in range (0,n,1):
    media=media + a[i]
m=media/(len(a))
print ("%.2f"%a[0])
print ("%.2f"%a[n-1])
print ("%.2f"%media)
print (a)