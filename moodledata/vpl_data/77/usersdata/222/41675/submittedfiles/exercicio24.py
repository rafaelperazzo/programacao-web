# -*- coding: utf-8 -*-
import math
a=int(input('a:'))
b=int(input('b:'))
anterior=a
atual=b
resto=anterior%atual
if a<0:
    a*(-1)
if b<0:
    b*(-1)
while resto!=0:
    anterior=atual
    atual=resto
    resto=anterior%atual
print("MDC(%d,%d)=%d"%(a,b,atual))


    
