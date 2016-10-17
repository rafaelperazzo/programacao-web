# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite o primeiro numero:'))
x=(a//10)
cont=1
while x>=10:
    x=(x//10)
    cont=cont+1
    print(cont)
while a>=10 and a<100:
    print ('2')
    break
else:
    print ('1')
    