# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input ('Digite um número entre 0 e 9 referente à primeira cor:')
b = input ('Digite um número entre 0 e 9 referente à segunda cor:')
c = input ('Digite um número entre 0 e 9 referente à terceira cor:')
d = input ('Digite um número entre 0 e 9 referente à quarta cor:')

if a==c or b==d:
    print ('V')
else:
    print ('F')