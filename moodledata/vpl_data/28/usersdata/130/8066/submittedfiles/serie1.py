# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:')
i=0
while i<=n:
    if i%2==0:
        soma=soma+(1+i)/(i+1)**2
    else:
        soma=soma-(1+i)/(i+1)**2
print('%.5f'% soma)        

