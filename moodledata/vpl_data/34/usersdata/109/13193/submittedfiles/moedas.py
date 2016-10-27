# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')

if a>b:
    d=c//a
    r=c%a
    e=r//b
    if r%b==0:
        print d
        print e