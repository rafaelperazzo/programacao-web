# -*- coding: utf-8 -*-
import math
num1=int(input('Digite n1: '))
num2=int(input('Digite n2: '))

mdc=num1

while mdc!=0 or (num2%mdc)!=0 :
    mdc=mdc-1
    
print(mdc)

