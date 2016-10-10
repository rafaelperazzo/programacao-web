# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('Digite primeiro número: '))
p=int(input('Digite segundo número: '))
i=1
while i<=p :
    if n%i!=0 or p%i!=0:
        i=i+1
print(i)

