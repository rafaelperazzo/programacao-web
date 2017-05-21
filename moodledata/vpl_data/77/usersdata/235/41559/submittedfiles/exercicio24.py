# -*- coding: utf-8 -*-
import math
x=int(input('digite x:'))
y=int(input('digite y:'))
if x<=y:
    i=x
else:
    i=y
while i>0:
    if (x%i=0)==(y%i=0):
        print (i)
i=i-1    