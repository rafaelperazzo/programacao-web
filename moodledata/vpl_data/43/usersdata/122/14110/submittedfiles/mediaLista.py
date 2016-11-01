# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de valores:')
l=[]
for i in range (0,n,1):
    l.apeend(input('Digite um elemento:'))
    
for i in range (l[0],l[n],1):
    m=i/n
    print m
    print l[0]
    print l[n]