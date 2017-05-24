# -*- coding: utf-8 -*-
import math
a=int(input('digite um numero:'))
b=int(input('digite um numero:'))
mdc=a
resto=a%b
cont=0
while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
while resto!=0:
    a%b
    cont=cont+1
    a=b
    b=resto
print(mdc)
print(cont)