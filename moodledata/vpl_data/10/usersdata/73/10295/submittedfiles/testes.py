# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite a:')
b=input('digite b:')
if a>=b:
    i=a
else:
    i=b
while True:
    if a%i==0 and b%i==0:
        print (i)
        break
    i=i-1