# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('numero de divisores:')
a=input('numero 1:')
b=input('numero 2:')
i=1
c=0
while(c<n):
    if(i%a==0 or i%b==0):
        print(i)
        c=c+1
    i=i+1