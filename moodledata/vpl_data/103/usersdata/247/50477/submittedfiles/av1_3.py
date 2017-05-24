# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
cont=0
mdc=0
d=b
while mdc==0:
    cont=cont+1
    if a%b==0 and d%b==0:
        mdc=b
    else:
        b=b-1
d=d-cont
print(mdc)
print(d)
