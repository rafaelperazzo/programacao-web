# -*- coding: utf-8 -*-
import math

n=int(input('Digite n:'))

a=2
b=3
c=4
soma=0

for i in range (0,n,1):
    if  i%2==0:
        soma=soma+4/(a*b*c)
    else:
        soma=soma-4/(a*b*c)
    a=a+2
    b=b+2
    c=c+2
somab=soma+3
print('%.6f'%somab)

