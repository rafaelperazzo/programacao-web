# -*- coding: utf-8 -*-
from __future__ import division
n=input ('digite n:')
maior=0
menor=10
for i in range (0,n,1):
    x=input('nota:')
    if x>maior:
        maior=x
    if x<menor:
        menor=x
    print maior
    print menor