# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input(' digite a:')
b=input(' digite b:')
i=2
if a>=b:
    i=a
else:
    i=b
while True:
    if a%i==0 and b%i==0:
        print(i)
        break
    i=i-1