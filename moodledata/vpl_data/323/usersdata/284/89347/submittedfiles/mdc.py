# -*- coding: utf-8 -*-
import math

x=int(input('digite o valor:'))
def divisor (x):
    for n in range(1,x+1,1):
        if(x%n==0):
            return(n)
            break

