# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
def pi(x):
    s=3
    a=0
    i1=2
    i2=3
    i3=4
    while(a<x):
        y=((4)/(i1*i2*i3))
        if (i3)%4==0:
            s=s+y
        else:
            s=s-y
        i1=i1+2
        i2=i2+2
        i3=i3+2
        a=a+1
    return s   
m=input('digite o valor de m:')
c=pi(m)
print(c)