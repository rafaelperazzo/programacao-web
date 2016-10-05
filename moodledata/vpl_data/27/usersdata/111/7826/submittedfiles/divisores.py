# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite n: ')
a=input('Digite a: ')
b=input('Digite b: ')

i=0
while i<=n:
    if a%i == 0:
        print i
    if b%i == 0:
        print i
    i=i+1
print i

    