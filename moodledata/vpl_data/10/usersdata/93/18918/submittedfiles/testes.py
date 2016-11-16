# -*- coding: utf-8 -*-
from __future__ import division

#COMECE9 AQUI ABAIXO
def congru(a,b,m,x0,n):
    c=[]
    c.append(x0)
    for i in range(0,n-1,1):
        c.append(c[i]*a+b)
    for i in range(0,n,1):
        c[i]=c[i]/m
    return(c)
print(congru(2,3,2,4,7))