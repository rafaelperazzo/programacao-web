# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a :'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c :'))
cont1=0
cont2=0
w=c
for i in range(0,c+1,1):
    if c>=a:
        c=c-a
        cont1=cont1+1
    if c>=b:
        c=c-b
        cont2=cont2+1
    if c>=a:
        n=c//a
        c=c-(a*n)
        cont1=cont1+n
    if c>=b:
        d=c//b
        c=c-(d*b)
        cont2=cont2+d
if (cont1*a)+(cont2*b)-w==0:
    print(cont1)
    print(cont2)
else:
    print('n')
        

  