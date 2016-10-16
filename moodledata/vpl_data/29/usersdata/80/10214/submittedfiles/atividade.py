# -*- coding: utf-8 -*-
from __future__ import division
import math

N=int(input('Digite o numero n:'))
C=0
while N>0:
    N=N//10
    C=C+1
print C

