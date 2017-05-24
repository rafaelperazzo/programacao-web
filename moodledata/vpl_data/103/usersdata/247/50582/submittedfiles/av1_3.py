# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
if a>b:
    x1=a
    x2=b
    mdc=b
else:
    x1=b 
    x2=a
    mdc=a
cont=1
while x1%x2!=0:
    r=x1%x2
    x1=x2
    x2=r
    cont=cont+1
    mdc=r
print(mdc)
print(cont)
