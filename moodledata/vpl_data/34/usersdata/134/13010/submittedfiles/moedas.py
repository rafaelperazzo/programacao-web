# -*- coding: utf-8 -*-
from __future__ import division
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

m1=c%a
m2=c%b
if m1==0:
    print ('%d' %m1)
    print ('0')
elif m2==0:
    print ('0')
    print ('%d' %m2)

elif m1!=0 and m1%b==0:
    m2 = m1/b
    print ('%d' %m1)
    print ('%d' %m2)


