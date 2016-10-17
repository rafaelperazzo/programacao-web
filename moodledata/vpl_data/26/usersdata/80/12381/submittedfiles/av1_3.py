# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite o primeiro numero:'))
x=(a//10)
y=1
while x>=10:
    print(y)
    x=(x//10)
    y=y+1
else:
    print ('2')
    