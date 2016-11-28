# -*- coding: utf-8 -*-
from __future__ import division

def degrau(a):
    s=[]
    for i in range(0,len(a)-1,1):
        b=a[i+1]-a[i]
        if (b < 0):
            b=(-1)*b
        s.append(b)
    return s

def maiordegrau(s):
    maior=0
    for i in range(0,len(s)-1,1):
        if s[i]>s[i+1]:
            maior=s[i]
        if maior<s[i+1]:
            maior=s[i+1]
    return maior
    

n=input('digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('digite a:'))
s=degrau(a)
m=maiordegrau(s)
print (m)

