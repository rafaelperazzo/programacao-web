# -*- coding: utf-8 -*-
import math
a=int(input('digite o numero a:'))
b=int(input('digite o numero b:'))
if a>=b:
    M=a
    m=b
else:
    M=b
    m=a
MDC=0    
while MDC==0:
    if a%m==0 and b%m==0:
        MDC=m
    else:
        m=m-1
print('MDC')    
    