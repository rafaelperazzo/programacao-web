# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite o valor de n:'))
a=[]
for i in range(1,n+1,1):
    valor=int(input('digite o valor:'))
cont=0
for i in range(0,len(a),1):
    if i==0:
        if a[i]>a[i+1]:
            cont=cont+1
    elif i==len(a)-1:
        if a[i]>a[i-1]:
            cont=cont+1 
    else:
        if a[i]>a[i+1] and a[i]>a[i-1]:
            cont=cont+1
if cont==1:
    print('LECKER')
else:
    print('NAO')