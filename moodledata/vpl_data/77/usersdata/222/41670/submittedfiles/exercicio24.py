# -*- coding: utf-8 -*-
import math
a=int(input('a:'))
b=int(input('b:'))
a>0
b>0
anterior=a
atual=b
resto=anterior%atual
while resto!=0:
    anterior=atual
    atual=resto
    resto=anterior%atual
print("MDC(%d,%d)=%d"%(a,b,atual))


    
