# -*- coding: utf-8 -*-
import math
a=int(input('digite a'))
b=int(input('digite b'))
if a>0 and b>0:
    d=2
    while d>=a:
        d=d+1
        if a%d==0 and b%d==0:
            mdc=d
        print(mdc)
        
        
