# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor da primeira moeda:'))
b=int(input('digite o valor da segunda moeda:'))
c=int(input('digite o valor da cédula:'))
qa=(c//a)
if (c%a)==0:
    print (qa)
    print '0'
elif (c%a)>=b and ((c%a)%b)==0:
        qb=((c%a)/b)
        print ('%d' %qa)
        print ('%d' %qb)

else:
    print 'N'
