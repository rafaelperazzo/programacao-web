# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o primeiro numero:')
b=input('Digite o segundo numero:')
x=a
y=1
if a<10:
    print('1')
while x>=10:
    x=(x//10)
    y=y+1
print(y)


