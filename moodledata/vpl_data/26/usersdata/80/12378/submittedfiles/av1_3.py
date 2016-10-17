# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o primeiro numero:')
x=(a//10)
cont=1
while x>=10:
    print(cont)
    x=(x//10)
    cont=cont+1
    