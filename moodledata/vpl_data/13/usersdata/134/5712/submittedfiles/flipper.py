# -*- coding: utf-8 -*-
from __future__ import division
import math

R = input('Digite a posição de R:')
P = input('Digite a posição de P:')

if P==0:
    print ('C')
if R==P==0:
    print ('A')
elif R==0 and P==1:
    print ('B')