# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
if a>b:
    x=a and x2=b and mdc=b
else:
    x1=b and x2=a and mdc=a
cont=1
while a%b!=0:
    r=a%b
    a=b
    b=r
    cont=cont+1
    mdc=r
print(mdc)
print(cont)
