# -*- coding: utf-8 -*-
from __future__ import division
p=input('Digite p: ')
q=input('Digite q: ')
cont=0
while p>=1 :
    cont=cont+1
    p=p/10
i=10**cont
while True:
    if q%i==p:
        print('S')
        break
    q=q//10
    if q<p:
        print('N')
        break
    
