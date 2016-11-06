# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite o valorde n:')
a=[]
for i in range(0,n,1):
    a.append=input('Digite um elemento:')
s1=0
con1=0
for i in range(0,n,1):
    if a[i]%2==0:
        s1=s1+a[i]
        con1=con1+1
s2=0
con2=0
for i in range(0,n,1):
    if a[i]%2!=0:
        s2=s2+a[i]
        con2=con2+1        
print(s2)
print(s1)
print(con2)
print(con1)
print(a)