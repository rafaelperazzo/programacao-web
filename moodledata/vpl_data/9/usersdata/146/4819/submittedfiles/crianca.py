# -*- coding: utf-8 -*-
from __future__ import division

a = input('DIGITE O  VALOR DE P1: ')
b = input('DIGITE O  VALOR DE C1: ')
c = input('DIGITE O  VALOR DE P2: ')
d = input('DIGITE O  VALOR DE C2: ')

if a*b==c*d:
    print '0'

elif a*b>c*d:
    print '-1'

else:
    print '1'