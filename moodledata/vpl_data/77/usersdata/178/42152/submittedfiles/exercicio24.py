# -*- coding: utf-8 -*-
import math

a=int(input('digite a:'))
b=int(input('digite b:'))


for i inrange (1,a+1,1):
    if a%i==0 and b%i==0:
        MDC=i
        
print (MDC)