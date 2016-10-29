# -*- coding: utf-8 -*-
from __future__ import division

p=input('Digite o valor de p:')
q=input('Digite o valor de q:')
cont=0
cont2=0
c=p

while True:
    c=c//10
    cont=cont+1
    if c<1:
        break
    r=cont

o=r*10

while True:
    if q//o==p:
        cont2=1
        break
    else:
        q=q//10
    if q<1:
        break
        if cont2==1:
            print 'S'
        else:
            print 'N'
    