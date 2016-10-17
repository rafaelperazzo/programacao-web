# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite a:')
b=input('Digite b:')
if a>b:
    n=a
if b>=a:
    n=b
x=0
i=2

while i<=n:
    if i%a==0 and i%b==0:
        x=x+1
        p=i
    i=i+1

print (p)
print (x)
    