# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA

a=input('digite o valor do lado a:')
b=input('digite o valor do lado b:')
c=input('digite o valor do lado c:')

if a<(a+b):
    print('S')
else:
    print('N')
    
if (a^2)=(b^2)+(c^2):
    print('Re')
else:
    if (a^2)>(b^2)+(c^2):
        print('Ob')
    else:
        if (a^2)<(b^2)+(c^2):
            print('Ac')
        