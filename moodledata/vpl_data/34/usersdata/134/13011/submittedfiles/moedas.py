# -*- coding: utf-8 -*-
from __future__ import division
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

aa = c//a
bb = c//b
m1=c%a
m2=c%b
if m1==0:
    print ('%d' %aa)
    print ('0')
elif m2==0:
    print ('0')
    print ('%d' %bb)

elif m1!=0 and m1%b==0:
    bb = m1//b
    print ('%d' %aa)
    print ('%d' %bb)


