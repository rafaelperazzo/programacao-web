# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
n=input('Digite o valor de n:')
l=[]
lp=[]
li=[]
#PROCESSAMENTO
for i in range(0,n,1):
    l.append(input('Digite o valor:'))
for i in range(0,n,1):
    if l[i]%2==0:
        lp.append(l[i])
    else:
        li.append(l[i])
print sum(li)
print sum(lp)
print len(li)
print len(lp)
print l
