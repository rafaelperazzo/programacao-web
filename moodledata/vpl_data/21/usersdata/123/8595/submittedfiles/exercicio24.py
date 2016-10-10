# -*- coding: utf-8 -*-
from __future__ import division
import math

n= int(input('Digite n:'))
p= int(input('Digite p:'))

i=1
while i<=n and i<=p:
    if n%i==0 and p%i==0:
        mdc=i
    i=i+1
print mdc
