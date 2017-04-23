# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
divisor=2
while divisor<=a:
    if a%divisor==0 and b%divisor==0:
        divisor=divisor+1
        mdc=divisor
print(mdc)        
        
        
