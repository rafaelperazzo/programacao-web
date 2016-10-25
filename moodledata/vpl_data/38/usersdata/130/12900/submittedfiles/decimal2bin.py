# -*- coding: utf-8 -*-
from __future__ import division
b=input('Digite o valor de b:')
s=0
i=0
while True:
    if b//10>0:
        if b%10==0:
            s=s+(0*(2**i))
        else:
            s=s+(1*(2**i))
        i=i+1
        b=b//10
    else:
        break
s=s+(1*(2**(i+1)))
print(s)

