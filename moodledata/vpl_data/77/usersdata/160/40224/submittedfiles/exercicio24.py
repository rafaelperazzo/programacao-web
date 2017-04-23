# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:'))
b=int(input('Digite b:'))

mdc=1
divisor=2
a1=a%divisor==0
b1=b%divisor==0

while divisor<=a:
    if a%divisor==0 and b%divisor==0:
        mdc==divisor+1
        print(mdc)
