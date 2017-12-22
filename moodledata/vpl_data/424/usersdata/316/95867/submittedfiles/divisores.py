# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de multiplos que devem ser mostrados:'))
n1=int(input('digite um numero:'))
n2=int(input('digite um numero:'))
mult=0
k=0
while k<n:
    if mult%n1 == 0 or mult%n2 == 0:
        print(mult)
        k = k + 1
    mult=mult+1