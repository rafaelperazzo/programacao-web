# -*- coding: utf-8 -*-
from __future__ import division
import math

R = input('Digite a posição de R:')
P = input('Digite a posição de P:')

if R==1 and P==0:
    print ('C')
elif R==P==1:
    print ('A')
elif R==0 and P==1:
    print ('B')