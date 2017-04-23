# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:'))
b=int(input('Digite b:'))

mdc=1
divisor=2

while divisor<=a:
    if a%divisor==0 and b%divisor==0:
        mdc==divisor
        divisor==a+1
        print(divisor)
