# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite a:')
b=input('digite b:')
c=input('digite c:')
if (c%a)%b==0:
    qa=c//a
    print qa
    qb=(c%a)//b
    print b
else:
    print ('N')