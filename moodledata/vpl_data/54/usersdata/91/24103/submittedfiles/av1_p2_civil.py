# -*- coding: utf-8 -*-
from __future__ import division
import math

def pinomaior(a):
    t=a[0]
    for i in range(0,len(a),1):
        if a[i]>t:
            t=a[i]
    return t
    
def pinomenor(a):
    t=a[0]
    for i in range(0,len(a),1):
        if a[i]<t:
            t=a[i]
    return t
    
def pino(a,m):
    x=math.fabs(pinomaior(a)-m)
    y=math.fabs(pinomenor(a)-m)
    total=(x+y)
    
n=input('digite a quantidade de pinos:')
m=input('digite a altura final:')
a=[]

for i in range(0,n,1):
    a.append(input('digite o elemento:'))

t=pino(a,m)
print t