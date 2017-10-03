# -*- coding: utf-8 -*-
import math
num1=int(input('Digite n1: '))
num2=int(input('Digite n2: '))

resto=num1%num2
mdc=resto
while mdc is not 0:
    mdc=mdc-1
    
print(mdc)

