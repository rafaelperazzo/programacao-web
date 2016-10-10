# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
n=int(input('Digite o valor de n:'))
c=0
i=0
while i<n:
    if c%a==0 or c%b==0:
        print(c)
        i=i+1
    c=c+1