# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite o valor de n: ')

cont=0
max=0
for i in range(1,n+1,1):
    a= input('Digite o valor de a: ')
    if i==1:
        vc=a
    else:
        if vc<a:
            cont=cont+1
        if cont>max:
            max= cont
    a=vc
    
