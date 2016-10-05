# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('insira o valor de n:'))
soma=0

for i in range (1,n,2):
    soma= soma+((1/i)*(-1^(i+1)))
    
print soma    
