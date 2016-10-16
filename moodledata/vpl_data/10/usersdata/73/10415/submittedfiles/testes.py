# -*- coding: utf-8 -*-
from __future__ import division
n=input ('digite n:')
soma=0
for i in range (0,n+1,1):
    a=(((-1)**i)/(2*i+1))*4
    soma=soma+a
print soma