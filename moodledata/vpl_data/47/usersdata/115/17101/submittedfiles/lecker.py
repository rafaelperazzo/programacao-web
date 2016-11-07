# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range(0,len(a)1):
        if i==0:
            if a[i]>a[i+1]:
                cont=cont+1
        elif i ==len(a)-1:
            if a[i]>a[i-1]:
                cont=cont+1
        else:
            if a[i]>a[i+1] and a[i]>a[i-1]:
                cont=cont+1

a=[]
b=[]
n=input('digite a quantidade:')
for i in range (0,n,1):
    a.append(input('digite um elemento:')
for i in range (0,n,1):
    b.append(input('digite um elemento:')
if a=lecker(lista):
    print 'S'
    else:
        print 'N'
elif b=lecker(lista):
    print 'S'
    else:
        print 'N'

    

        