# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('Digite primeiro número: '))
p=int(input('Digite segundo número: '))
i=1
for i in range (1,p+1,1):
    if n%i==0 and p%i==0:
        c=i
print (c)

