# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input("Digite o valor de n:"))
if n<0:
    n=n*(-1)
i=1
j=0
somatorio=0
for i in range(1,n+1,1):
    somatorio=i/(n-j)
    j=j-1
    print(somatorio)
    

    