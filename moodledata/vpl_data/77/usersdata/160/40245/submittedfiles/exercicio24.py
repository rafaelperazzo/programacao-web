# -*- coding: utf-8 -*-
import math

a=int(input('Digite a:'))
b=int(input('Digite b:'))


divisor=1


while mdc<=a:
    mdc1=a%divisor
    mdc2=b%divisor
    mdc=mdc1==mdc2

    if mdc==0:
        if mdc1>mdc2:
            print(mdc1)
        elif mdc1<mdc2:
            print(mdc2)
            
    
    
