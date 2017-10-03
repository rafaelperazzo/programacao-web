# -*- coding: utf-8 -*-
import math
num1=int(input('Digite n1: '))
num2=int(input('Digite n2: '))

mdc=1
divisor=2
while divisor<=num1:
    if divisor%num1 == 0 and divisor%num2==0:
        divisor=divisor+1
        mdc=mdc+1
print (mdc)
