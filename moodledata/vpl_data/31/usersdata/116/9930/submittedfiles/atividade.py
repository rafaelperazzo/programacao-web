# -*- coding: utf-8 -*-
from __future__ import division
import math
n = int (input ('insira o valor de n:') )

i=1

while i<=n:
    x=input ('insira x:')
    y=input ('insira y:')
    if (x**2)+(y**2)<=1:
        print ('SIM')
    else:
        print ('NAO')
    i=i+1
