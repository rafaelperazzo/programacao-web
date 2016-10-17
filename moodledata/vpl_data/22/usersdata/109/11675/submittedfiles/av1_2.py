# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite a primeira cor:')
b=input('Digite a segunda cor:')
c=input('Digite a terceira cor:')
d=input('Digite a quarta cor')

if a==c or b==d:
    print 'V'
elif a==d:
    print 'F'