# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))

cont=1
mdc=0
d=b
while a%b!=0:
    r=a%b
    a=b
    b=r
    cont=cont+1
    mdc=r
print(mdc)
print(cont)
