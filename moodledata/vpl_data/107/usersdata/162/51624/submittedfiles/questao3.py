# -*- coding: utf-8 -*-
p=int(input('Digite p:'))
q=int(input('Digite q:'))
contador=0
for i in range(2,p,1):
    if p%i==0:
        contador=contador+1
    if contador==0:
        i=i+1
    for i in range(2,q,1):
        if q%i==0:
            contador=contador+1
        if contador==0:
            i=i+1
    if q==p+2:
       print('S')
    else:
       print('N')

