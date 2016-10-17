# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o numero inteiro:')
x=(a//10)
y=2
while x>=10:
    x=(x//10)
    y=y+1
    print(y)
else:
    if a>9 and a<100:
        print('2')
    else:
        print('1')
    