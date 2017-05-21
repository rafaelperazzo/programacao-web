# -*- coding: utf-8 -*-
import math
n1=int(input('digite n1:'))
n2=int(input('digite n2:'))
mdc=n1
while n1%mdc!=0 or n2%mdc!=0:
    mdc=mdc-1
print(mdc)