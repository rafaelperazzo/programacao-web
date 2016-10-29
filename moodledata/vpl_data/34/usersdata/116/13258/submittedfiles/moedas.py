# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('insira o valor de a:'))
b=int(input('insira o valor de b:'))
c=int(input('insira o valor de c:'))
cont=0
p=0
while p<=c:
    q=1
    
    while q<=c:
        if c==((p*a)+(q*b)):
            m=p
            n=q
            cont=cont+1
            break
        q=q+1
    p=p+1
    
if cont==0:
    print ('N')
else:
    print (m)
    print (n)