# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o primeiro numero:')
cont=2
if a<10:
    print('1')
else:
    while a//10<10:
        print(cont)
        cont=cont+1
        