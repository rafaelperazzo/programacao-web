# -*- coding: utf-8 -*-
import math
n=int(input('Digite n:'))
soma=0
d=1
for n in range (1,n+1,1):
    if n%2==0:
        soma=soma-n/d
    else:
        soma=+n/d
        d=n**2
print(soma)

