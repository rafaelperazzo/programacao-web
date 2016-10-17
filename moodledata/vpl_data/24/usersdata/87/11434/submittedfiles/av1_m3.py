# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input("Digite valor de m: ")
i=0
j=1
while m>0:
    j=j+1
    if j%2==0:
        j=4/(i+1)*(i+2)*(i+3)
    if j%2==1:
        j=-4/(i+1)*(i+2)*(i+3)
    i=i+1
print("pi= %.6f" %pi)