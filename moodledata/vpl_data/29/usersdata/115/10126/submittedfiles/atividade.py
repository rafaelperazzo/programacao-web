# -*- coding: utf-8 -*-
from __future__ import division
import math
N=int(input('Digite aqui o valor de N:'))
F=0
while N>0:
    N=N//10
    F=F+1
print (F)
