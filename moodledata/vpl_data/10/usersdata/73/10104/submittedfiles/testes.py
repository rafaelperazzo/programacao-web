# -*- coding: utf-8 -*-
from __future__ import division
n= input ('digite n:')
i=1
maior=0
menor=10
while (i<=n):
    x=input('digite a nota:')
    if x>maior:
        print i
    if x<menor:
        print i
    i=i+1