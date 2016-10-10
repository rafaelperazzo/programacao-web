# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('digite um numero:'))
b=int(input('digite um numero:'))

mdc=a

while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
print mdc
