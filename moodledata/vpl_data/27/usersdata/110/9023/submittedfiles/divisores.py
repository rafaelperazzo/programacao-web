# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('Digite n: '))
a=int(input('Digite a: '))
b=int(input('Digite b: '))
i=0
d=2
while i<n:
   if d%a==0 or d%b==0:
       print(d)
       i=i+1
       d=d+1
    

