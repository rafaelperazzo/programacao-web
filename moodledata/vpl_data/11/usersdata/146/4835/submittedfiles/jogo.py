# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('DIGITE O  VALOR DE Cv: ')
b = input('DIGITE O  VALOR DE Ce: ')
c = input('DIGITE O  VALOR DE Cs: ')
d = input('DIGITE O  VALOR DE Fv: ')
e = input('DIGITE O  VALOR DE Fe: ')
f = input('DIGITE O  VALOR DE Fs: ')

if a+b>d+e:
    print 'C'

elif a+b<d+e:
    print 'F'

elif c>f:
    print 'C'

elif c<f:
    print 'F'

else:
    print '='