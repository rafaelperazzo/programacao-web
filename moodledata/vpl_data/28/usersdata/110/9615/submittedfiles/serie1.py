# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite n: ')
i=1
sp=0
sn=0
while i<=n:
    if i%2==0:
        sn=sn- i/(i*i)
    else:
        sp=sp+ i/(i*i)
    i=i+1
s=sn+sp
print(s)

