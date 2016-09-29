# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o primeiro elemento do conjunto')
b=input('Digite o segundo elemento do conjunto')
c=input('Digite o terceiro elemento do conjunto')
d=input('Digite o quarto elemento do conjunto')
if (b>a and b>c) or (c>b and c>d):
    print ('S')
else:
    print('N')
