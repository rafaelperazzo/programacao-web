# -*- coding: utf-8 -*-
from __future__ import division
import math
n1=input('Digite n1: ')
n2=input('Digite n2: ')
a1=n1
a2=n2
cont=1
if  a1%a2!=0: 
    while a1%a2!=0:
     r=a1%a2
     cont=cont+1
     a1=a2
     a2=r
  print(r)
  print(cont)
else:
    print(a2)
    print(cont)


