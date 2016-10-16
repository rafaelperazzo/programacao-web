# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite um numero:')
i=1

while True:
    
    if i*(i+1)*(i+2)==a:
        print('s')
        break
    if i*(i+1)*(i+2)>a:
        print('n')
        break
    i=i+1
    
