# -*- coding: utf-8 -*-
from __future__ import division
import math
#entrada
i=1
mdc=1
a=input('digite o valor do primeiro numero :')
b=input('digite o valor do segundo numero :')
#processamento e saida 
while (i<=a) and (i<=b):
    if a%i==0 and b%i==0:
        mdc=i
    i=i+1
    
print(mdc)
