# -*- coding: utf-8 -*-
import math
n1=int(input('digite n1:'))
n2=int(input('digite n2:'))
n1>0
n2>0
mdc=1
divisor=2
while divisor<=n1:
    if n1%divisor==0 and n2%divisor==0:
        mdc=divisor
    divisor+=1
    print("mdc(%d,%d)=%d %(n1,n2,mdc))
    