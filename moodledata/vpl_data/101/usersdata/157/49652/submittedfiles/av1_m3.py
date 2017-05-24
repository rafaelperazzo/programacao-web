# -*- coding: utf-8 -*-
import math
n=int(input('Digite um valor: '))
pi=3
for i in range (3,n+1,1):
    if (i%3==1):
        pi=pi+(i/(i**2))
    else:
        pi=pi-(i/(i**2))
print ('%.6f'%pi)
