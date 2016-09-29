# -*- coding: utf-8 -*-
from __future__ import division
import math

R = input('Digite a posição de R:')
P = input('Digite a posição de P:')

if P==0 and R==1:
    print ('C')
elif R==P==0:
    print ('A')
elif R==0 and P==1:
    print ('B')