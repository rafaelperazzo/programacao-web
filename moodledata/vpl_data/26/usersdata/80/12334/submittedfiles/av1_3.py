# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o primeiro numero:')
x=a
cont=0
while (x%10)>=10:
    x=(x%10)
    cont=cont+1
    print(cont)
    