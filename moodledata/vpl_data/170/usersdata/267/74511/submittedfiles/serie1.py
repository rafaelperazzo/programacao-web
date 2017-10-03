# -*- coding: utf-8 -*-
import math

n=int(input('Número de termos: '))
num=1
den=1
s=0
i=1
while num<=n:
    s=s+num/den
    i=i+2
    num=num+1
    den=den+i
print(%.5f %s)