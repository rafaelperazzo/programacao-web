# -*- coding: utf-8 -*-
from __future__ import division
import math
valor=int(input('digite o valor:'))
if valor>0:
    not20=valor/20
    print('%d' %not20)
    not10=(valor%20)/10
    print('%d' %not10)
    not5=(not10%10)/5
    print('%d' %not5)