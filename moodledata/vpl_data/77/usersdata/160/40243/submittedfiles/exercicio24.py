# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:'))
b=int(input('Digite b:'))


divisor=1
mdc1=a%divisor
mdc2=b%divisor
mdc=mdc1==mdc2

while mdc<=a:
    if mdc==0:
        if mdc1>mdc2:
            print(mdc1)
        elif mdc1<mdc2:
            print(mdc2)
            
    
    
