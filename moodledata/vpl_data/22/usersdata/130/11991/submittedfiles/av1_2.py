# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('Digite o valor de d:')
if a==c or b==d:
    if b!=d or a!=c:
        if a!=b or b!=c or c!=d:
            print('V')
        else:
            print('F')
    else:
        print('F')
else:
    print('F')
