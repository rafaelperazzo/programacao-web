# -*- coding: utf-8 -*-
from __future__ import division
import math

P=input('digite a posição da porta P:')
R=input('digite a posição da porta R:')
if P==0:
    print('C')
elif P==1 and R==0:
    print('B')
else:
    print('A')