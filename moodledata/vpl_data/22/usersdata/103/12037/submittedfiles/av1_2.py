# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite um número correspondente à primeira cor:')
b=input('digite um número correspondente à segunda cor:')
c=input('digite um número correspondente à terceira cor:')
d=input('digite um número correspondente à quarta cor:')
if a==b or b==c or a==d:
    print('F')
else: 
    if a==c or b==d:
        print('N')