# -*- coding: utf-8 -*-
from __future__ import division
i=1000
x=i//100
y=i%100
while(i<=9999):
    if i**0.5==x+y:
        print(i)
    i=i+1    