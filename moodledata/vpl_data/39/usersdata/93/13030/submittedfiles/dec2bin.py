# -*- coding: utf-8 -*-
from __future__ import division
n=input('n: ')
b=0
c=n
i=1
while c!=0:
 b=b+(c%2)*10**i
 c=c//2
 i=i+1
print (b)
