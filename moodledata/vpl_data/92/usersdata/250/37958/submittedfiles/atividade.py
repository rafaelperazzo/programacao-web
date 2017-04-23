# -*- coding: utf-8 -*-
import math
n=int(input('digite um vlor:'))
i=1
contador=0
while i<=n:
    if n>0:
        s=(i/(n-(i-1)))
        contador=contador+1
    i=i+1
print('%.5f'%s)
