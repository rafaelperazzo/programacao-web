# -*- coding: utf-8 -*-
import math
a=int(input('a (a>0):'))
b=int(input('b (b>0):'))
anterior=a
atual=b
resto=anterior%atual
while resto!=0:
    anterior=atual
    atual=resto
    resto=anterior%atual
print("MDC(%d,%d)=%d"%(a,b,atual))


    
