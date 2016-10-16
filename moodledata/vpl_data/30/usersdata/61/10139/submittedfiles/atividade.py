# -*- coding: utf-8 -*-
from __future__ import division
import math
s=0
n=input('Digite o valor de n: ')
if n<0:
    k=n*(-1)
    j=k
    for i in range (1,k+1,1):
        s=(i/j)+s
        j=j-1
else:
    j=n
    for i in range (1,n+1,1):
        s=(i/j)+s
        j=j-1
print ('%.5f' %s)
        

