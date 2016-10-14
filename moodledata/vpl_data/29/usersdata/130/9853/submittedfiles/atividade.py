# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('Digite o valor de n:'))
soma=0
while True:
    if n/10:
        soma=soma+1
    n=(n//10)
    if n==0:
        break
print (soma)    
