# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite um numero:')
i=1
while(i*i+1*i+2)<a:
    if (i*(i+1)*(i+2))==a:
        print('s')
    if (i*(i+1)*(i+2))>a:
        print('n')
    i=i+1    