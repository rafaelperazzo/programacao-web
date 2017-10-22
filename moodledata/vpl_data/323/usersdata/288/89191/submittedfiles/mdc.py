# -*- coding: utf-8 -*-
import math
x=int(input('Digite um numero x: '))
y=int(input('Digite um numero y: '))
mdc=1
divisor=2
while divisor<=x:
    if x%divisor==0 and y%divisor==0:
        mdc=divisor
    divisor=divisor+1
print (mdc)
   