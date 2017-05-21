# -*- coding: utf-8 -*-
for a in range(1000,10000,1):
    x=a//100
    y=a%100
    if a**(1/2)==x+y:
        print(a)

