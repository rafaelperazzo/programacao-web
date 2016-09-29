# -*- coding: utf-8 -*-
from __future__ import division
import math

p = input ('digite a posição de P:')
r = input ('digite a posição de R:')

if p==0 and r==0:
    print ('C')
if p==0 and r==1:
    print ('C')
if p==1 and r==0:
    print ('B')
if p==1 and r==1:
    print ('A')