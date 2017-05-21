# -*- coding: utf-8 -*-
import math
a=int(input('digite o numero a:'))
b=int(input('digite o numero b:'))
anterior=a
atual=b
resto=anterior%atual
while resto!=0:
    anterior=atual
    atual=resto
    resto=anterior%atual
print("mdc(%d,%d)=%d"%(a,b,atual))