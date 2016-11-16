# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de números das listas:')
a=[]
b=[]
c=[]
for i in range (0,n,1):
    a.append(input('Digite um valor da lista A:'))
    b.append(input('Digite um valor da lista B:'))
    c.append(input('Digite um valor da lista C:'))

def crescente:
    for i in range (a,len(a)-1,1):
        if a[i]>a[i+1]:
            print 'S' 