# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite n: '))
a=[]
for i in range(0, n, 1):
    a.append(input('Digite um valor de b: '))

m= input('Digite m: '))
a=[]
for i in range(0, m, 1):
    a.append(input('Digite um valor de b: '))

def  contidos(x,y):
    z=[]
    for i in range(0, len(y), 1):
        if y[i] in x:
            return print y[i]

