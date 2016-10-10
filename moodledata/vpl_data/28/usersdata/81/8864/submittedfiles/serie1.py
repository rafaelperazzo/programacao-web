# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite o valo r de n:'))
soma=0

for i in range (1,n+1,1):
    soma=soma+((i**-1)*((-1)**(i+1)))

print(%.5f'%soma)
