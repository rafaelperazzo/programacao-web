# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de a:  ')
b=input('Digite o valor de b:  ')
c=input('Digite o valor de c:  ')

if a>=b :
    w=c//a
    r=(c%a)//b
    if (c%a)%b==0 :
        print (w)
        print (r)
    else :
        print ('N')
else :
    r=c//b
    w=(c%b)//a
    if (c%b)%a==0 :
        print (w)
        print (r)
    else :
        print ('N')
