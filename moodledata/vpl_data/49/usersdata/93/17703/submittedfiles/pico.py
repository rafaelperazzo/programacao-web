# -*- coding: utf-8 -*-
from __future__ import division

def pico(a):
    if len(a)==1:
        return 'N'
    if a[1]<=a[0]:
        return 'N'
    for i in range(0,len(a),1):
        c=i
        if i==len(a)-1:
            return 'N'
            break
        if a[i+1]<=a[i]:
            break
    if a[1]>a[0] and c!=len(a)-1 and len(a)!=1:
        for i in range(c,len(a)-1,1):
            if a[i+1]>=a[i]:
                return 'N'
                break
            if i==len(a)-2:
                return 'S'
                break
n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('elemento: '))
print(pico(a))
