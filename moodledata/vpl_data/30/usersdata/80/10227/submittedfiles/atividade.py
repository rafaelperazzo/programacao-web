# -*- coding: utf-8 -*-
from __future__ import division
import math

N=int(input('Digite o valor de N:'))

S=0
if N<0:
    K=N*(-1)
    J=K
    for i in range(1,N+1,1):
        S=(i/j)+S
        j=j-1
else:
    j=N
    for i in range(1,N+1,1):
        S=(i/j)+S
        j=j-1
print ('%.5f' %S)
