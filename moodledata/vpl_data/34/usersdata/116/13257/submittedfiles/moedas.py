# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('insira o valor de a:'))
b=int(input('insira o valor de b:'))
c=int(input('insira o valor de c:'))

p=0
while p<=c:
    q=1
    cont=0
    while q<=c:
        if c==((p*a)+(q*b)):
            print p
            print q
            cont=cont+1
            break
        q=q+1
    p=p+1
    
if cont==0:
    print ('N')
        