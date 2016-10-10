# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input('Digite n:')
p= input('Digite p:')

i=2
while i<=n and i<=p:
    if n%i==0 and p%i==0:
        mdc=i
    i=i+1
print mdc
