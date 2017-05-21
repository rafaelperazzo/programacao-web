# -*- coding: utf-8 -*-
import math
a=int(input('digite a'))
b=int(input('digite b'))
if a>0 and b>0:
    d=2
    while d<=a:
        if a%d==0 and b%d==0:
            mdc=d
        d+=1
    print("mdc(%d,%d)=%d" %(a,b,mdc))
        
