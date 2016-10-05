# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input("valor de a:"))
b = int(input("valor de b:"))

mdc=a
while a % mdc !=0 or b % mdc !=0:
    mdc = mdc -1
    
print(mdc)