# -*- coding: utf-8 -*-
from __future__ import division
import math
resul=0
n=input('n:')
for i in range (0,n,1):
    resul=resul+((-1)**i)/(2*i+1)
print resul