# -*- coding: utf-8 -*-
import math
a=int(input('digite a :'))
b=int(input('digite b :'))
mdc=a

while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
print (mdc)