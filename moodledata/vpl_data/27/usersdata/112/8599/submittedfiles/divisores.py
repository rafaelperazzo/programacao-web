# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
n=int(input('Digite o valor de n:'))
c=0
i=2
for i in range (0,n+1,1):
    if a%i==0 or b%i==0:
        print(i)
        c=c+1
    i=i+1