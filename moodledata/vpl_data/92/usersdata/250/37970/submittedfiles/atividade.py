# -*- coding: utf-8 -*-
import math
n=int(input('digite um vlor:'))
if n<0:
    n=n*(-1)
i=0
contador=0
while i<=n:
    if n>0:
        s=(i/(n-(i-1)))
        contador=contador+1
    i=i+1
print('%.5f'%s)
