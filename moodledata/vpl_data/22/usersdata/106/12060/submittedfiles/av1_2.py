# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int (input ('Digite um número entre 0 e 9 referente à primeira cor:'))
b = int (input ('Digite um número entre 0 e 9 referente à segunda cor:'))
c = int (input ('Digite um número entre 0 e 9 referente à terceira cor:'))
d = int (input ('Digite um número entre 0 e 9 referente à quarta cor:'))

if a==c or b==d:
    if a!=b and b !=c and c!=d:
        print ('V')
    else:
        print('F')
else:
    print ('F')