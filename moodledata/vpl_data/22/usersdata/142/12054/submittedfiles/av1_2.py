# -*- coding: utf-8 -*-
from __future__ import division
import math

n1=input('Digite o numero 1:')
n2=input('Digite o numero 2:')
n3=input('Digite o numero 3:')
n4=input('Digite o numero 4:')

if n1 == n3 and n1!=n2 and n2!=n3 and n3!=n4 and n2!=n4:
    print 'V'
elif n2 == n4 and n1!=n2 and n2!=n3 and n3!=n4 and n1!=n3:
    print 'V'
else:
    print 'F'