# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero:'))
b=int(input('digite um numero:'))
mdc=a
cont=0
while a%mdc!=0 or b%mdc!=0:
    cont=cont+1
    mdc=mdc-1
print(mdc)
print(cont)