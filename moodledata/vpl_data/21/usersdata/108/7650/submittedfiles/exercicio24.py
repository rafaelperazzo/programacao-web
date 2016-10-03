# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('Digite o valor de n:'))
m = int (input ('Digite o valor de m:'))
div=1

i=1
while ((n%i==0) and (m%i==0)):
    div=i
    i=i+1

print (i)
