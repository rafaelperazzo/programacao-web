# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite n: ')
a=[]
for i in range(0, n, 1):
    a.append(input('Digite um valor de a: '))
e= input('Digite e: ')
s= input('Digite s: ')

soma=0
for i in range(e, s+1, 1):
    soma=soma+ a[i]

print soma