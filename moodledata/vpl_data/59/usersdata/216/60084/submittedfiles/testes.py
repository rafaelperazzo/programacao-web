# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
def maior(a):
    for i in range(0,len(a),1):
        if a[i]>a[i+1]:
            ma=a[i]
    return (ma)
    
n=int(input('Digite a:'))

for i in range(0,n,1):
    a=[]
    x=int(input('Digite x:'))
    a.append(x)
    
print(maior(a))