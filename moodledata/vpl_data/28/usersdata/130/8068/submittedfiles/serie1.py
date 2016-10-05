# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('Digite o valor de n:')
i=1
while i<=n:
    if i%2==0:
        soma=soma+(i)/(i)**2
    else:
        soma=soma-(i)/(i)**2
    i=i+1    
print('%.5f'% soma)        

