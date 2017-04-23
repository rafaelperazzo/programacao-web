# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:'))
b=int(input('Digite b:'))


divisor=2
mdc1=a%divisor
mdc2=b%divisor
mdc=mdc1==mdc2

while divisor<=a:
    if mdc==0:
        print(mdc)
        mdc==divisor+1
    
