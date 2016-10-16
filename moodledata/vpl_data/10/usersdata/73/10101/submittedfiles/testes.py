# -*- coding: utf-8 -*-
from __future__ import division
n= input ('digite n:')
maior=0
menor=10
for i in range(0,n,1):
    x=input('digite a nota:')
    if i>maior:
        print maior
    if i<menor:
        print menor
    i=i+1