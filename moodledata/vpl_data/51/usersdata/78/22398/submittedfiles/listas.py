# -*- coding: utf-8 -*-
from __future__ import division


def absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x

def degrau(a):
    
    maior=absoluto(a[0]-a[1])
    for i in range(0,len(a),1):
        if i==0:
            if absoluto(a[0]-a[1])>maior:
                maior=absoluto(a[0]-a[1])
        elif i==(len(a)-1):
            if absoluto(a[len(a)-2]-a[len(a)-1])>maior:
                maior=absoluto(a[len(a)-2]-a[len(a)-1])
        else:
            if absoluto(a[i]-a[i+1])>maior:
                maior=absoluto(a[i]-a[i+1])
    return maior
a=[]
n=input('digite a quantidade de n:')
for i in range(0,n,1):
    a.append(input('digite o valor de a:'))

print (degrau(a))