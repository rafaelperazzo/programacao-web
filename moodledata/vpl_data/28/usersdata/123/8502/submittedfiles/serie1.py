# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input('Digite n:')
soma=0
i=1
while i<=n:
    if(i%2)==1:
        soma=soma+(n/(n**2))
    if(i%2)==0:
        soma=soma-(n/(n**2))
    i=i+1
print('%.5f'%soma)
