# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
cont=0
resto=0
for i in range(1,a+1,1):
    if c//i!=0:
        cont=cont+1
if c%i!=0:
    resto=(c%i)
print(cont)
print(resto)
