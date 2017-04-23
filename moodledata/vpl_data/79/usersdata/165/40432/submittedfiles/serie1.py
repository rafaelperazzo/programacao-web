# -*- coding: utf-8 -*-
import math
n=int(input('digite um valor para n:'))
s=0
numerador=1
for numerador in range (1,n+1,1):
    if numerador%2==0:
        s=s-numerador//(numerador**2)
    else:
        s=s+numerador//(numerador**2)
    print('%.5f' %s)
