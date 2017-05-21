# -*- coding: utf-8 -*-
import math
a=int(input('diite a:'))
b=int(input('diite b:'))
mdc=a
while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
print(mdc)
