# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('digite um valor:')

while n>0:
    x=input('digite o valor:')
    y=input('digite o valor:')
    if x>=0 and y>=0 and x**2+y**2<=1:
        print ('SIM')
        else:
            ('NAO')
            n=n-1