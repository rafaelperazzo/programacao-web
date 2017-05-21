# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
if a>0 and b>0:
    mdc=1
    if a>b:
        maior=a
    else:
        maior=b
    for i in range(1,maior):
        if a%i==0 and b%i==0:
            mdc=i
    print(mdc)
        
        
