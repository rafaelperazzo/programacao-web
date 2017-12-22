# -*- coding: utf-8 -*-
import math
x1=int(input(''))
x2=int(input(''))
if x1>x2:
    mdc=x1
    while x1%mdc!=0 or x2%mdc!=0:
        mdc=mdc-1
    print(mdc)
if x2>x1:
    mdc=x2
    while x1%mdc!=0 or x2%mdc!=0:
        mdc=mdc-1
    print(mdc)