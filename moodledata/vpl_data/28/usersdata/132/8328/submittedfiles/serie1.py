# -*- coding: utf-8 -*-
from __future__ import division
import math
from __future__ import division
a=input(' digite o numero de termos:')
i=0
s=0
while(i<=a):
    x=(-1**i)/(2*i + 1)
    s=s+x
    i=i+1
pi=4*s
print(pi)