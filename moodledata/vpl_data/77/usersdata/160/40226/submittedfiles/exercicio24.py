# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:'))
b=int(input('Digite b:'))


divisor=2
mdc1=a%divisor
mdc2=b%divisor

while divisor<=a:
    if mdc1==0 and mdc2==0:
        mdc==divisor+1
        print(mdc)
