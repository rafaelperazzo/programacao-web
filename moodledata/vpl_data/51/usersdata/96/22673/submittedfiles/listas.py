# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def degrau(a):
    a = []
    for i in range(0,len(a)-1,1):
        b = a[i+1]-a[i]
        if b<0:
            b = (-1)*b
        a.append(b)
    return a

def md(d):
    maior = 0
    for i in range(0,len(d)-1,1):
        if d[i]>d[i+1]:
            maior = d[i]
        if maior<d[i+1]:
            maior = d[i+1]
    return maior

n = input('Digite o valor de n:')
a = []
for i in range(0,n,1):
    a.append(input('Digite o valor do degrau:'))

d = degrau(a)
m = md(d)

print m

