# -*- coding: utf-8 -*-
from __future__ import division

def ab(a):
    if a<0:
        return a*(-1)
    else:
        return a
        
def m(b):
    m=b[0]
    for i in range(0,len(b),1):
        if b[i]>m:
            m=b[i]
    return m
    
def mr(b):
    mr=b[0]
    for i in range(0,len(b),1):
        if b[i]<mr:
            mr=b[i]
    return mr
    
def h(b,h):
    soma=(ab(m(b)-h)+ab(mr(b)-h))
    return soma


n=input('Digite n: ')
o=input('Digite a altura:')

l=[]
for i in range(0,n,1):
    l.append(input('Digite um número:'))

print ((h(l,o)))