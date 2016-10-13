# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('n:'))
i=1
cont=0
while (n//i==0):
    cont=cont+1
    i=i*10
print(cont)

