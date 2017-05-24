# -*- coding: utf-8 -*-
import math

d=2
e=3
f=4
soma=0

for i in range(0,n,1):
    if  i%2==0:
        soma=soma+4/(d*e*f)
    else:
        soma=soma-4/(d*e*f)
    d=d+2
    e=e+2
    f=f+2
somab=soma+3
print('%.6f'%somab)