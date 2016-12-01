# -*- coding: utf-8 -*-
from __future__ import division
n=input('n:')
a=[]
for i in range(0,n,1):
    a.append(input('a:'))
pe= input('digite entrada:')
ps= input('digite saida:')
vidas=0
for i in range(pe,ps+1,1):
    vidas=vidas+a[i]
print (vidas)

