# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input("Digite valor de n:"))

i=0

while n>0:
    n=n//10
    i=i+1
print(i)