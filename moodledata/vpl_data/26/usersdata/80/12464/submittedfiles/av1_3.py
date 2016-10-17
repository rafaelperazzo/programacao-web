# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o numero inteiro:')
b=input('Digite o numero real:')
x=(a//10)
y=1
while x>=10:
    x=(x//10)
    y=y+1
    print(y)
    