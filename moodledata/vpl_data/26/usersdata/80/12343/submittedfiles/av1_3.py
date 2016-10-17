# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o primeiro numero:')
if a<10:
    print('1')
else:
    x=2
    while a%10>=10:
        print(x)
    x=x+1    