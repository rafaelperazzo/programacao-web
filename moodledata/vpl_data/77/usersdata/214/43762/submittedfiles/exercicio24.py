# -*- coding: utf-8 -*-
import math

n= int(input ("digite o valor de n:"))
m= int(input ("digite o valor de m:"))
mdc = 1
while divisor <= n:
    if n % divisor == 0 and m % divisor == 0:
      mdc = divisor
    divisor += 1
print("MDC (%d,%d)=%d" %(n,m,mdc))